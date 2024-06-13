from django.contrib import admin
from .models import TmallRefund, PddRefund, JdRefund, DouyinRefund, Invoice, GoodsSalesSummary, FinanceSalesAndInvoice, PDMaterialNOList, InvoiceManual
from rangefilter.filters import DateRangeFilterBuilder
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from import_export.fields import Field

class InvoiceManualResource(resources.ModelResource):
    invoice_time = Field(attribute='invoice_time', column_name='日期')
    shop_name = Field(attribute='shop_name', column_name='订货客户')
    goods_model = Field(attribute='goods_model', column_name='货号')
    goods_name = Field(attribute='goods_name', column_name='品名')
    goods_num = Field(attribute='goods_num', column_name='数量')
    goods_total_amount = Field(attribute='goods_total_amount', column_name='价税合计')
    
    def before_import_row(self, row, **kwargs):
        if row['订货客户'] == '抖音-佩蒂宠物专营店':
            row['订货客户'] = '杭州-抖音-佩蒂宠物专营店'
        elif row['订货客户'] == '天猫-佩蒂旗舰店':
            row['订货客户'] = '杭州-天猫-佩蒂旗舰店'
        elif row['订货客户'] == '天猫-好适嘉旗舰店':
            row['订货客户'] = '杭州-天猫-好适嘉旗舰店'
        elif row['订货客户'] == '天猫-smartbones旗舰店':
            row['订货客户'] = '杭州-天猫-smartbones旗舰店'
        elif row['订货客户'] == '天猫-千百仓宠物用品专营店':
            row['订货客户'] = '上海-天猫-千百仓宠物用品专营店'
        elif row['订货客户'] == '拼多多-喵汪食堂宠物用品店':
            row['订货客户'] = '上海-拼多多-喵汪食堂宠物用品店'
        elif row['订货客户'] == '抖音-哈宠抖音小店':
            row['订货客户'] = '上海-抖音-哈宠抖音小店'
        elif row['订货客户'] == '京东-CPET宠物生活旗舰店':
            row['订货客户'] = '杭州-京东-CPET宠物生活旗舰店'
        elif row['订货客户'] == '京东-禾仕嘉旗舰店':
            row['订货客户'] = '杭州-京东-禾仕嘉旗舰店'
        elif row['订货客户'] == '京东MeatyWay爵宴旗舰店':
            row['订货客户'] = '杭州-京东-爵宴旗舰店'
        elif row['订货客户'] == '京东好适嘉旗舰店':
            row['订货客户'] = '杭州-京东-好适嘉旗舰店'
        elif row['订货客户'] == '拼多多-啊猫阿狗宠物店':
            row['订货客户'] = '上海-拼多多-啊猫阿狗宠物店'
        elif row['订货客户'] == '拼多多-四脚星球宠物店':
            row['订货客户'] = '上海-拼多多-四脚星球宠物店'
        elif row['订货客户'] == '拼多多-爵宴旗舰店':
            row['订货客户'] = '杭州-拼多多-爵宴旗舰店'
        elif row['订货客户'] == '京东-Smartbones旗舰店':
            row['订货客户'] = '杭州-京东-Smartbones旗舰店'
        elif row['订货客户'] == '抖音-HEALTH好适嘉客户':
            row['订货客户'] = '杭州-抖音-HEALTH好适嘉'
        elif row['订货客户'] == '抖音-佩蒂旗舰店':
            row['订货客户'] = '杭州-抖音-佩蒂旗舰店'
        elif row['订货客户'] == '抖音-上海妙旺宠物专营店':
            row['订货客户'] = '上海-抖音-上海妙旺宠物专营店'
        elif row['订货客户'] == '拼多多-猫酱宠物食品官方旗舰店':
            row['订货客户'] = '上海-拼多多-猫酱宠物食品官方旗舰店'
        elif row['订货客户'] == '千百仓宠物用品专营店':
            row['订货客户'] = '上海-天猫-千百仓宠物用品专营店'
        elif row['订货客户'] == '拼多多MeatyWay爵宴旗舰店':
            row['订货客户'] = '杭州-拼多多-爵宴旗舰店'
        elif row['订货客户'] == '拼多多-smartbones旗舰店':
            row['订货客户'] = '杭州-拼多多-smartbones旗舰店'
        elif row['订货客户'] == '拼多多-好适嘉旗舰店':
            row['订货客户'] = '杭州-拼多多-好适嘉旗舰店'
        elif row['订货客户'] == '天猫-哈宠宠物用品专营店':
            row['订货客户'] = '上海-天猫-哈宠宠物用品专营店'         

    class Meta:
        model = InvoiceManual

