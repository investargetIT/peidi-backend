from django.db import models

# Create your models here.



class orders(models.Model):
    trade_no = models.CharField(max_length=100, blank=True, null=True, verbose_name='订单编号')
    platform = models.CharField(max_length=100, blank=True, null=True, verbose_name='平台')
    shop_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='店铺/店铺名称')
    tid = models.CharField(max_length=100, blank=True, null=True, unique=True, verbose_name='原始单号')
    warehouse = models.CharField(max_length=100, blank=True, null=True, verbose_name='仓库名称')
    warehouse_no = models.CharField(max_length=100, blank=True, null=True, verbose_name='外部仓库编号')
    order_type = models.CharField(max_length=40, blank=True, null=True, verbose_name='订单类型')
    trade_status = models.CharField(max_length=40, blank=True, null=True, verbose_name='平台状态')
    pay_status = models.CharField(max_length=40, blank=True, null=True, verbose_name='支付状态')
    guarantee_mode = models.CharField(max_length=40, blank=True, null=True, verbose_name='担保方式')
    delivery_term = models.CharField(max_length=40, blank=True, null=True, verbose_name='货到付款/发货条件')
    freeze_reason = models.CharField(max_length=100, blank=True, null=True, verbose_name='冻结原因')
    pay_method = models.CharField(max_length=40, blank=True, null=True, verbose_name='支付方式')
    refund_status = models.CharField(max_length=40, blank=True, null=True, verbose_name='退款状态')
    process_status = models.CharField(max_length=40, blank=True, null=True, verbose_name='系统处理状态/订单状态')
    bad_reason = models.TextField(blank=True, null=True, verbose_name='递交失败原因')
    trade_time = models.DateTimeField(blank=True, null=True, verbose_name='下单时间/交易时间')
    pay_time = models.DateTimeField(blank=True, null=True, verbose_name='支付时间/付款时间')
    end_time = models.DateTimeField(blank=True, null=True, verbose_name='结束时间')
    buyer_nick = models.CharField(max_length=100, blank=True, null=True, verbose_name='客户网名')
    receiver_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='收件人姓名')
    receiver_area = models.CharField(max_length=128, blank=True, null=True, verbose_name='省市县')
    receiver_ring = models.CharField(max_length=100, blank=True, null=True, verbose_name='区域（京东几环）')
    receiver_dtb = models.CharField(max_length=128, blank=True, null=True, verbose_name='大头笔')
    receiver_address = models.CharField(max_length=255, blank=True, null=True, verbose_name='收件人地址')
    receiver_mobile = models.CharField(max_length=40, blank=True, null=True, verbose_name='收件人手机')
    receiver_telno = models.CharField(max_length=40, blank=True, null=True, verbose_name='收件人电话')
    receiver_zip = models.CharField(max_length=20, blank=True, null=True, verbose_name='收件人邮编')
    to_deliver_time = models.DateTimeField(blank=True, null=True, verbose_name='送货时间/派送时间')
    logistics_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='物流公司')
    logistics_no = models.CharField(max_length=100, blank=True, null=True, verbose_name='物流编码/物流单号')
    buyer_message = models.CharField(max_length=1024, blank=True, null=True, verbose_name='买家备注/客户备注')
    remark = models.CharField(max_length=1024, blank=True, null=True, verbose_name='客服备注')
    biaoqi = models.CharField(max_length=100, blank=True, null=True, verbose_name='标旗/客服标旗')
    print_remark = models.CharField(max_length=1024, blank=True, null=True, verbose_name='打印备注')
    goods_type_count = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='货品种类数')
    goods_count = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='货品总数')
    goods_amount = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='货款/货品总额')
    post_amount = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='邮费/邮资')
    other_amount = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='其他收费')
    discount = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='优惠')
    platform_cost = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='平台费用')
    received = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='已收')
    receivable = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='应收/应收金额')
    cash_on_delivery_amount = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='货到付款金额/COD金额')
    ext_cod_fee = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='买家COD费用')
    refund_amount = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='退款金额')
    commission = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='佣金')
    logistics_type = models.CharField(max_length=40, blank=True, null=True, verbose_name='物流方式')
    invoice_type = models.CharField(max_length=40, blank=True, null=True, verbose_name='发票类别/需要发票',
                                     help_text='否/普通发票/电子发票/专用发票/全电普通发票/全电专用发票')
    payer_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='发票抬头/付款方名称')
    invoice_content = models.TextField(blank=True, null=True, verbose_name='发票内容')
    flag_name = models.CharField(max_length=32, blank=True, null=True, verbose_name='标记名称')
    is_auto_wms = models.CharField(max_length=40, blank=True, null=True, verbose_name='是否自流转')
    is_ware_trade = models.CharField(max_length=40, blank=True, null=True, verbose_name='外部订单')
    trade_from = models.CharField(max_length=40, blank=True, null=True, verbose_name='订单来源')
    pay_id = models.CharField(max_length=40, blank=True, null=True, verbose_name='支付单号')
    pay_account = models.CharField(max_length=128, blank=True, null=True, verbose_name='买家支付账号/买家付款账号')
    paid = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='已付')
    consumer_amount = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='消费者实付金额')
    platform_amount = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='平台承担优惠金额')
    currency = models.TextField(blank=True, null=True, verbose_name='币种')
    id_no = models.CharField(max_length=40, blank=True, null=True, verbose_name='证件号码')
    single_spec_no = models.CharField(max_length=100, blank=True, null=True, verbose_name='货品商家编码')
    raw_goods_count = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='原始货品数量')
    raw_goods_type_count = models.IntegerField(blank=True, null=True, verbose_name='原始货品种类数')
    stockout_no = models.CharField(max_length=100, blank=True, null=True, verbose_name='出库单号')
    modified = models.DateTimeField(blank=True, null=True, verbose_name='修改时间')
    created = models.DateTimeField(blank=True, null=True, verbose_name='创建时间/递交时间')

