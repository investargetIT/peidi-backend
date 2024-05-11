from django.db import models

# 天猫仅退款
class TmallRefund(models.Model):
    trade_no = models.CharField(max_length=100, verbose_name='订单编号')
    refund_no = models.CharField(max_length=100, blank=True, null=True, verbose_name='退款编号')
    alipay_transaction_no = models.CharField(max_length=100, blank=True, null=True, verbose_name='支付宝交易号')
    pay_time = models.DateTimeField(blank=True, null=True, verbose_name='订单付款时间')
    goods_no = models.CharField(max_length=100, blank=True, null=True, verbose_name='商品编码')
    refund_close_time = models.DateTimeField(blank=True, null=True, verbose_name='退款完结时间')
    paid = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='买家实际支付金额')
    goods_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='宝贝标题')
    refund = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='买家退款金额')
    refund_source = models.CharField(max_length=40, blank=True, null=True, verbose_name='手工退款_系统退款')
    goods_return = models.CharField(max_length=40, blank=True, null=True, verbose_name='是否需要退货')
    refund_apply_time = models.DateTimeField(blank=True, null=True, verbose_name='退款的申请时间')
    refund_deadline = models.DateTimeField(blank=True, null=True, verbose_name='超时时间')
    refund_status = models.CharField(max_length=40, blank=True, null=True, verbose_name='退款状态')
    goods_status = models.CharField(max_length=40, blank=True, null=True, verbose_name='货物状态')
    return_logistics_info = models.CharField(max_length=255, blank=True, null=True, verbose_name='退货物流信息')
    deliver_logistics_info = models.CharField(max_length=255, blank=True, null=True, verbose_name='发货物流信息')
    service_intervene = models.CharField(max_length=40, blank=True, null=True, verbose_name='客服介入状态')
    seller_name = models.CharField(max_length=40, blank=True, null=True, verbose_name='卖家真实姓名')
    seller_name_new = models.CharField(max_length=40, blank=True, null=True, verbose_name='卖家真实姓名_新')
    seller_return_address = models.CharField(max_length=255, blank=True, null=True, verbose_name='卖家退货地址')
    seller_zip = models.CharField(max_length=20, blank=True, null=True, verbose_name='卖家邮编')    
    seller_telno = models.CharField(max_length=40, blank=True, null=True, verbose_name='卖家电话')    
    seller_mobile = models.CharField(max_length=40, blank=True, null=True, verbose_name='卖家手机')
    logistics_no = models.CharField(max_length=100, blank=True, null=True, verbose_name='退货物流单号')
    logistics_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='退货物流公司')
    refund_reason = models.CharField(max_length=255, blank=True, null=True, verbose_name='买家退款原因')
    refund_explanation = models.CharField(max_length=1024, blank=True, null=True, verbose_name='买家退款说明')

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['trade_no', 'refund_no', 'alipay_transaction_no', 'goods_no'], name='unique_tradeno_refundno_alipaytransactionno_goodsno')
        ]

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
        constraints = [
            models.UniqueConstraint(fields=['pay_transaction_no', 'trade_no', 'goods_id'], name='unique_paytransactionno_tradeno_goodsid')
        ]

# 发票
class Invoice(models.Model):
    trade_no = models.CharField(max_length=100, verbose_name='订单id')
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
        constraints = [
            models.UniqueConstraint(fields=['trade_no', 'goods_model', 'goods_total_amount'], name='unique_tradeno_goodsmodel_goodstotalamount')
        ]
