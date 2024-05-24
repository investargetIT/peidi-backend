from datetime import datetime

from django.contrib import admin
from django.utils.html import format_html
from rangefilter.filters import DateTimeRangeFilterBuilder

from .models import orders, salesOutDetails, historySalesOutDetails, OrderDetail, WMSShipData, StockDetail, ExchangeManagement, ShopTarget

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

@admin.register(OrderDetail)
class OrderDetailAdmin(admin.ModelAdmin):
    list_display = [
        "trade_no",
        "shop_name",
        "trade_from",
        "warehouse",
        "tid",
        "oid",
        "process_status",
        "order_type",
        "delivery_term",
        "refund_status",
        "refund_status_of_details",
        "trade_time",
        "pay_time",
        "deliver_time",
        "buyer_nick",
        "receiver_name",
        "receiver_area",
        "receiver_address",
        "receiver_mobile",
        "receiver_telno",
        "receiver_zip",
        "logistics_name",
        "logistics_no",
        "buyer_message",
        "service_remark",
        "print_remark",
        "remark",
        "biaoqi",
        "post_amount",
        "other_amount",
        "order_discount",
        "receivable",
        "cod_amount",
        "invoice_type",
        "payer_name",
        "invoice_content",
        "flag_name",
        "spec_no",
        "goods_no",
        "goods_name",
        "spec_name",
        "goods_type",
        "num",
        "ori_price",
        "discount",
        "deal_price",
        "share_price",
        "share_post_amount",
        "discount_rate",
        "share_total_price",
        "commission",
        "source_suite_name",
        "source_suite_no",
        "source_suite_num",
        "gift_method",
        "platform_goods_name",
        "platform_spec_name",
        "order_tag",
        "distributor",
        "distributor_no",
        "paid",
        "pay_account",
        "deadline_deliver_time",
        "buyer_no",
        "distribution_oid",   
    ]

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

@admin.register(StockDetail)
class StockDetailAdmin(admin.ModelAdmin):
    
    def image_tag_1(self, obj):
        return format_html('<img src="{}" style="width:70px;"/>'.format(obj.img_url))
    image_tag_1.short_description = '图片链接'

    def image_tag_2(self, obj):
        return format_html('<img src="{}" style="width:70px;"/>'.format(obj.img))
    image_tag_2.short_description = '图片'

    list_display = [
        "spec_no",
        "barcode",
        "goods_no",
        "goods_name",
        "goods_short_name",
        "goods_tag",
        "spec_name",
        "spec_id",
        "brand_name",
        "qa_num",
        "todeliver_order_num",
        "retail_price",
        "wholesale_price",
        "market_price",
        "member_price",
        "lowest_price",
        "goods_type",
        "stock",
        "weight",
        "total_weight",
        "is_defective",
        "unit_name",
        "aux_unit_name",
        "aux_remark",
        "deliverable_stock",
        "usable_stock",
        "min_alert_stock",
        "max_alert_stock",
        "unpaid_num",
        "preorder_num",
        "toreview_num",
        "todeliver_num",
        "lock_num",
        "topurchase_num",
        "purchase_ontheway_num",
        "purchase_arrival_num",
        "totransfer_num",
        "totransout_num",
        "toinstock_num",
        "tooutstock_num",
        "transfer_ontheway_num",
        "purchase_return_num",
        "sale_return_ontheway_num",
        "produce_tooutstock_num",
        "produce_toinstock_num",
        "toqa_num",
        "outside_stock_num",
        "stock_diff",
        "sync_time",
        "remark",
        "goods_remark",
        "specgoods_remark",
        "onsale_time",
        "last_inventory_time",
        "actual_stock_num",
        "actual_todelivery_stock_num",
        "image_tag_1",
        "image_tag_2",
        "major_supplier",
        "custom_stock_one",
        "custom_stock_two",
        "custom_stock_three",
        "custom_stock_four",
        "custom_stock_five",
    ]

@admin.register(WMSShipData)
class WMSShipDataAdmin(admin.ModelAdmin):
    list_display = [
        "order_num",
        "to_print",
        "printed",
        "to_ship",
        "shipped",
        "created_at",
    ]

@admin.register(ExchangeManagement)
class ExchangeManagementAdmin(admin.ModelAdmin):
    list_display = [
        "exchange_no",
        "shop_name",
        "type",
        "status",
        "stock_status",
        "tid",
        "trade_no",
        "original_exchange_no",
        "buyer_nick",
        "receiver_name",
        "receiver_telno",
        "refund_amount",
        "platform_refund",
        "offline_refund",
        "collection_amount",
        "refund",
        "logistics_name",
        "logistics_no",
        "warehouse",
        "data_source",
        "exchange_remark",
        "refuse_reason",
        "mark",
        "creater",
        "remark",
        "created_time",
        "updated_time",
        "exchange_info",
        "distributor_exchange_no",
        "refund_num",
        "distributor_name",
        "distributor_no",
        "refund_reason",
        "wms_no",
        "error_msg",
        "distributor_tid",
    ]

@admin.register(ShopTarget)
class ShopTargetAdmin(admin.ModelAdmin):
    list_display = [
        "shop_name",
        "wdt_name",
        "channel",
        "platform",
        "principal",
        "year",
        "target",
        "product_score",
        "logistic_score",
        "service_score",
        "dsr_date",
    ]
    list_filter = ["year"]
