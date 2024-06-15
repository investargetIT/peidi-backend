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
    material_no = Field(attribute='material_no', column_name='料号')
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

class InvoiceAliResource(resources.ModelResource):
    trade_no = Field(attribute='trade_no', column_name='订单id')
    invoice_time = Field(attribute='invoice_time', column_name='开票日期')
    shop_name = Field(attribute='shop_name', column_name='店铺名称')
    invoice_category = Field(attribute='invoice_category', column_name='发票种类')
    invoice_type = Field(attribute='invoice_type', column_name='发票类型')
    invoice_no = Field(attribute='invoice_no', column_name='发票号码发票代码')
    seller_tax_no = Field(attribute='seller_tax_no', column_name='税号')
    seller_corp_name = Field(attribute='seller_corp_name', column_name='企业名称')
    invoice_title = Field(attribute='invoice_title', column_name='发票抬头')
    payer_tax_no = Field(attribute='payer_tax_no', column_name='付款人税号')
    invoice_tax = Field(attribute='invoice_tax', column_name='总税额')
    invoice_amount = Field(attribute='invoice_amount', column_name='发票总金额')
    red_to_blue = Field(attribute='red_to_blue', column_name='红票对应蓝票')
    remark = Field(attribute='remark', column_name='备注')
    goods_name = Field(attribute='goods_name', column_name='商品名称')
    goods_model = Field(attribute='goods_model', column_name='商品型号')
    goods_unit = Field(attribute='goods_unit', column_name='商品单位')
    goods_price = Field(attribute='goods_price', column_name='单价')
    goods_num = Field(attribute='goods_num', column_name='数量')
    goods_amount_without_tax = Field(attribute='goods_amount_without_tax', column_name='不含税金额')
    goods_tax = Field(attribute='goods_tax', column_name='税额')
    goods_total_amount = Field(attribute='goods_total_amount', column_name='总金额')
    tax_rate = Field(attribute='tax_rate', column_name='税率')
   
    def before_import_row(self, row, **kwargs):
        row['开票日期'] = row['开票日期'].strip().replace('/', '-')
        
        float_fields = ["数量", "单价"]
        for float_field in float_fields:
            if row[float_field]:
                row[float_field] = "{:.4f}".format(float(row[float_field]))
            else:
                row[float_field] = None

        if row['店铺名称'] == 'smartbones旗舰店':
            row['店铺名称'] = '杭州-天猫-smartbones旗舰店'
        elif row['店铺名称'] == '哈宠宠物用品专营店':
            row['店铺名称'] = '上海-天猫-哈宠宠物用品专营店'
        elif row['店铺名称'] == '好适嘉旗舰店':
            row['店铺名称'] = '杭州-天猫-好适嘉旗舰店'
        elif row['店铺名称'] == '佩蒂旗舰店':
            row['店铺名称'] = '杭州-天猫-佩蒂旗舰店'
        elif row['店铺名称'] == '千百仓宠物用品专营店':
            row['店铺名称'] = '上海-天猫-千百仓宠物用品专营店'        

    class Meta:
        model = Invoice

class TmallRefundResource(resources.ModelResource):
    refund_no = Field(attribute='refund_no', column_name='退款编号')
    trade_no = Field(attribute='trade_no', column_name='订单编号')
    alipay_transaction_no = Field(attribute='alipay_transaction_no', column_name='支付宝交易号')
    pay_time = Field(attribute='pay_time', column_name='订单付款时间')
    goods_no = Field(attribute='goods_no', column_name='商品编码')
    refund_close_time = Field(attribute='refund_close_time', column_name='退款完结时间')
    paid = Field(attribute='paid', column_name='买家实际支付金额')
    goods_name = Field(attribute='goods_name', column_name='宝贝标题')
    refund = Field(attribute='refund', column_name='买家退款金额')
    refund_source = Field(attribute='refund_source', column_name='手工退款_系统退款')
    goods_return = Field(attribute='goods_return', column_name='是否需要退货')
    apply_time = Field(attribute='apply_time', column_name='退款的申请时间')
    refund_status = Field(attribute='refund_status', column_name='退款状态')
    goods_status = Field(attribute='goods_status', column_name='货物状态')
    deliver_logistics_info = Field(attribute='deliver_logistics_info', column_name='发货物流信息')
    service_intervene = Field(attribute='service_intervene', column_name='客服介入状态')
    seller_name = Field(attribute='seller_name', column_name='卖家真实姓名')
    seller_name_new = Field(attribute='seller_name_new', column_name='卖家真实姓名_新')
    refund_reason = Field(attribute='refund_reason', column_name='买家退款原因')
    refund_explanation = Field(attribute='refund_explanation', column_name='买家退款说明')
    refund_type = Field(attribute='refund_type', column_name='部分退款_全部退款')

    class Meta:
        model = TmallRefund

