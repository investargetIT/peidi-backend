import requests, os, time
from django.core.management.base import BaseCommand
from django.db.models import Sum

from goods.models import SpecGoods, SuiteGoodsRec
from finance.models import Invoice, FinanceSalesAndInvoice, PDMaterialNOList, GoodsSalesSummary, DouyinRefund, PddRefund, JdRefund, TmallRefund, InvoiceManual
from orders.models import salesOutDetails, historySalesOutDetails, ShopTarget

base_url = os.getenv("APITABLE_BASE_URL")
token = os.getenv("APITABLE_TOKEN")

class Command(BaseCommand):

    def handle(self, *args, **options):
        print("Hello")

        # print(self.goods_no_to_material_no("6971758277324"))
        
        # self.invoice_created_by_ali("2024-05-26", "2024-06-25")

        # self.invoice_created_manually("2024-05-26", "2024-06-25")

        # self.invoice_summary('2024-05-26', '2024-06-25')

        # self.extend_douyin_refund("2024-05-26", "2024-06-25")

        # self.extend_jd_refund("2024-05-26", "2024-06-25")

        # self.extend_pdd_refund("2024-05-26", "2024-06-25")

        # self.extend_tmall_refund("2024-05-26", "2024-06-25")

        # self.refund_summary("2024-05-26", "2024-06-25")

        # self.sales_summary("2024-05-26", "2024-06-25")

        # self.overall_summary("2024-05-26", "2024-06-25")
    
    def goods_model_to_spec_goods(self, finance_sales_and_invoice):
        records = []
        goods_model = finance_sales_and_invoice.goods_no
        try:
            spec_goods = SpecGoods.objects.get(spec_no=goods_model)
            # print(spec_goods.spec_no, '是单品', spec_goods.goods_name)
            finance_sales_and_invoice.goods_name = spec_goods.goods_name
            finance_sales_and_invoice.save()
            records.append(finance_sales_and_invoice)
            # print()
        except SpecGoods.DoesNotExist:
            suite_goods = SuiteGoodsRec.objects.filter(suite_no=goods_model)
            if len(suite_goods) == 0:
                print('根据商家编码未找到组合装，尝试根据名称查找', goods_model)
                suite_goods = SuiteGoodsRec.objects.filter(suite_name=goods_model)
                print('结果找到了', len(suite_goods))
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
                    records.append(f)
                # print()
            else:
                print('该商品不存在', goods_model)
                # 作为单品处理
                finance_sales_and_invoice.save()
                records.append(finance_sales_and_invoice)
        return records

    def merge_original_invoice(self, start_date, end_date):
        result = []
        end_date += " 23:59:59"
        distinct_trade_no = Invoice.objects.filter(
                invoice_time__range=(start_date, end_date),
                trade_no__isnull = False,
            ).values("trade_no").distinct()
        
        for i in distinct_trade_no:
            # 以订单id、商品型号、开票日期和店铺名称为唯一数据，合并发票总金额，即对冲掉优惠返现等负的发票总金额
            invoices = Invoice.objects.values(
                    "trade_no",
                    "goods_model",
                    "invoice_time",
                    "shop_name",
                ).filter(
                    trade_no=i['trade_no'],
                    invoice_time__range=(start_date, end_date),
                ).annotate(
                    Sum("goods_total_amount"),
                    Sum("goods_num"),
                )
            
            for invoice in invoices:
                date = invoice['invoice_time']
                shop_name = invoice['shop_name']
                goods_no = invoice['goods_model']
                invoice_num = invoice['goods_num__sum']
                invoice_amount = invoice['goods_total_amount__sum']

                f = FinanceSalesAndInvoice(
                    date=date,
                    shop_name=shop_name,
                    goods_no=goods_no,
                    invoice_num=invoice_num,
                    invoice_amount=invoice_amount
                )
                result.append(f)
                 
        return result

    def invoice_created_by_ali(self, start_date, end_date):
        url = os.getenv("APITABLE_BASE_URL") + "/fusion/v1/datasheets/dstpdLsvjo1Nr6iti6/records"
        token = os.getenv("APITABLE_TOKEN")
        merged_invoice = self.merge_original_invoice(start_date, end_date)
        invoices, records = [], []
        for invoice in merged_invoice:
            f = self.goods_model_to_spec_goods(invoice)
            invoices += f
        for f in invoices:
            material_no_and_goods_name = self.goods_no_to_material_no(f.goods_no)
            r = {
                    "时间": f.date.strftime("%Y-%m-%d"),
                    "店铺名称": f.shop_name,
                    "商家编码": f.goods_no,
                    "料号": material_no_and_goods_name[0],
                    "数量": int(f.invoice_num) if f.invoice_num is not None else 0,
                    "价税合计": float(f.invoice_amount) if f.invoice_amount is not None else 0,
                }
            records.append({ "fields": r })
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
            time.sleep(1)

    def invoice_created_manually(self, start_date, end_date):
        end_date += " 23:59:59"        
        manual_invoices = InvoiceManual.objects.filter(
            invoice_time__range=(start_date, end_date)
        ).values()
        url = os.getenv("APITABLE_BASE_URL") + "/fusion/v1/datasheets/dst6D5RicsfUPcUunq/records"
        token = os.getenv("APITABLE_TOKEN")
        records = []
        for invoice in manual_invoices:
            date = invoice['invoice_time']
            shop_name = invoice['shop_name']
            goods_no = invoice['goods_model']
            goods_name = invoice["goods_name"]
            invoice_num = invoice['goods_num']
            invoice_amount = invoice['goods_total_amount']
            print(date, shop_name, goods_no, goods_name, invoice_num, invoice_amount)

            f = FinanceSalesAndInvoice(
                date=date,
                shop_name=shop_name,
                goods_no=goods_no,
                goods_name=goods_name,
                invoice_num=invoice_num,
                invoice_amount=invoice_amount
            )
            f.save()
            material_no_and_goods_name = self.goods_no_to_material_no(goods_no)
            r = {
                "日期": date.strftime("%Y-%m-%d"),
                "订货客户": shop_name,
                "货号": goods_no,
                "料号": material_no_and_goods_name[0],
                "数量": int(invoice_num),
                "价税合计": float(invoice_amount),
            }
            records.append({ "fields": r })

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
            time.sleep(1)

    def goods_no_to_material_no(self, goods_no):
        try:
            spec_goods = SpecGoods.objects.get(spec_no=goods_no)
            return (spec_goods.u9_no, spec_goods.goods_name, spec_goods.tax_rate)
        except:
            return (None, None, None)

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

        records = []
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

            price = None
            if invoice_num != 0:
                price = abs(float("%.2f" % (invoice_amount / invoice_num)))

            material_no_and_goods_name = self.goods_no_to_material_no(goods_no)
            tax_rate = None
            untax_amount = None
            if material_no_and_goods_name[2]:
                tax_rate = float("%.2f" % material_no_and_goods_name[2])
                untax_amount = invoice_amount / (1 + material_no_and_goods_name[2] / 100)
                untax_amount = float("%.2f" % untax_amount)

            records.append({
                "fields": {
                    "时间": end_date[:7],
                    "订货客户": shop_name,
                    "货号": goods_no,
                    "料号": material_no_and_goods_name[0],
                    "品名": material_no_and_goods_name[1],
                    "数量": invoice_num,
                    "单价": price,
                    "价税合计": float("%.2f" % invoice_amount),
                    "税率": tax_rate,
                    "未含税金额": untax_amount,
                },
            })

        print(len(records))
        url = base_url + "/fusion/v1/datasheets/dstayEpslFPDrHdEcC/records"
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
            time.sleep(1)

        summary = details.aggregate(
            total_num=Sum("details_sum_num"),
            total_price=Sum("details_sum_amount") / Sum("details_sum_num"),
            total_amount=Sum("details_sum_amount"),
        )
        print(summary)

    def sales_summary(self, start_date, end_date):
        # 从店铺目标表中过滤出需要汇总的店铺
        wdt_shop_name_list = ShopTarget.objects.filter(
                need_summary = True,
            ).values_list("wdt_name", flat=True)

        details = GoodsSalesSummary.objects.values(
            "spec_no",
            "shop_name",
        ).filter(
            start_date__gte=start_date,
            end_date__lte=end_date,
            shop_name__in=list(wdt_shop_name_list)
        ).annotate(
            details_ship_refund_num=Sum("ship_refund_num"),
            details_sales_num=Sum("sales_num"),
            details_sum_num=Sum("sales_num",default=0)+Sum("ship_refund_num",default=0),
            details_ship_refund_amount=Sum("ship_refund_amount"),
            details_sum_post=Sum("post_amount"),
            details_actual_sales_amount=Sum("actual_sales_amount"),
            details_sum_amount=Sum("actual_sales_amount",default=0)+Sum("ship_refund_amount",default=0),
            details_total_amount=Sum("actual_sales_amount",default=0)+Sum("post_amount",default=0)+Sum("ship_refund_amount",default=0),
        )

        records = []
        for i in details:
            print(i)
            shop_name = i['shop_name']
            goods_no = i['spec_no']
            sales_num = i['details_sum_num']
            sales_amount = i['details_sum_amount']
            post_amount = i['details_sum_post']

            r = {
                "时间": end_date[:7],
                "商家编码": i["shop_name"],
                "商家编码": goods_no,
                "店铺": shop_name,
                "系统发货但平台退款量": float(i["details_ship_refund_num"]),
                "实际销售量": float(i["details_sales_num"]),
                "系统发货但平台退款金额": float(i["details_ship_refund_amount"]),
                "邮费": float(i["details_sum_post"]),
                "实际销售额": float(i["details_actual_sales_amount"]),
                "价税合计": float(i["details_total_amount"]),
            }
            records.append({ "fields": r })

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

        url = os.getenv("APITABLE_BASE_URL") + "/fusion/v1/datasheets/dstsvNdHbHR27VJ0WK/records"
        token = os.getenv("APITABLE_TOKEN")
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
            time.sleep(1)
        
        summary = details.aggregate(
            total_num=Sum("details_sum_num"),
            total_post=Sum("details_sum_post"),
            total_amount=Sum("details_sum_amount"),
        )
        print(summary)
    
    def refund_basic(self, url, refund_records):
        records = []
        for refund_record in refund_records:
            trade_no = refund_record.trade_no
            refund = refund_record.refund
            if refund == 0:
                continue
            refund_time = refund_record.apply_time
            salesout_records = salesOutDetails.objects.values(
                    "shop_name",
                    "spec_no",
                ).filter(
                    otid=trade_no,
                    deliver_time__isnull=False,
                    deal_total_price__gt=0,
                ).annotate(Sum("deal_total_price"))
            
            # 销售出库明细里没找到的话，在历史销售出库明细里找
            if len(salesout_records) == 0:
                salesout_records = historySalesOutDetails.objects.values(
                    "shop_name",
                    "spec_no",
                ).filter(
                    otid=trade_no,
                    deliver_time__isnull=False,
                    deal_total_price__gt=0,
                ).annotate(Sum("deal_total_price"))
            
            # 销售出库明细和历史销售出库明细都没找到的情况
            if len(salesout_records) == 0:    
                print('未找到销售出库明细', refund_record.trade_no)
                continue
            
            print(len(salesout_records))

            # 计算这笔订单（可能包含多个单品）的货品成交总价
            overall_amount = 0
            for i in salesout_records:
                overall_amount += i["deal_total_price__sum"]
            
            if overall_amount == 0:
                continue
            print(overall_amount)
            for i in salesout_records:
                print(refund_time, i["shop_name"], trade_no, i["spec_no"], i["deal_total_price__sum"])
                r = {
                    "时间": refund_time.strftime("%Y-%m-%d"),
                    "订单编号": trade_no,
                    "商家编码": i["spec_no"],
                    "店铺名称": i["shop_name"],
                    "买家退款金额": float(i["deal_total_price__sum"]/overall_amount*refund),
                }
                records.append({ "fields": r })

                f = FinanceSalesAndInvoice(
                    date=refund_time,
                    shop_name=i["shop_name"],
                    goods_no=i["spec_no"],
                    refund_amount=i["deal_total_price__sum"]/overall_amount*refund
                )
                f.save()

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
            time.sleep(1)

    def extend_douyin_refund(self, start_date, end_date):
        end_date += " 23:59:59" 
        refund_records = DouyinRefund.objects.filter(refund_time__range=(start_date, end_date))
        url = os.getenv("APITABLE_BASE_URL") + "/fusion/v1/datasheets/dstDJlVoKmcEGgbk8n/records"
        self.refund_basic(url, refund_records)

    def extend_jd_refund(self, start_date, end_date):
        end_date += " 23:59:59" 
        refund_records = JdRefund.objects.filter(apply_time__range=(start_date, end_date))
        url = os.getenv("APITABLE_BASE_URL") + "/fusion/v1/datasheets/dstMTmJLFNzjg3tBtn/records"
        self.refund_basic(url, refund_records)

    def extend_pdd_refund(self, start_date, end_date):
        end_date += " 23:59:59" 
        refund_records = PddRefund.objects.filter(
            apply_time__range=(start_date, end_date),
            refund_status="打款成功",
        )
        url = os.getenv("APITABLE_BASE_URL") + "/fusion/v1/datasheets/dstc0QSDi41j7GMkYa/records"
        self.refund_basic(url, refund_records)

    def extend_tmall_refund(self, start_date, end_date):
        end_date += " 23:59:59" 
        refund_records = TmallRefund.objects.filter(
            apply_time__range=(start_date, end_date),
            refund_type="部分退款",
        ).exclude(goods_name__contains="购物金")
        url = os.getenv("APITABLE_BASE_URL") + "/fusion/v1/datasheets/dst79PPdUTvu6FUCL8/records"
        self.refund_basic(url, refund_records)

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
            sales_num__sum=Sum("sales_num", default=0),
            invoice_num__sum=Sum("invoice_num", default=0),
            uninvoice_num__sum=Sum("sales_num", default=0)-Sum("invoice_num", default=0),
            sales_amount__sum=Sum("sales_amount", default=0),
            post_amount__sum=Sum("post_amount", default=0),
            refund_amount__sum=Sum("refund_amount", default=0),
            invoice_amount__sum=Sum("invoice_amount", default=0),
            uninvoice_amount__sum=Sum("sales_amount", default=0)+Sum("post_amount", default=0)-Sum("refund_amount", default=0)-Sum("invoice_amount", default=0),
        )
        url = os.getenv("APITABLE_BASE_URL") + "/fusion/v1/datasheets/dstG0kXVLwywl4U6Bq/records"
        token = os.getenv("APITABLE_TOKEN")
        records, uninvoiced_records = [], []
        for i in details:
            print(i)
            material_no_and_goods_name = self.goods_no_to_material_no(i["goods_no"])
            r = {
                "时间": end_date[:7],
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

            price = None
            if i["uninvoice_num__sum"] != 0:
                price = abs(float("%.2f" % (i["uninvoice_amount__sum"] / i["uninvoice_num__sum"])))

            tax_rate = None
            untax_amount = None
            if material_no_and_goods_name[2]:
                tax_rate = float("%.2f" % material_no_and_goods_name[2])
                untax_amount = i["uninvoice_amount__sum"] / (1 + material_no_and_goods_name[2] / 100)
                untax_amount = float("%.2f" % untax_amount)

            uninvoiced_records.append({
                "fields": {
                    "时间": end_date[:7],
                    "订货客户": i["shop_name"],
                    "货号": i["goods_no"],
                    "料号": material_no_and_goods_name[0],
                    "品名": material_no_and_goods_name[1],
                    "数量": i["uninvoice_num__sum"],
                    "单价": price,
                    "价税合计": float("%.2f" % i["uninvoice_amount__sum"]),
                    "税率": tax_rate,
                    "未含税金额": untax_amount,
                }
            })
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
            time.sleep(1)
        
        print(len(uninvoiced_records))
        url = base_url + "/fusion/v1/datasheets/dstBxinVoohgN131w8/records"
        for i in range(int(len(uninvoiced_records)/30)+1):
            s = 30 * i
            e = 30 * (i + 1)
            if i == int(len(uninvoiced_records)/30):
                e = len(uninvoiced_records)
            res = requests.post(
                url=url,
                json={"records": uninvoiced_records[s:e]},
                headers={"Authorization": f"Bearer {token}"},
            )
            res.raise_for_status()
            time.sleep(1)
        
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
