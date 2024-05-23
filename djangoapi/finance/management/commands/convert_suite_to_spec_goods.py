from django.core.management.base import BaseCommand
from django.db.models import Sum

from goods.models import SpecGoods, SuiteGoodsRec
from finance.models import Invoice, FinanceSalesAndInvoice

class Command(BaseCommand):

    def handle(self, *args, **options):
        distinct_trade_no = Invoice.objects.values("trade_no").distinct()
        for i in distinct_trade_no:
            merged_invoice = self.merge_original_invoice(i['trade_no'])
            for invoice in merged_invoice:
                self.goods_model_to_spec_goods(invoice)
    
    def goods_model_to_spec_goods(self, finance_sales_and_invoice):
        goods_model = finance_sales_and_invoice.goods_no
        try:
            spec_goods = SpecGoods.objects.get(spec_no=goods_model)
            print(spec_goods.spec_no, '是单品', spec_goods.goods_name)
            finance_sales_and_invoice.goods_name = spec_goods.goods_name
            finance_sales_and_invoice.save()
            print()
        except SpecGoods.DoesNotExist:
            suite_goods = SuiteGoodsRec.objects.filter(suite_no=goods_model)
            if len(suite_goods) > 0:
                print(goods_model, '是组合装，包括以下单品：')
                for goods in suite_goods:
                    print(goods.spec_no, goods.goods_name, goods.num, goods.ratio)
                    f = FinanceSalesAndInvoice(invoice_time=finance_sales_and_invoice.invoice_time, shop_name=finance_sales_and_invoice.shop_name, goods_no=goods.spec_no, goods_name=goods.goods_name, num=finance_sales_and_invoice.num*goods.num, price_with_tax=finance_sales_and_invoice.price_with_tax*goods.ratio)
                    f.save()
                print()
            else:
                print('该商品不存在', goods_model)
                # 作为单品处理
                finance_sales_and_invoice.save()

    def merge_original_invoice(self, trade_no):
        result = []
        # 以订单id、商品型号、开票日期和店铺名称为唯一数据，合并发票总金额，即对冲掉优惠返现等负的发票总金额
        invoices = Invoice.objects.values("trade_no", "goods_model", "invoice_time", "shop_name").filter(trade_no=trade_no).annotate(Sum("goods_total_amount"), Sum("goods_num"))
        for invoice in invoices:
            invoice_time = invoice['invoice_time']
            shop_name = invoice['shop_name']
            goods_no = invoice['goods_model']
            num = invoice['goods_num__sum']
            price_with_tax = invoice['goods_total_amount__sum']

            print(invoice_time, shop_name, goods_no, num, price_with_tax)
            f = FinanceSalesAndInvoice(invoice_time=invoice_time, shop_name=shop_name, goods_no=goods_no, num=num, price_with_tax=price_with_tax)
            result.append(f)
        print()
        return result
