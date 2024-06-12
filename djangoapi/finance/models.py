from django.db import models

# 天猫仅退款
class TmallRefund(models.Model):
    trade_no = models.CharField(max_length=100, verbose_name='订单编号')
    refund_no = models.CharField(max_length=100, unique=True, verbose_name='退款编号')
    alipay_transaction_no = models.CharField(max_length=100, blank=True, null=True, verbose_name='支付宝交易号')
    pay_time = models.DateTimeField(blank=True, null=True, verbose_name='订单付款时间')
    goods_no = models.CharField(max_length=100, blank=True, null=True, verbose_name='商品编码')
    refund_close_time = models.DateTimeField(blank=True, null=True, verbose_name='退款完结时间')
    paid = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='买家实际支付金额')
    goods_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='宝贝标题')
    refund = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='买家退款金额')
    refund_source = models.CharField(max_length=40, blank=True, null=True, verbose_name='手工退款_系统退款')
    goods_return = models.CharField(max_length=40, blank=True, null=True, verbose_name='是否需要退货')
    apply_time = models.DateTimeField(blank=True, null=True, verbose_name='退款的申请时间')
    refund_deadline = models.DateTimeField(blank=True, null=True, verbose_name='超时时间')
    refund_status = models.CharField(max_length=40, blank=True, null=True, verbose_name='退款状态')
    goods_status = models.CharField(max_length=40, blank=True, null=True, verbose_name='货物状态')
    deliver_logistics_info = models.CharField(max_length=255, blank=True, null=True, verbose_name='发货物流信息')
    service_intervene = models.CharField(max_length=40, blank=True, null=True, verbose_name='客服介入状态')
    seller_name = models.CharField(max_length=40, blank=True, null=True, verbose_name='卖家真实姓名')
    seller_name_new = models.CharField(max_length=40, blank=True, null=True, verbose_name='卖家真实姓名_新')
    refund_reason = models.CharField(max_length=255, blank=True, null=True, verbose_name='买家退款原因')
    refund_explanation = models.CharField(max_length=1024, blank=True, null=True, verbose_name='买家退款说明')
    refund_type = models.CharField(max_length=40, blank=True, null=True, verbose_name='部分退款_全部退款')

    class Meta:
        verbose_name = "天猫仅退款"
        verbose_name_plural = "天猫仅退款"

# 拼多多仅退款
class PddRefund(models.Model):
    shop_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='店铺名称')
    trade_no = models.CharField(max_length=100, verbose_name='订单号')
    goods_id = models.CharField(max_length=100, blank=True, null=True, verbose_name='商品ID')
    goods_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='商品名称')
    refund_reason = models.CharField(max_length=255, blank=True, null=True, verbose_name='扣款原因')
    applicant = models.CharField(max_length=100, blank=True, null=True, verbose_name='申请人')    
    apply_time = models.DateTimeField(blank=True, null=True, verbose_name='申请时间')
    refund = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='申请扣款金额')
    refund_status = models.CharField(max_length=40, blank=True, null=True, verbose_name='打款状态')

    class Meta:
        verbose_name = "拼多多仅退款"
        verbose_name_plural = "拼多多仅退款"
        constraints = [
            models.UniqueConstraint(fields=['trade_no', 'goods_id', 'applicant'], name='unique_tradeno_goodsid_applicant')
        ]

# 京东仅退款
class JdRefund(models.Model):
    shop_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='店铺名称')
    apply_time = models.DateTimeField(blank=True, null=True, verbose_name='申请时间')
    refund_no = models.CharField(max_length=100, verbose_name='赔付单号')
    trade_no = models.CharField(max_length=100, blank=True, null=True, verbose_name='关联订单号')
    service_no = models.CharField(max_length=100, blank=True, null=True, verbose_name='关联服务单号')
    refund = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='赔付金额')
    refund_reason = models.CharField(max_length=255, blank=True, null=True, verbose_name='赔付原因')
    refund_status = models.CharField(max_length=40, blank=True, null=True, verbose_name='赔付状态')
    applicant = models.CharField(max_length=100, blank=True, null=True, verbose_name='申请人')    

    class Meta:
        verbose_name = "京东仅退款"
        verbose_name_plural = "京东仅退款"       
        constraints = [
            models.UniqueConstraint(fields=['refund_no', 'trade_no', 'service_no'], name='unique_refundno_tradeno_serviceno')
        ]

# 抖音仅退款
class DouyinRefund(models.Model):
    shop_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='店铺名称')
    pay_transaction_no = models.CharField(max_length=100, blank=True, null=True, verbose_name='支付流水号')
    trade_no = models.CharField(max_length=100, verbose_name='订单编号')
    goods_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='商品名称')
    goods_id = models.CharField(max_length=100, blank=True, null=True, verbose_name='商品ID')
    refund_reason = models.CharField(max_length=255, blank=True, null=True, verbose_name='打款类型')
    refund = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='打款金额')
    applicant = models.CharField(max_length=100, blank=True, null=True, verbose_name='打款申请人')
    apply_time = models.DateTimeField(blank=True, null=True, verbose_name='打款申请时间')
    refund_time = models.DateTimeField(blank=True, null=True, verbose_name='打款到账时间')
    refund_status = models.CharField(max_length=40, blank=True, null=True, verbose_name='打款状态')
    refund_remark = models.CharField(max_length=1024, blank=True, null=True, verbose_name='打款备注')

    class Meta:
        verbose_name = "抖音仅退款"
        verbose_name_plural = "抖音仅退款"
        constraints = [
            models.UniqueConstraint(fields=['pay_transaction_no', 'trade_no', 'goods_id'], name='unique_paytransactionno_tradeno_goodsid')
        ]