class salesOutDetails(models.Model):
    trade_no = models.CharField(max_length=100, blank=True, null=True, verbose_name='订单编号')
    tid = models.CharField(max_length=100, blank=True, null=True, verbose_name='原始单号')
    oid = models.CharField(max_length=100, blank=True, null=True, verbose_name='原始子订单号')
    otid = models.CharField(max_length=100, blank=True, null=True, verbose_name='子单原始单号')
    order_type = models.CharField(max_length=40, blank=True, null=True, verbose_name='订单类别')
    trade_from = models.CharField(max_length=40, blank=True, null=True, verbose_name='订单来源')
    pay_account = models.CharField(max_length=128, blank=True, null=True, verbose_name='支付账号/付款账号')
    stockout_no = models.CharField(max_length=100, blank=True, null=True, verbose_name='出库单编号')
    warehouse = models.CharField(max_length=100, blank=True, null=True, verbose_name='仓库')
    shop_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='店铺')
    status_type = models.CharField(max_length=100, blank=True, null=True, verbose_name='出库单状态')
    stockout_status = models.CharField(max_length=100, blank=True, null=True, verbose_name='出库状态')
    spec_no = models.CharField(max_length=100, blank=True, null=True, verbose_name='商家编码')
    goods_no = models.CharField(max_length=100, blank=True, null=True, verbose_name='货品编号')
    goods_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='货品名称')
    goods_short_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='货品简称')
    brand_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='品牌')
    goods_type = models.CharField(max_length=255, blank=True, null=True, verbose_name='分类')
    spec_id = models.CharField(max_length=40, blank=True, null=True, verbose_name='规格码')
    spec_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='规格名称')
    barcode = models.CharField(max_length=50, blank=True, null=True, verbose_name='条码')
    num = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='货品数量')
    unit_name = models.CharField(max_length=50, blank=True, null=True, verbose_name='单位')
    aux_num = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='辅助货品数量')
    aux_unit_name = models.CharField(max_length=50, blank=True, null=True, verbose_name='辅助单位')
    ori_price = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='货品原单价')
    ori_total_amount = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='货品原总金额')
    order_discount = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='订单总优惠')
    post_amount = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='订单邮费')
    share_post_amount = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='分摊邮费')
    deal_price = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='货品成交价')
    deal_total_price = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='货品成交总价')
    goods_discount = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='货品总优惠')
    cod_amount = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='货到付款金额/COD金额')
    receivable = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='应收金额')
    ori_receivable = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='子单应收金额')
    buyer_nick = models.CharField(max_length=100, blank=True, null=True, verbose_name='客户网名')
    receiver_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='收件人')
    receiver_area = models.CharField(max_length=128, blank=True, null=True, verbose_name='收货地区')
    receiver_address = models.CharField(max_length=255, blank=True, null=True, verbose_name='收货地址')
    receiver_mobile = models.CharField(max_length=40, blank=True, null=True, verbose_name='收件人手机')
    receiver_telno = models.CharField(max_length=40, blank=True, null=True, verbose_name='收件人电话')
    logistics_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='物流公司')
    invoice_type = models.CharField(max_length=40, blank=True, null=True, verbose_name='发票类别/需开发票',
                                    help_text='否/普通发票/电子发票/专用发票/全电普通发票/全电专用发票')
    flag_name = models.CharField(max_length=32, blank=True, null=True, verbose_name='标记名称')
    trade_time = models.DateTimeField(blank=True, null=True, verbose_name='下单时间/交易时间')
    pay_time = models.DateTimeField(blank=True, null=True, verbose_name='支付时间/付款时间')
    created = models.DateTimeField(blank=True, null=True, verbose_name='创建时间')
    deliver_time = models.DateTimeField(blank=True, null=True, verbose_name='发货时间')
    gift_method = models.CharField(max_length=128, blank=True, null=True, verbose_name='赠品方式')
    buyer_message = models.CharField(max_length=1024, blank=True, null=True, verbose_name='买家留言/客户备注')
    service_remark = models.CharField(max_length=1024, blank=True, null=True, verbose_name='客服备注')
    remark = models.CharField(max_length=1024, blank=True, null=True, verbose_name='备注')
    print_remark = models.CharField(max_length=1024, blank=True, null=True, verbose_name='打印备注')
    source_suite_no = models.CharField(max_length=100, blank=True, null=True, verbose_name='来源组合装编码')
    source_suite_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='来源组合装名称')
    source_suite_num = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, default=0, verbose_name='来源组合装数量')
    stockout_tag = models.CharField(max_length=100, blank=True, null=True, verbose_name='出库标签')
    order_tag = models.CharField(max_length=100, blank=True, null=True, verbose_name='订单标签')
    specgoods_price = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='单品零售价')
    distributor = models.CharField(max_length=100, blank=True, null=True, verbose_name='分销商名称')
    distributor_no = models.CharField(max_length=100, blank=True, null=True, verbose_name='分销商编号')
    paid = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='已付')
    distribution_oid = models.CharField(max_length=100, blank=True, null=True, verbose_name='分销原始单号')

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['oid', 'stockout_no', 'spec_no', 'goods_no'], name='unique_oid_stockoutno_specno_goodsno')
        ]


