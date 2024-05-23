from django.core.management.base import BaseCommand
from django.db.models import Sum

from goods.models import SpecGoods, SuiteGoodsRec
from finance.models import Invoice, FinanceSalesAndInvoice

class Command(BaseCommand):

    def handle(self, *args, **options):
        # all_invoices = Invoice.objects.all()
        # print(len(all_invoices))
        # for invoice in all_invoices:
        #     if invoice.goods_model:
        #         self.goods_model_to_spec_goods(invoice.goods_model)
        finance_sales_and_invoice = self.merge_original_invoice('3848946120620204220')
        print(finance_sales_and_invoice.invoice_time)
    
    def goods_model_to_spec_goods(self, goods_model):
        try:
            spec_goods = SpecGoods.objects.get(spec_no=goods_model)
            print('单品', spec_goods.spec_no, spec_goods.goods_name)
        except SpecGoods.DoesNotExist:
            suite_goods = SuiteGoodsRec.objects.filter(suite_no=goods_model)
            if len(suite_goods) > 0:
                print('组合装，包括以下单品：')
                for goods in suite_goods:
                    print(goods.spec_no, goods.goods_name)
            else:
                print('该商品不存在', goods_model)
                # 作为单品处理

    def merge_original_invoice(self, trade_no):
        # 以订单 id 和商品型号为唯一数据，合并发票总金额，即对冲掉优惠返现等负的发票总金额
        invoices = Invoice.objects.values("trade_no", "goods_model").filter(trade_no=trade_no).annotate(Sum("goods_total_amount"))
        for invoice in invoices:
            no = invoice['trade_no']
            model = invoice['goods_model']
            price_with_tax = invoice['goods_total_amount__sum']

            # 根据合并结果中的订单 id 和 商品型号拿到商品数量
            target_item = Invoice.objects.filter(trade_no=no).filter(goods_model=model).exclude(goods_num=None).values()
            if len(target_item) > 1:
                raise Exception("根据该订单 id 和商品型号找到了2条或2条以上商品数量不为空的记录", no, model)
            
            invoice_time = target_item[0]['invoice_time']
            shop_name = target_item[0]['shop_name']
            goods_no = target_item[0]['goods_model']
            num = target_item[0]['goods_num']

            return FinanceSalesAndInvoice(invoice_time=invoice_time, shop_name=shop_name, goods_no=goods_no, num=num, price_with_tax=price_with_tax)
