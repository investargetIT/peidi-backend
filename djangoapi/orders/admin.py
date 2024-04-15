from datetime import datetime

from django.contrib import admin
from rangefilter.filters import DateTimeRangeFilterBuilder

from .models import orders, salesOutDetails

admin.site.register(salesOutDetails)

@admin.register(orders)
class OrderAdmin(admin.ModelAdmin): 
    list_display = [
        "trade_no",
        "platform",
        "shop_name",
        "warehouse_no",
        "tid",
        "trade_status",
        "guarantee_mode",
        "pay_status",
        "delivery_term",
        "pay_method",
        "pay_account",
        "refund_status",
        "process_status",
        "bad_reason",
        "trade_time",
        "pay_time",
        "end_time",
        "buyer_nick",
        "receiver_name",
        "receiver_area",
        "receiver_ring",
        "receiver_address",
        "receiver_mobile",
        "receiver_telno",
        "receiver_zip",
        "to_deliver_time",
        "buyer_message",
        "remark",
        "biaoqi",
        "goods_amount",
        "post_amount",
        "other_amount",
        "discount",
        "platform_cost",
        "received",
        "receivable",
        "cash_on_delivery_amount",
        "refund_amount",
        "logistics_type",
        "invoice_type",
        "payer_name",
        "invoice_content",
        "is_auto_wms",
        "is_ware_trade",
        "trade_from",
        "logistics_no",
        "pay_id",
        "paid",
        "consumer_amount",
        "platform_amount",
        "currency",
        "id_no",
        "modified",
        "created",
    ]
    search_fields = ["tid"]
    list_filter = (
        (
            "pay_time",
            DateTimeRangeFilterBuilder(
                title="支付时间",
                default_start=datetime(2022, 1, 1),
                default_end=datetime(2022, 12, 31, 23, 59, 59),
            ),
        ),
    )