class JdRefundResource(resources.ModelResource):
    shop_name = Field(attribute='shop_name', column_name='店铺名称')
    apply_time = Field(attribute='apply_time', column_name='申请时间')
    refund_no = Field(attribute='refund_no', column_name='赔付单号')
    trade_no = Field(attribute='trade_no', column_name='关联订单号')
    service_no = Field(attribute='service_no', column_name='关联服务单号')
    refund = Field(attribute='refund', column_name='赔付金额')
    refund_reason = Field(attribute='refund_reason', column_name='赔付原因')
    refund_status = Field(attribute='refund_status', column_name='赔付状态')
    applicant = Field(attribute='applicant', column_name='申请人')

    class Meta:
        model = JdRefund 

class DouyinRefundResource(resources.ModelResource):
    shop_name = Field(attribute='shop_name', column_name='店铺名称')
    pay_transaction_no = Field(attribute='pay_transaction_no', column_name='支付流水号')
    trade_no = Field(attribute='trade_no', column_name='订单编号')
    goods_name = Field(attribute='goods_name', column_name='商品名称')
    goods_id = Field(attribute='goods_id', column_name='商品ID')
    refund_reason = Field(attribute='refund_reason', column_name='打款类型')
    refund = Field(attribute='refund', column_name='打款金额')
    applicant = Field(attribute='applicant', column_name='打款申请人')
    apply_time = Field(attribute='apply_time', column_name='打款申请时间')
    refund_time = Field(attribute='refund_time', column_name='打款到账时间')
    refund_status = Field(attribute='refund_status', column_name='打款状态')
    refund_remark = Field(attribute='refund_remark', column_name='打款备注')

    class Meta:
        model = DouyinRefund

class PddRefundResource(resources.ModelResource):
    shop_name = Field(attribute='shop_name', column_name='店铺名称')
    trade_no = Field(attribute='trade_no', column_name='订单号')
    goods_id = Field(attribute='goods_id', column_name='商品ID')
    goods_name = Field(attribute='goods_name', column_name='商品名称')
    refund_reason = Field(attribute='refund_reason', column_name='扣款原因')
    applicant = Field(attribute='applicant', column_name='申请人')
    apply_time = Field(attribute='apply_time', column_name='申请时间')
    refund = Field(attribute='refund', column_name='申请扣款金额')
    refund_status = Field(attribute='refund_status', column_name='打款状态')

    class Meta:
        model = PddRefund

