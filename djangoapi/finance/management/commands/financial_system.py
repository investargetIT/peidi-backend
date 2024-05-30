import requests, os
from django.core.management.base import BaseCommand
from django.db.models import Sum

from goods.models import SpecGoods, SuiteGoodsRec
from finance.models import Invoice, FinanceSalesAndInvoice, PDMaterialNOList, GoodsSalesSummary, DouyinRefund, PddRefund, JdRefund, TmallRefund
from orders.models import salesOutDetails

class Command(BaseCommand):

    def handle(self, *args, **options):
        print("Hello")

        # print(self.goods_no_to_material_no("6971758277324"))
        
        # merged_invoice = self.merge_original_invoice("2024-02-26", "2024-03-25")
        # for invoice in merged_invoice:
        #     self.goods_model_to_spec_goods(invoice)

        # self.extend_douyin_refund("2024-02-26", "2024-03-25")

        # self.extend_jd_refund("2024-02-26", "2024-03-25")

        # self.extend_pdd_refund("2024-02-26", "2024-03-25")

        # self.extend_tmall_refund("2024-02-26", "2024-03-25")

        # self.refund_summary("2024-02-26", "2024-03-25")

        # self.sales_summary("2024-02-26", "2024-03-25")

        # self.invoice_summary('2024-02-26', '2024-03-25')

        # self.overall_summary("2024-02-26", "2024-03-25")
    
    def goods_model_to_spec_goods(self, finance_sales_and_invoice):
        goods_model = finance_sales_and_invoice.goods_no
        try:
            spec_goods = SpecGoods.objects.get(spec_no=goods_model)
            # print(spec_goods.spec_no, '是单品', spec_goods.goods_name)
            finance_sales_and_invoice.goods_name = spec_goods.goods_name
            finance_sales_and_invoice.save()
            # print()
        except SpecGoods.DoesNotExist:
            suite_goods = SuiteGoodsRec.objects.filter(suite_no=goods_model)
            if len(suite_goods) > 0:
                # print(goods_model, '是组合装，包括以下单品：')
                for goods in suite_goods:
                    # print(goods.spec_no, goods.goods_name, goods.num, goods.ratio)
                    f = FinanceSalesAndInvoice(
                        date=finance_sales_and_invoice.date,
                        shop_name=finance_sales_and_invoice.shop_name,
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

    def merge_original_invoice(self, start_date, end_date):
        result = []
        end_date += " 23:59:59" 
        distinct_trade_no = Invoice.objects.filter(invoice_time__range=(start_date, end_date)).values("trade_no").distinct()
        print("阿里发票原始单号", len(distinct_trade_no))
        for i in distinct_trade_no:
            if i["trade_no"] is None:
                continue
            print(i)
            # 以订单id、商品型号、开票日期和店铺名称为唯一数据，合并发票总金额，即对冲掉优惠返现等负的发票总金额
            invoices = Invoice.objects.values("trade_no", "goods_model", "invoice_time", "shop_name").filter(trade_no=i['trade_no']).annotate(Sum("goods_total_amount"), Sum("goods_num"))
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
        
        # 财务手动创建的发票是没有订单号的
        manual_invoices = Invoice.objects.filter(invoice_time__range=(start_date, end_date), trade_no__isnull=True).values()
        print("人工发票", len(manual_invoices))
        for invoice in manual_invoices:
            date = invoice['invoice_time']
            shop_name = invoice['shop_name']
            goods_no = invoice['goods_model']
            invoice_num = invoice['goods_num']
            invoice_amount = invoice['goods_total_amount']
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
        
        material_no, goods_name = [], []
        materials = PDMaterialNOList.objects.filter(barcode=goods_no)
        for material in materials:
            material_no.append(material.material_no)
            goods_name.append(material.goods_name)
        return ("/".join(material_no), "/".join(goods_name))

    def invoice_summary(self, start_date, end_date):
        details = FinanceSalesAndInvoice.objects.values(
            "shop_name",
            "goods_no",
            "material_no",
            "goods_name",
        ).filter(
            date__gte=start_date, 
            date__lte=end_date,
            invoice_num__isnull=False,
            invoice_amount__isnull=False,
        ).annotate(
            details_sum_num=Sum("invoice_num"),
            details_price=Sum("invoice_amount") / Sum("invoice_num"),
            details_sum_amount=Sum("invoice_amount"),
        )
        for i in details:
            print(i)
            shop_name = i['shop_name']
            goods_no = i['goods_no']
            invoice_num = i['details_sum_num']
            invoice_amount = i['details_sum_amount']
            f = FinanceSalesAndInvoice(
                start_date=start_date,
                end_date=end_date,
                shop_name=shop_name,
                goods_no=goods_no,
                invoice_num=invoice_num,
                invoice_amount=invoice_amount,
            )
            f.save()

        # summary = details.aggregate(
        #     total_num=Sum("details_sum_num"),
        #     total_price=Sum("details_sum_amount") / Sum("details_sum_num"),
        #     total_amount=Sum("details_sum_amount"),
        # )
        # print(summary)

        # return details

    def sales_summary(self, start_date, end_date):
        details = GoodsSalesSummary.objects.values(
            "spec_no",
            "shop_name",
        ).filter(
            start_date__gte=start_date,
            end_date__lte=end_date,
        ).annotate(
            details_sum_num=Sum("sales_num")+Sum("ship_refund_num"),
            details_sum_post=Sum("post_amount"),
            details_sum_amount=Sum("actual_sales_amount")+Sum("ship_refund_amount"),
        )
        for i in details:
            print(i)
            shop_name = i['shop_name']
            goods_no = i['spec_no']
            sales_num = i['details_sum_num']
            sales_amount = i['details_sum_amount']
            post_amount = i['details_sum_post']
            f = FinanceSalesAndInvoice(
                start_date=start_date,
                end_date=end_date,
                shop_name=shop_name,
                goods_no=goods_no,
                sales_num=sales_num,
                sales_amount=sales_amount,
                post_amount=post_amount,
            )
            f.save()
        
        summary = details.aggregate(
            total_num=Sum("details_sum_num"),
            total_post=Sum("details_sum_post"),
            total_amount=Sum("details_sum_amount"),
        )
        print(summary)
    
    def extend_douyin_refund(self, start_date, end_date):
        end_date += " 23:59:59" 
        refund_records = DouyinRefund.objects.filter(refund_time__range=(start_date, end_date))
        for refund_record in refund_records:
            trade_no = refund_record.trade_no
            refund = refund_record.refund
            if refund == 0:
                continue

            refund_time = refund_record.refund_time
            salesout_records = salesOutDetails.objects.filter(otid=trade_no)

            if len(salesout_records) == 0:
                print("未找到关联订单", refund_record)
            
            overall_amount = 0
            for i in salesout_records:
                overall_amount += i.deal_total_price
            if overall_amount == 0:
                continue
            
            for i in salesout_records:
                if i.deal_total_price == 0:
                    continue
                f = FinanceSalesAndInvoice(
                    date=refund_time,
                    shop_name=i.shop_name,
                    goods_no=i.spec_no,
                    refund_amount=i.deal_total_price/overall_amount*refund
                )
                f.save()
    
    def extend_jd_refund(self, start_date, end_date):
        end_date += " 23:59:59" 
        refund_records = JdRefund.objects.filter(apply_time__range=(start_date, end_date))
        for refund_record in refund_records:
            trade_no = refund_record.trade_no
            refund = refund_record.refund
            if refund == 0:
                continue

            refund_time = refund_record.apply_time
            salesout_records = salesOutDetails.objects.filter(otid=trade_no)

            if len(salesout_records) == 0:
                print("未找到关联订单", refund_record)
            
            overall_amount = 0
            for i in salesout_records:
                overall_amount += i.deal_total_price
            if overall_amount == 0:
                continue

            for i in salesout_records:
                if i.deal_total_price == 0:
                    continue
                f = FinanceSalesAndInvoice(
                    date=refund_time,
                    shop_name=i.shop_name,
                    goods_no=i.spec_no,
                    refund_amount=i.deal_total_price/overall_amount*refund
                )
                f.save()
    
    def extend_pdd_refund(self, start_date, end_date):
        end_date += " 23:59:59" 
        refund_records = PddRefund.objects.filter(apply_time__range=(start_date, end_date))
        for refund_record in refund_records:
            trade_no = refund_record.trade_no
            refund = refund_record.refund
            if refund == 0:
                continue

            refund_time = refund_record.apply_time
            salesout_records = salesOutDetails.objects.filter(otid=trade_no)

            if len(salesout_records) == 0:
                print("未找到关联订单", refund_record)
            
            overall_amount = 0
            for i in salesout_records:
                overall_amount += i.deal_total_price
            if overall_amount == 0:
                continue

            for i in salesout_records:
                if i.deal_total_price == 0:
                    continue
                f = FinanceSalesAndInvoice(
                    date=refund_time,
                    shop_name=i.shop_name,
                    goods_no=i.spec_no,
                    refund_amount=i.deal_total_price/overall_amount*refund
                )
                f.save()
    
    def extend_tmall_refund(self, start_date, end_date):
        end_date += " 23:59:59" 
        refund_records = TmallRefund.objects.filter(refund_apply_time__range=(start_date, end_date))
        for refund_record in refund_records:
            trade_no = refund_record.trade_no
            refund = refund_record.refund
            if refund == 0:
                continue

            refund_time = refund_record.refund_apply_time
            salesout_records = salesOutDetails.objects.filter(otid=trade_no)
            
            if len(salesout_records) == 0:
                print("未找到关联订单", refund_record)
            
            overall_amount = 0
            for i in salesout_records:
                overall_amount += i.deal_total_price
            if overall_amount == 0:
                continue

            for i in salesout_records:
                if i.deal_total_price == 0:
                    continue
                f = FinanceSalesAndInvoice(
                    date=refund_time,
                    shop_name=i.shop_name,
                    goods_no=i.spec_no,
                    refund_amount=i.deal_total_price/overall_amount*refund
                )
                f.save()
    
    def refund_summary(self, start_date, end_date):
        details = FinanceSalesAndInvoice.objects.values(
            "shop_name",
            "goods_no",
        ).filter(
            date__gte=start_date, 
            date__lte=end_date,
            refund_amount__isnull=False,
        ).annotate(
            details_sum_amount=Sum("refund_amount"),
        )
        for i in details:
            print(i)
            shop_name = i['shop_name']
            goods_no = i['goods_no']
            refund_amount = i['details_sum_amount']
            f = FinanceSalesAndInvoice(
                start_date=start_date,
                end_date=end_date,
                shop_name=shop_name,
                goods_no=goods_no,
                refund_amount=refund_amount,
            )
            f.save()

    def overall_summary(self, start_date, end_date):
        details = FinanceSalesAndInvoice.objects.values(
            "shop_name",
            "goods_no",
        ).filter(
            start_date=start_date,
            end_date=end_date,
        ).annotate(
            sales_num__sum=Sum("sales_num"),
            invoice_num__sum=Sum("invoice_num"),
            uninvoice_num__sum=Sum("sales_num", default=0)-Sum("invoice_num", default=0),
            sales_amount__sum=Sum("sales_amount", default=0),
            post_amount__sum=Sum("post_amount", default=0),
            refund_amount__sum=Sum("refund_amount", default=0),
            invoice_amount__sum=Sum("invoice_amount", default=0),
            uninvoice_amount__sum=Sum("sales_amount", default=0)+Sum("post_amount", default=0)-Sum("refund_amount", default=0)-Sum("invoice_amount", default=0),
        )
        url = os.getenv("APITABLE_BASE_URL") + "/fusion/v1/datasheets/dstG0kXVLwywl4U6Bq/records"
        token = os.getenv("APITABLE_TOKEN")
        records = []
        for i in details:
            print(i)
            material_no_and_goods_name = self.goods_no_to_material_no(i["goods_no"])
            r = {
                "时间": end_date,
                "店铺名称": i["shop_name"],
                "商家编码": i["goods_no"],
                "料号": material_no_and_goods_name[0],
                "实际销售量": i["sales_num__sum"],
                "已开票数量": i["invoice_num__sum"],
                "未开票数量": i["uninvoice_num__sum"],
                "实际销售额": float(i["sales_amount__sum"]),
                "邮费": float(i["post_amount__sum"]),
                "退款金额": float(i["refund_amount__sum"]),
                "已开票金额": float(i["invoice_amount__sum"]),
                "未开票金额": float(i["uninvoice_amount__sum"]),
            }
            records.append({ "fields": r })

        #     f = FinanceSalesAndInvoice(
        #         start_date=start_date,
        #         end_date=end_date,
        #         shop_name=i["shop_name"],
        #         goods_no=i["goods_no"],
        #         material_no=material_no_and_goods_name[0],
        #         goods_name=material_no_and_goods_name[1],
        #         sales_num=i["sales_num__sum"],
        #         invoice_num=i["invoice_num__sum"] or 0,
        #         sales_amount=i["sales_amount__sum"],
        #         post_amount=i["post_amount__sum"],
        #         refund_amount=i["refund_amount__sum"] or 0,
        #         invoice_amount=i["invoice_amount__sum"] or 0,
        #     )
        #     f.save()
        print(len(records))
        for i in range(int(len(records)/30)+1):
            s = 30 * i
            e = 30 * (i + 1)
            if i == int(len(records)/30):
                e = len(records)
            res = requests.post(
                url=url,
                json={"records": records[s:e]},
                headers={"Authorization": f"Bearer {token}"},
            )
            res.raise_for_status()
            res = res.content.decode()
            print(res)
        
        summary = details.aggregate(
            total_sales_num=Sum("sales_num__sum"),
            total_invoice_num=Sum("invoice_num__sum"),
            total_uninvoice_num=Sum("uninvoice_num__sum"),
            total_sales_amount=Sum("sales_amount__sum"),
            total_post_amount=Sum("post_amount__sum"),
            total_refund_amount=Sum("refund_amount__sum"),
            total_invoice_amount=Sum("invoice_amount__sum"),
            total_uninvoice_amount=Sum("uninvoice_amount__sum"),
        )
        print(summary)
