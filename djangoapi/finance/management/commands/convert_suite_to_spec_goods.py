from django.core.management.base import BaseCommand
from django.db.models import Sum

from goods.models import SpecGoods, SuiteGoodsRec
from finance.models import Invoice

class Command(BaseCommand):

    def handle(self, *args, **options):
        # all_invoices = Invoice.objects.all()
        # print(len(all_invoices))
        # for invoice in all_invoices:
        #     if invoice.goods_model:
        #         self.goods_model_to_spec_goods(invoice.goods_model)
        self.trim_original_invoice('3848946120620204220')
    
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

    def trim_original_invoice(self, trade_no):
        invoices = Invoice.objects.values("trade_no", "goods_model").filter(trade_no=trade_no).annotate(Sum("goods_total_amount"))
        for invoice in invoices:
            print(invoice)