class historySalesOutDetails(models.Model):
    trade_no = models.CharField(max_length=100, blank=True, null=True, verbose_name='订单编号')
    tid = models.CharField(max_length=255, blank=True, null=True, verbose_name='原始单号')
    oid = models.CharField(max_length=100, blank=True, null=True, verbose_name='原始子订单号')
    otid = models.CharField(max_length=100, blank=True, null=True, verbose_name='子单原始单号')
    order_type = models.CharField(max_length=40, blank=True, null=True, verbose_name='订单类别')
    trade_from = models.CharField(max_length=40, blank=True, null=True, verbose_name='订单来源')
    pay_account = models.CharField(max_length=128, blank=True, null=True, verbose_name='支付账号/付款账号')
    stockout_no = models.CharField(max_length=100, blank=True, null=True, verbose_name='出库单编号')
    warehouse = models.CharField(max_length=100, blank=True, null=True, verbose_name='仓库')
    shop_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='店铺')
    status_type = models.CharField(max_length=100, blank=True, null=True, verbose_name='出库单状态')
    stockout_status = models.CharField(max_length=100, blank=True, null=True, verbose_name='出库状态')
    spec_no = models.CharField(max_length=100, blank=True, null=True, verbose_name='商家编码')
    goods_no = models.CharField(max_length=100, blank=True, null=True, verbose_name='货品编号')
    goods_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='货品名称')
    goods_short_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='货品简称')
    brand_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='品牌')
    goods_type = models.CharField(max_length=255, blank=True, null=True, verbose_name='分类')
    spec_id = models.CharField(max_length=40, blank=True, null=True, verbose_name='规格码')
    spec_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='规格名称')
    barcode = models.CharField(max_length=50, blank=True, null=True, verbose_name='条码')
    num = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='货品数量')
    unit_name = models.CharField(max_length=50, blank=True, null=True, verbose_name='单位')
    aux_num = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='辅助货品数量')
    aux_unit_name = models.CharField(max_length=50, blank=True, null=True, verbose_name='辅助单位')
    ori_price = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='货品原单价')
    ori_total_amount = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='货品原总金额')
    order_discount = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='订单总优惠')
    post_amount = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='订单邮费')
    share_post_amount = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='分摊邮费')
    deal_price = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='货品成交价')
    deal_total_price = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='货品成交总价')
    goods_discount = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='货品总优惠')
    cod_amount = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='货到付款金额/COD金额')
    receivable = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='应收金额')
    ori_receivable = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='子单应收金额')
    buyer_nick = models.CharField(max_length=100, blank=True, null=True, verbose_name='客户网名')
    receiver_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='收件人')
    receiver_area = models.CharField(max_length=128, blank=True, null=True, verbose_name='收货地区')
    receiver_address = models.CharField(max_length=255, blank=True, null=True, verbose_name='收货地址')
    receiver_mobile = models.CharField(max_length=40, blank=True, null=True, verbose_name='收件人手机')
    receiver_telno = models.CharField(max_length=40, blank=True, null=True, verbose_name='收件人电话')
    logistics_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='物流公司')
    invoice_type = models.CharField(max_length=40, blank=True, null=True, verbose_name='发票类别/需开发票',
                                    help_text='否/普通发票/电子发票/专用发票/全电普通发票/全电专用发票')
    flag_name = models.CharField(max_length=32, blank=True, null=True, verbose_name='标记名称')
    trade_time = models.DateTimeField(blank=True, null=True, verbose_name='下单时间/交易时间')
    pay_time = models.DateTimeField(blank=True, null=True, verbose_name='支付时间/付款时间')
    created = models.DateTimeField(blank=True, null=True, verbose_name='创建时间')
    deliver_time = models.DateTimeField(blank=True, null=True, verbose_name='发货时间')
    gift_method = models.CharField(max_length=128, blank=True, null=True, verbose_name='赠品方式')
    buyer_message = models.CharField(max_length=1024, blank=True, null=True, verbose_name='买家留言/客户备注')
    service_remark = models.CharField(max_length=1024, blank=True, null=True, verbose_name='客服备注')
    remark = models.CharField(max_length=1024, blank=True, null=True, verbose_name='备注')
    print_remark = models.CharField(max_length=1024, blank=True, null=True, verbose_name='打印备注')
    source_suite_no = models.CharField(max_length=100, blank=True, null=True, verbose_name='来源组合装编码')
    source_suite_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='来源组合装名称')
    source_suite_num = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, default=0, verbose_name='来源组合装数量')
    stockout_tag = models.CharField(max_length=100, blank=True, null=True, verbose_name='出库标签')
    order_tag = models.CharField(max_length=100, blank=True, null=True, verbose_name='订单标签')
    specgoods_price = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='单品零售价')
    distributor = models.CharField(max_length=100, blank=True, null=True, verbose_name='分销商名称')
    distributor_no = models.CharField(max_length=100, blank=True, null=True, verbose_name='分销商编号')
    paid = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='已付')
    distribution_oid = models.CharField(max_length=100, blank=True, null=True, verbose_name='分销原始单号')

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['oid', 'stockout_no', 'spec_no', 'goods_no'], name='historysalesout_unique_oid_stockoutno_specno_goodsno')
        ]
