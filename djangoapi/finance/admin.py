from django.contrib import admin
from .models import TmallRefund, PddRefund, JdRefund, DouyinRefund

@admin.register(TmallRefund)
class TmallRefundAdmin(admin.ModelAdmin): 
    list_display = [
        "trade_no",
        "refund_no",
        "alipay_transaction_no",
        "pay_time",
        "goods_no",
        "refund_close_time",
        "paid",
        "goods_name",
        "refund",
        "refund_source",
        "goods_return",
        "refund_apply_time",
        "refund_deadline",
        "refund_status",
        "goods_status",
        "return_logistics_info",
        "deliver_logistics_info",
        "service_intervene",
        "seller_name",
        "seller_name_new",
        "seller_return_address",
        "seller_zip",
        "seller_telno",
        "seller_mobile",
        "logistics_no",
        "logistics_name",
        "refund_reason",
        "refund_explanation",
    ]

@admin.register(PddRefund)
class PddRefundAdmin(admin.ModelAdmin):
    list_display = [
        "shop_name",
        "trade_no",
        "goods_id",
        "goods_name",
        "refund_reason",
        "applicant",
        "apply_time",
        "refund",
        "refund_status"
    ]

@admin.register(JdRefund)
class JdRefundAdmin(admin.ModelAdmin):
    list_display = [
        "shop_name",
        "apply_time",
        "refund_no",
        "trade_no",
        "service_no",
        "refund",
        "refund_reason",
        "refund_status",
        "applicant",
    ]

@admin.register(DouyinRefund)
class DouyinRefundAdmin(admin.ModelAdmin):
    list_display = [
        "shop_name",
        "pay_transaction_no",
        "trade_no",
        "goods_name",
        "goods_id",
        "refund_reason",
        "refund",
        "applicant",
        "apply_time",
        "refund_time",
        "refund_status",
        "refund_remark",
    ]