# 发票，包括阿里发票和财务手工调整的发票
class Invoice(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='入库时间')
    trade_no = models.CharField(max_length=100, blank=True, null=True, verbose_name='订单id')
    invoice_time = models.DateTimeField(blank=True, null=True, verbose_name='开票日期')
    shop_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='店铺名称')
    invoice_category = models.CharField(max_length=40, blank=True, null=True, verbose_name='发票种类')
    invoice_type = models.CharField(max_length=40, blank=True, null=True, verbose_name='发票类型')
    invoice_no = models.CharField(max_length=100, blank=True, null=True, verbose_name='发票号码发票代码')
    seller_tax_no = models.CharField(max_length=100, blank=True, null=True, verbose_name='税号')
    seller_corp_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='企业名称')
    invoice_title = models.CharField(max_length=100, blank=True, null=True, verbose_name='发票抬头')
    payer_tax_no = models.CharField(max_length=100, blank=True, null=True, verbose_name='付款人税号')
    invoice_tax = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='总税额')
    invoice_amount = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='发票总金额')
    red_to_blue = models.CharField(max_length=100, blank=True, null=True, verbose_name='红票对应蓝票')
    remark = models.CharField(max_length=1024, blank=True, null=True, verbose_name='备注')
    goods_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='商品名称')
    goods_model = models.CharField(max_length=100, blank=True, null=True, verbose_name='商品型号')
    goods_unit = models.CharField(max_length=40, blank=True, null=True, verbose_name='商品单位')
    goods_price = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='单价')
    goods_num = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='数量')
    goods_amount_without_tax = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='不含税金额')
    goods_tax = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='税额')
    goods_total_amount = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='总金额')
    tax_rate = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='税率')

    class Meta:
        verbose_name = "发票"
        verbose_name_plural = "发票"       

# 旺店通货品销售汇总表
class GoodsSalesSummary(models.Model):
    start_date = models.DateField(verbose_name='开始日期')
    end_date = models.DateField(verbose_name='结束日期')
    spec_no = models.CharField(max_length=100, verbose_name='商家编码')
    major_supplier = models.CharField(max_length=100, blank=True, null=True, verbose_name='主供应商')
    shop_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='店铺')
    brand_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='品牌')
    goods_type = models.CharField(max_length=255, blank=True, null=True, verbose_name='分类')
    goods_no = models.CharField(max_length=100, blank=True, null=True, verbose_name='货品编号')
    goods_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='货品名称')
    spec_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='规格名称')
    goods_category = models.CharField(max_length=40, blank=True, null=True, verbose_name='货品类别')
    average_price = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='均价')
    retail_price = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='零售价')
    ship_num = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='发货总量')
    return_num = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='退货入库量（原退货总量）')
    return_count_num = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='退货入库结算量')
    sales_num = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='实际销售量')
    ship_amount = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='发货总金额')
    sales_amount = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='销售总金额')
    sales_amount_unknown_cost = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='未知成本销售总额')
    return_amount = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='退货总金额（结算）')
    actual_sales_amount = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='实际销售额')
    gift_sales_num = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='赠品销量')
    post_amount = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='邮费')
    post_cost = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='邮资成本')
    ship_refund_num = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='系统发货但平台退款量')
    ship_refund_amount = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='系统发货但平台退款金额')
    abnormal_warehouse_sales_num = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='异常仓销量')
    refund_stockin = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='退货总金额（入库）')

    class Meta:
        verbose_name = "旺店通货品销售汇总表"
        verbose_name_plural = "旺店通货品销售汇总表"        
        constraints = [
            models.UniqueConstraint(fields=['start_date', 'spec_no', 'shop_name'], name='unique_startdate_specno_shopname')
        ]

class FinanceSalesAndInvoice(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    start_date = models.DateField(blank=True, null=True, verbose_name='开始日期（统计）')
    end_date = models.DateField(blank=True, null=True, verbose_name='结束日期（统计）')
    date = models.DateField(blank=True, null=True, verbose_name='开票/退款日期')
    shop_name = models.CharField(max_length=100, verbose_name='店铺名称')
    goods_no = models.CharField(max_length=100, verbose_name='商家编码')
    material_no = models.CharField(max_length=100, blank=True, null=True, verbose_name='料号')
    goods_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='商品名称')
    sales_num = models.IntegerField(blank=True, null=True, verbose_name='实际销售量')
    invoice_num = models.IntegerField(blank=True, null=True, verbose_name='已开票数量')
    sales_amount = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='实际销售额')
    post_amount = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='邮费')
    refund_amount = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='退款金额')
    invoice_amount = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='已开票金额')

# 智创料号清单
class PDMaterialNOList(models.Model):
    type = models.CharField(max_length=100, blank=True, null=True, verbose_name='采购分类.分类名称')
    material_no = models.CharField(max_length=100, unique=True, verbose_name='料号')
    goods_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='品名')
    invoice_goods_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='开票品名')
    goods_no = models.CharField(max_length=100, blank=True, null=True, verbose_name='货号')
    no_product_series = models.CharField(max_length=100, blank=True, null=True, verbose_name='重编编号(产品系列)')
    barcode = models.CharField(max_length=100, blank=True, null=True, verbose_name='条码')
    unit = models.CharField(max_length=40, blank=True, null=True, verbose_name='库存单位.名称')
    feature = models.CharField(max_length=40, blank=True, null=True, verbose_name='料品形态属性')
    brand = models.CharField(max_length=255, blank=True, null=True, verbose_name='品牌')
    weight = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='(单件重)')

    class Meta:
        verbose_name = "智创料号清单"
        verbose_name_plural = "智创料号清单"