class GoodsSalesSummaryResource(resources.ModelResource):
    start_date = Field(attribute='start_date', column_name='开始日期')
    end_date = Field(attribute='end_date', column_name='结束日期')
    spec_no = Field(attribute='spec_no', column_name='商家编码')
    major_supplier = Field(attribute='major_supplier', column_name='主供应商')
    shop_name = Field(attribute='shop_name', column_name='店铺')
    brand_name = Field(attribute='brand_name', column_name='品牌')
    goods_type = Field(attribute='goods_type', column_name='分类')
    goods_no = Field(attribute='goods_no', column_name='货品编号')
    goods_name = Field(attribute='goods_name', column_name='货品名称')
    spec_name = Field(attribute='spec_name', column_name='规格名称')
    goods_category = Field(attribute='goods_category', column_name='货品类别')
    average_price = Field(attribute='average_price', column_name='均价')
    retail_price = Field(attribute='retail_price', column_name='零售价')
    ship_num = Field(attribute='ship_num', column_name='发货总量')
    return_num = Field(attribute='return_num', column_name='退货入库量（原退货总量）')
    return_count_num = Field(attribute='return_count_num', column_name='退货入库结算量')
    sales_num = Field(attribute='sales_num', column_name='实际销售量')
    ship_amount = Field(attribute='ship_amount', column_name='发货总金额')
    sales_amount = Field(attribute='sales_amount', column_name='销售总金额')
    sales_amount_unknown_cost = Field(attribute='sales_amount_unknown_cost', column_name='未知成本销售总额')
    return_amount = Field(attribute='return_amount', column_name='退货总金额（结算）')
    actual_sales_amount = Field(attribute='actual_sales_amount', column_name='实际销售额')
    gift_sales_num = Field(attribute='gift_sales_num', column_name='赠品销量')
    post_amount = Field(attribute='post_amount', column_name='邮费')
    post_cost = Field(attribute='post_cost', column_name='邮资成本')
    ship_refund_num = Field(attribute='ship_refund_num', column_name='系统发货但平台退款量')
    ship_refund_amount = Field(attribute='ship_refund_amount', column_name='系统发货但平台退款金额')
    abnormal_warehouse_sales_num = Field(attribute='abnormal_warehouse_sales_num', column_name='异常仓销量')
    refund_stockin = Field(attribute='refund_stockin', column_name='退货总金额（入库）')

    class Meta:
        model = GoodsSalesSummary

class PDMaterialNoListResource(resources.ModelResource):
    type = Field(attribute='type', column_name='采购分类.分类名称')
    material_no = Field(attribute='material_no', column_name='料号')
    goods_name = Field(attribute='goods_name', column_name='品名')
    invoice_goods_name = Field(attribute='invoice_goods_name', column_name='开票品名')
    goods_no = Field(attribute='goods_no', column_name='货号')
    no_product_series = Field(attribute='no_product_series', column_name='重编编号(产品系列)')
    barcode = Field(attribute='barcode', column_name='条码')
    unit = Field(attribute='unit', column_name='库存单位.名称')
    feature = Field(attribute='feature', column_name='料品形态属性')
    brand = Field(attribute='brand', column_name='品牌')
    weight = Field(attribute='weight', column_name='(单件重)')

    def before_import(self, dataset, **kwargs):
        PDMaterialNOList.objects.all().delete()

    class Meta:
        model = PDMaterialNOList 

@admin.register(TmallRefund)
class TmallRefundAdmin(ImportExportModelAdmin): 
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
        "refund_status",
        "goods_status",
        "deliver_logistics_info",
        "service_intervene",
        "seller_name",
        "seller_name_new",
        "refund_type",
        "refund_reason",
        "refund_explanation",
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
    resource_classes = [TmallRefundResource]

@admin.register(PddRefund)
class PddRefundAdmin(ImportExportModelAdmin):
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
    resource_classes = [PddRefundResource]

@admin.register(JdRefund)
class JdRefundAdmin(ImportExportModelAdmin):
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
    resource_classes = [JdRefundResource]

@admin.register(DouyinRefund)
class DouyinRefundAdmin(ImportExportModelAdmin):
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
    resource_classes = [DouyinRefundResource]

@admin.register(InvoiceManual)
class InvoiceManualAdmin(ImportExportModelAdmin):
    list_display = [
        "invoice_time",
        "shop_name",
        "goods_model",
        "material_no",
        "goods_name",
        "goods_num",
        "goods_total_amount",
        "created_at",
    ]
    search_fields = ["goods_model", "goods_name"]
    list_filter = ["shop_name"]
    resource_classes = [InvoiceManualResource]

@admin.register(Invoice)
class InvoiceAdmin(ImportExportModelAdmin):
    list_display = [ 
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
        # "goods_unit",
        "goods_price",
        "goods_num",
        "goods_amount_without_tax",
        "goods_tax",
        "goods_total_amount",
        "tax_rate",
        "created_at",
    ]
    search_fields = ["trade_no", "goods_model"]
    list_filter = ["shop_name"]
    resource_classes = [InvoiceAliResource]

@admin.register(GoodsSalesSummary)
class GoodsSalesSummaryAdmin(ImportExportModelAdmin):
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
    resource_classes = [GoodsSalesSummaryResource]

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
class PDMaterialNOListAdmin(ImportExportModelAdmin):
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
    resource_classes = [PDMaterialNoListResource]
