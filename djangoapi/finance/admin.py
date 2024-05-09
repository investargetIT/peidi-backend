from django.contrib import admin
from .models import TmallRefund

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
