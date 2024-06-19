from datetime import datetime

from django.contrib import admin
from django.utils.html import format_html

from rangefilter.filters import DateTimeRangeFilterBuilder
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from import_export.fields import Field

from .models import orders, salesOutDetails, historySalesOutDetails, OrderDetail, WMSShipData, StockDetail, ExchangeManagement, ShopTarget

class StockDetailResource(resources.ModelResource):
    spec_no = Field(attribute='spec_no', column_name='商家编码')
    goods_no = Field(attribute='goods_no', column_name='货品编号')
    goods_name = Field(attribute='goods_name', column_name='货品名称')
    goods_short_name = Field(attribute='goods_short_name', column_name='货品简称')
    goods_tag = Field(attribute='goods_tag', column_name='货品标签')
    goods_type = Field(attribute='goods_type', column_name='分类')
    spec_id = Field(attribute='spec_id', column_name='规格码')
    spec_name = Field(attribute='spec_name', column_name='规格名称')
    barcode = Field(attribute='barcode', column_name='条码')
    weight = Field(attribute='weight', column_name='单品重量')
    brand_name = Field(attribute='brand_name', column_name='品牌')
    is_defective = Field(attribute='is_defective', column_name='残次品')
    stock = Field(attribute='stock', column_name='库存')
    unit_name = Field(attribute='unit_name', column_name='单位')
    aux_unit_name = Field(attribute='aux_unit_name', column_name='辅助单位')
    aux_remark = Field(attribute='aux_remark', column_name='辅助说明')
    deliverable_stock = Field(attribute='deliverable_stock', column_name='可发库存')
    min_alert_stock = Field(attribute='min_alert_stock', column_name='警戒库存下限')
    max_alert_stock = Field(attribute='max_alert_stock', column_name='警戒库存上限')
    unpaid_num = Field(attribute='unpaid_num', column_name='未付款量')
    qa_num = Field(attribute='qa_num', column_name='已质检库存')
    todeliver_order_num = Field(attribute='todeliver_order_num', column_name='未发货订单总数')
    preorder_num = Field(attribute='preorder_num', column_name='预订单量')
    toreview_num = Field(attribute='toreview_num', column_name='待审核量')
    todeliver_num = Field(attribute='todeliver_num', column_name='待发货量')
    lock_num = Field(attribute='lock_num', column_name='锁定量')
    topurchase_num = Field(attribute='topurchase_num', column_name='待采购量')
    purchase_ontheway_num = Field(attribute='purchase_ontheway_num', column_name='采购在途')
    purchase_arrival_num = Field(attribute='purchase_arrival_num', column_name='采购到货量')
    totransfer_num = Field(attribute='totransfer_num', column_name='待调拨量')
    totransout_num = Field(attribute='totransout_num', column_name='待调出量')
    transfer_ontheway_num = Field(attribute='transfer_ontheway_num', column_name='调拨在途')
    toinstock_num = Field(attribute='toinstock_num', column_name='其他待入库量')
    tooutstock_num = Field(attribute='tooutstock_num', column_name='其他待出库量')
    toqa_num = Field(attribute='toqa_num', column_name='待质检量')
    purchase_return_num = Field(attribute='purchase_return_num', column_name='采购退货')
    sale_return_ontheway_num = Field(attribute='sale_return_ontheway_num', column_name='退货在途量')
    produce_tooutstock_num = Field(attribute='produce_tooutstock_num', column_name='生产待出库量')
    produce_toinstock_num = Field(attribute='produce_toinstock_num', column_name='生产待入库量')
    material_no = Field(attribute='material_no', column_name='U9料号')
    tax_rate = Field(attribute='tax_rate', column_name='税率')
    remark = Field(attribute='remark', column_name='备注')
    goods_remark = Field(attribute='goods_remark', column_name='货品备注')
    specgoods_remark = Field(attribute='specgoods_remark', column_name='单品备注')
    spec_created = Field(attribute='spec_created', column_name='单品创建时间')
    last_inventory_time = Field(attribute='last_inventory_time', column_name='最后盘点时间')
    usable_stock = Field(attribute='usable_stock', column_name='可用库存')
    img_url = Field(attribute='img_url', column_name='图片链接')
    img = Field(attribute='img', column_name='图片')
    major_supplier = Field(attribute='major_supplier', column_name='主供应商')
    custom_stock_one = Field(attribute='custom_stock_one', column_name='自定义库存1')
    custom_stock_two = Field(attribute='custom_stock_two', column_name='自定义库存2')
    custom_stock_three = Field(attribute='custom_stock_three', column_name='自定义库存3')
    custom_stock_four = Field(attribute='custom_stock_four', column_name='自定义库存4')
    custom_stock_five = Field(attribute='custom_stock_five', column_name='自定义库存5')
    actual_stock_num = Field(attribute='actual_stock_num', column_name='实际库存')
    actual_todelivery_stock_num = Field(attribute='actual_todelivery_stock_num', column_name='实际可发库存')

    def before_import_row(self, row, **kwargs):
        float_fields = ["单品创建时间", "最后盘点时间", "税率", "可用库存"]
        for float_field in float_fields:
            if not row[float_field]:
                row[float_field] = None

    def before_import(self, dataset, **kwargs):
        StockDetail.objects.all().delete()

    class Meta:
        model = StockDetail

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
            "trade_time",
            DateTimeRangeFilterBuilder(
                title="下单时间",
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
class StockDetailAdmin(ImportExportModelAdmin):
    
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
        "goods_type",
        "stock",
        "weight",
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
        "remark",
        "goods_remark",
        "specgoods_remark",
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
    resource_classes = [StockDetailResource]

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
        "need_summary",
    ]
    list_filter = ["year"]
