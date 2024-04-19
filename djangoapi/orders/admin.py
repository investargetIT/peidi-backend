from datetime import datetime

from django.contrib import admin
from rangefilter.filters import DateTimeRangeFilterBuilder

from .models import orders, salesOutDetails, historySalesOutDetails

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

@admin.register(salesOutDetails)
class SalesOutDetailsAdmin(admin.ModelAdmin):
    list_display = [
        "trade_no",
        "tid",
        "oid",
        "otid",
        "order_type",
        "trade_from",
        "pay_account",
        "stockout_no",
        "warehouse",
        "shop_name",
        "status_type",
        "stockout_status",
        "spec_no",
        "goods_no",
        "goods_name",
        "goods_short_name",
        "brand_name",
        "goods_type",
        "spec_id",
        "spec_name",
        "barcode",
        "num",
        "unit_name",
        "aux_num",
        "aux_unit_name",
        "ori_price",
        "ori_total_amount",
        "order_discount",
        "post_amount",
        "share_post_amount",
        "deal_price",
        "deal_total_price",
        "goods_discount",
        "cod_amount",
        "receivable",
        "ori_receivable",
        "buyer_nick",
        "receiver_name",
        "receiver_area",
        "receiver_address",
        "receiver_mobile",
        "receiver_telno",
        "logistics_name",
        "invoice_type",
        "flag_name",
        "trade_time",
        "pay_time",
        "created",
        "deliver_time",
        "gift_method",
        "buyer_message",
        "service_remark",
        "remark",
        "print_remark",
        "source_suite_no",
        "source_suite_name",
        "source_suite_num",
        "stockout_tag",
        "order_tag",
        "specgoods_price",
        "distributor",
        "distributor_no",
        "paid",
        "distribution_oid"
    ]
    search_fields = ["trade_no", "tid", "oid", "buyer_nick"]
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

@admin.register(historySalesOutDetails)
class HistorySalesOutDetailsAdmin(admin.ModelAdmin):
    list_display = [
        "trade_no",
        "tid",
        "oid",
        "otid",
        "order_type",
        "trade_from",
        "pay_account",
        "stockout_no",
        "warehouse",
        "shop_name",
        "status_type",
        "stockout_status",
        "spec_no",
        "goods_no",
        "goods_name",
        "goods_short_name",
        "brand_name",
        "goods_type",
        "spec_id",
        "spec_name",
        "barcode",
        "num",
        "unit_name",
        "aux_num",
        "aux_unit_name",
        "ori_price",
        "ori_total_amount",
        "order_discount",
        "post_amount",
        "share_post_amount",
        "deal_price",
        "deal_total_price",
        "goods_discount",
        "cod_amount",
        "receivable",
        "ori_receivable",
        "buyer_nick",
        "receiver_name",
        "receiver_area",
        "receiver_address",
        "receiver_mobile",
        "receiver_telno",
        "logistics_name",
        "invoice_type",
        "flag_name",
        "trade_time",
        "pay_time",
        "created",
        "deliver_time",
        "gift_method",
        "buyer_message",
        "service_remark",
        "remark",
        "print_remark",
        "source_suite_no",
        "source_suite_name",
        "source_suite_num",
        "stockout_tag",
        "order_tag",
        "specgoods_price",
        "distributor",
        "distributor_no",
        "paid",
        "distribution_oid"
    ]
    search_fields = ["trade_no", "tid", "oid", "buyer_nick"]
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