@admin.register(TmallRefund)
class TmallRefundAdmin(admin.ModelAdmin): 
    list_display = [
        "refund_no",
        "trade_no",
        "alipay_transaction_no",
        "pay_time",
        "goods_no",
        "refund_close_time",
        "paid",
        "goods_name",
        "refund",
        "refund_source",
        "goods_return",
        "apply_time",
        "refund_deadline",
        "refund_status",
        "goods_status",
        "deliver_logistics_info",
        "service_intervene",
        "seller_name",
        "seller_name_new",
        "refund_reason",
        "refund_explanation",
        "refund_type",
    ]
    list_filter = (
        (
            "apply_time",
            DateRangeFilterBuilder(
                title="退款的申请时间",
            ),
        ),
    )
    search_fields = ["trade_no", "goods_no", "goods_name"]

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
    list_filter = (
        (
            "apply_time",
            DateRangeFilterBuilder(
                title="申请时间",
            ),
        ),
    )

@admin.register(JdRefund)
class JdRefundAdmin(admin.ModelAdmin):
    list_display = [
        "shop_name",
        "apply_time",
        "refund_no",
        "trade_no",
        # "service_no",
        "refund",
        "refund_reason",
        "refund_status",
        "applicant",
    ]
    list_filter = (
        (
            "apply_time",
            DateRangeFilterBuilder(
                title="申请时间",
            ),
        ),
    )

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
    list_filter = (
        (
            "refund_time",
            DateRangeFilterBuilder(
                title="打款到账时间",
            ),
        ),
    )

@admin.register(InvoiceManual)
class InvoiceManualAdmin(ImportExportModelAdmin):
    list_display = [
        "invoice_time",
        "shop_name",
        "goods_model",
        "goods_name",
        "goods_num",
        "goods_total_amount",
        "created_at",
    ]
    search_fields = ["goods_model", "goods_name"]
    list_filter = ["shop_name"]
    resource_classes = [InvoiceManualResource]

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = [
        "created_at",
        "trade_no",
        "invoice_time",
        "shop_name",
        # "invoice_category",
        # "invoice_type",
        # "invoice_no",
        # "seller_tax_no",
        # "seller_corp_name",
        # "invoice_title",
        # "payer_tax_no",
        # "invoice_tax",
        # "invoice_amount",
        # "red_to_blue",
        # "remark",
        "goods_name",
        "goods_model",
        "goods_unit",
        "goods_price",
        "goods_num",
        "goods_amount_without_tax",
        "goods_tax",
        "goods_total_amount",
        "tax_rate",
    ]
    search_fields = ["trade_no", "goods_model"]
    list_filter = ["shop_name"]

@admin.register(GoodsSalesSummary)
class GoodsSalesSummaryAdmin(admin.ModelAdmin):
    list_display = [
        "start_date",
        "end_date",
        "spec_no",
        "major_supplier",
        "shop_name",
        "brand_name",
        "goods_type",
        "goods_no",
        "goods_name",
        "spec_name",
        "goods_type",
        "average_price",
        "retail_price",
        "ship_num",
        "return_num",
        "return_count_num",
        "sales_num",
        "ship_amount",
        "sales_amount",
        "sales_amount_unknown_cost",
        "return_amount",
        "actual_sales_amount",
        "gift_sales_num",
        "post_amount",
        "post_cost",
        "ship_refund_num",
        "ship_refund_amount",
        "abnormal_warehouse_sales_num",
        "refund_stockin",
    ]

@admin.register(FinanceSalesAndInvoice)
class FinanceSalesAndInvoiceAdmin(admin.ModelAdmin):
    list_display = [
        "created_at",
        "start_date",
        "end_date",
        "date",
        "shop_name",
        "goods_no",
        "material_no",
        "goods_name",
        "sales_num",
        "invoice_num",
        "sales_amount",
        "post_amount",
        "refund_amount",
        "invoice_amount",
    ]
    search_fields = ["goods_no"]
    list_filter = (
        (
            "date",
            DateRangeFilterBuilder(
                title="开票/退款时间",
            ),
        ),
    )

@admin.register(PDMaterialNOList)
class PDMaterialNOListAdmin(admin.ModelAdmin):
    list_display = [
        "material_no",
        "type",
        "goods_name",
        "invoice_goods_name",
        "goods_no",
        "no_product_series",
        "barcode",
        "unit",
        "feature",
        "brand",
        "weight",
    ]
    search_fields = ["material_no", "goods_name", "goods_no", "barcode"]
