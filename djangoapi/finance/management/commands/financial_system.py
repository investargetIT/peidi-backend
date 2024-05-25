from django.core.management.base import BaseCommand
from django.db.models import Sum

from goods.models import SpecGoods, SuiteGoodsRec
from finance.models import Invoice, FinanceSalesAndInvoice, PDMaterialNOList, GoodsSalesSummary, DouyinRefund, PddRefund, JdRefund, TmallRefund
from orders.models import salesOutDetails

class Command(BaseCommand):

    def handle(self, *args, **options):
        # print(self.goods_no_to_material_no("6971758277324"))

        # distinct_trade_no = Invoice.objects.values("trade_no").distinct()
        # for i in distinct_trade_no:
        #     merged_invoice = self.merge_original_invoice(i['trade_no'])
        #     for invoice in merged_invoice:
        #         self.goods_model_to_spec_goods(invoice)

        # self.finance_sales_invoice_summary('2024-03-26', '2024-04-25')

        # self.goods_sales_summary("2024-03-26", "2024-04-25")

        # self.extend_douyin_refund("2024-02-01", "2024-02-29")

        # self.extend_jd_refund("2024-02-01", "2024-02-29")

        self.extend_pdd_refund("2024-02-01", "2024-02-29")
    
    def goods_model_to_spec_goods(self, finance_sales_and_invoice):
        goods_model = finance_sales_and_invoice.goods_no
        try:
            spec_goods = SpecGoods.objects.get(spec_no=goods_model)
            # print(spec_goods.spec_no, '是单品', spec_goods.goods_name)
            finance_sales_and_invoice.material_no = self.goods_no_to_material_no(spec_goods.spec_no)
            finance_sales_and_invoice.goods_name = spec_goods.goods_name
            finance_sales_and_invoice.save()
            # print()
        except SpecGoods.DoesNotExist:
            suite_goods = SuiteGoodsRec.objects.filter(suite_no=goods_model)
            if len(suite_goods) > 0:
                # print(goods_model, '是组合装，包括以下单品：')
                for goods in suite_goods:
                    # print(goods.spec_no, goods.goods_name, goods.num, goods.ratio)
                    material_no = self.goods_no_to_material_no(goods.spec_no)
                    f = FinanceSalesAndInvoice(
                        date=finance_sales_and_invoice.date,
                        shop_name=finance_sales_and_invoice.shop_name,
                        material_no=material_no,
                        goods_no=goods.spec_no,
                        goods_name=goods.goods_name,
                        invoice_num=finance_sales_and_invoice.invoice_num*goods.num,
                        invoice_amount=finance_sales_and_invoice.invoice_amount*goods.ratio
                    )
                    f.save()
                # print()
            else:
                print('该商品不存在', goods_model)
                # 作为单品处理
                finance_sales_and_invoice.save()

    def merge_original_invoice(self, trade_no):
        result = []
        # 以订单id、商品型号、开票日期和店铺名称为唯一数据，合并发票总金额，即对冲掉优惠返现等负的发票总金额
        invoices = Invoice.objects.values("trade_no", "goods_model", "invoice_time", "shop_name").filter(trade_no=trade_no).annotate(Sum("goods_total_amount"), Sum("goods_num"))
        for invoice in invoices:
            date = invoice['invoice_time']
            shop_name = invoice['shop_name']
            goods_no = invoice['goods_model']
            invoice_num = invoice['goods_num__sum']
            invoice_amount = invoice['goods_total_amount__sum']
            print(date, shop_name, goods_no, invoice_num, invoice_amount)

            f = FinanceSalesAndInvoice(
                date=date,
                shop_name=shop_name,
                goods_no=goods_no,
                invoice_num=invoice_num,
                invoice_amount=invoice_amount
            )
            result.append(f)
        print()
        return result

    def goods_no_to_material_no(self, goods_no):
        # try:
        #     material = PDMaterialNOList.objects.get(barcode=goods_no)
        #     # print(material)
        #     return material.material_no
        # except PDMaterialNOList.DoesNotExist as e:
        #     print(e)
        # except PDMaterialNOList.MultipleObjectsReturned as e:
        #     print(e)
        
        result = []
        materials = PDMaterialNOList.objects.filter(barcode=goods_no)
        for material in materials:
            result.append(material.material_no)
        return '/'.join(result)

    def finance_sales_invoice_summary(self, start_date, end_date):
        details = FinanceSalesAndInvoice.objects.values(
            "shop_name",
            "goods_no",
            "material_no",
            "goods_name",
        ).filter(
            date__gte=start_date, 
            date__lte=end_date,
        ).annotate(
            details_sum_num=Sum("invoice_num"),
            details_price=Sum("invoice_amount") / Sum("invoice_num"),
            details_sum_amount=Sum("invoice_amount"),
        )
        for i in details:
            print(i)

        summary = details.aggregate(
            total_num=Sum("details_sum_num"),
            total_price=Sum("details_sum_amount") / Sum("details_sum_num"),
            total_amount=Sum("details_sum_amount"),
        )
        print(summary)

        return details

    def goods_sales_summary(self, start_date, end_date):
        details = GoodsSalesSummary.objects.values(
            "spec_no",
            "shop_name",
        ).filter(
            start_date__gte=start_date,
            end_date__lte=end_date,
        ).annotate(
            details_sum_num=Sum("sales_num"),
            details_sum_post=Sum("post_amount"),
            details_sum_amount=Sum("actual_sales_amount"),
        )
        for i in details:
            print(i)
        
        summary = details.aggregate(
            total_num=Sum("details_sum_num"),
            total_post=Sum("details_sum_post"),
            total_amount=Sum("details_sum_amount"),
        )
        print(summary)

        return details
    
    def extend_douyin_refund(self, start_date, end_date):
        end_date += " 23:59:59" 
        refund_records = DouyinRefund.objects.filter(refund_time__range=(start_date, end_date))
        for refund_record in refund_records:
            print(refund_record)   
            trade_no = refund_record.trade_no
            refund = refund_record.refund
            refund_time = refund_record.refund_time

            salesout_records = salesOutDetails.objects.filter(otid=trade_no)
            overall_amount = salesout_records.aggregate(Sum("deal_total_price"))
            for i in salesout_records:
                print(i)
                f = FinanceSalesAndInvoice(
                    date=refund_time,
                    shop_name=i.shop_name,
                    goods_no=i.spec_no,
                    refund_amount=i.deal_total_price/overall_amount['deal_total_price__sum']*refund
                )
                f.save()
    
    def extend_jd_refund(self, start_date, end_date):
        end_date += " 23:59:59" 
        refund_records = JdRefund.objects.filter(apply_time__range=(start_date, end_date))
        for refund_record in refund_records:
            print(refund_record)
            trade_no = refund_record.trade_no
            refund = refund_record.refund
            refund_time = refund_record.apply_time

            salesout_records = salesOutDetails.objects.filter(otid=trade_no)
            overall_amount = salesout_records.aggregate(Sum("deal_total_price"))
            for i in salesout_records:
                print(i)
                f = FinanceSalesAndInvoice(
                    date=refund_time,
                    shop_name=i.shop_name,
                    goods_no=i.spec_no,
                    refund_amount=i.deal_total_price/overall_amount['deal_total_price__sum']*refund
                )
                f.save()
    
    def extend_pdd_refund(self, start_date, end_date):
        end_date += " 23:59:59" 
        refund_records = PddRefund.objects.filter(apply_time__range=(start_date, end_date))
        for refund_record in refund_records:
            print(refund_record)
            trade_no = refund_record.trade_no
            refund = refund_record.refund
            refund_time = refund_record.apply_time

            salesout_records = salesOutDetails.objects.filter(otid=trade_no)
            overall_amount = salesout_records.aggregate(Sum("deal_total_price"))
            for i in salesout_records:
                print(i)
                f = FinanceSalesAndInvoice(
                    date=refund_time,
                    shop_name=i.shop_name,
                    goods_no=i.spec_no,
                    refund_amount=i.deal_total_price/overall_amount['deal_total_price__sum']*refund
                )
                f.save()

