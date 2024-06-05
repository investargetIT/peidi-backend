from django.db import models

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

class OrderDetail(models.Model):
    trade_no = models.CharField(max_length=100, verbose_name='订单编号')
    shop_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='店铺名称')
    trade_from = models.CharField(max_length=40, blank=True, null=True, verbose_name='订单来源')
    warehouse = models.CharField(max_length=100, blank=True, null=True, verbose_name='仓库')
    tid = models.CharField(max_length=512, blank=True, null=True, verbose_name='原始单号')
    oid = models.CharField(max_length=100, blank=True, null=True, verbose_name='原始子单号')
    process_status = models.CharField(max_length=40, blank=True, null=True, verbose_name='订单状态')
    order_type = models.CharField(max_length=40, blank=True, null=True, verbose_name='订单类型')
    delivery_term = models.CharField(max_length=40, blank=True, null=True, verbose_name='发货条件')
    refund_status = models.CharField(max_length=40, blank=True, null=True, verbose_name='订单退款状态')
    refund_status_of_details = models.CharField(max_length=40, blank=True, null=True, verbose_name='订单明细退款状态')
    trade_time = models.DateTimeField(blank=True, null=True, verbose_name='交易时间')
    pay_time = models.DateTimeField(blank=True, null=True, verbose_name='付款时间')
    deliver_time = models.DateTimeField(blank=True, null=True, verbose_name='发货时间')
    buyer_nick = models.CharField(max_length=100, blank=True, null=True, verbose_name='客户网名')
    receiver_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='收件人')
    receiver_area = models.CharField(max_length=128, blank=True, null=True, verbose_name='省市县')
    receiver_address = models.CharField(max_length=255, blank=True, null=True, verbose_name='地址')
    receiver_mobile = models.CharField(max_length=40, blank=True, null=True, verbose_name='手机')
    receiver_telno = models.CharField(max_length=40, blank=True, null=True, verbose_name='电话')
    receiver_zip = models.CharField(max_length=20, blank=True, null=True, verbose_name='邮编')
    logistics_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='物流公司')
    logistics_no = models.CharField(max_length=100, blank=True, null=True, verbose_name='物流单号')
    buyer_message = models.CharField(max_length=1024, blank=True, null=True, verbose_name='买家留言')
    service_remark = models.CharField(max_length=1024, blank=True, null=True, verbose_name='客服备注')
    print_remark = models.CharField(max_length=1024, blank=True, null=True, verbose_name='打印备注')
    remark = models.CharField(max_length=1024, blank=True, null=True, verbose_name='备注')
    biaoqi = models.CharField(max_length=100, blank=True, null=True, verbose_name='客服标旗')
    post_amount = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='订单邮费')
    other_amount = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='其它费用')
    order_discount = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='订单总优惠')
    receivable = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='应收金额')
    cod_amount = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='货到付款金额')
    invoice_type = models.CharField(max_length=40, blank=True, null=True, verbose_name='需要发票')
    payer_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='发票抬头')
    invoice_content = models.TextField(blank=True, null=True, verbose_name='发票内容')
    flag_name = models.CharField(max_length=32, blank=True, null=True, verbose_name='标记名称')
    spec_no = models.CharField(max_length=100, blank=True, null=True, verbose_name='商家编码')
    goods_no = models.CharField(max_length=100, blank=True, null=True, verbose_name='货品编号')
    goods_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='货品名称')
    spec_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='规格名称')
    goods_type = models.CharField(max_length=255, blank=True, null=True, verbose_name='分类')
    num = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='数量')
    ori_price = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='标价')
    discount = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='优惠')
    deal_price = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='成交价')
    share_price = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='分摊后价格')
    share_post_amount = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='分摊邮费')
    discount_rate = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='打折比')
    share_total_price = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='分摊后总价')
    commission = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='佣金')
    source_suite_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='拆自组合装')
    source_suite_no = models.CharField(max_length=100, blank=True, null=True, verbose_name='组合装编码')
    source_suite_num = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, default=0, verbose_name='组合装数量')
    gift_method = models.CharField(max_length=128, blank=True, null=True, verbose_name='赠品方式')
    platform_goods_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='平台货品名称')
    platform_spec_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='平台规格名称')
    order_tag = models.CharField(max_length=100, blank=True, null=True, verbose_name='订单标签')
    distributor = models.CharField(max_length=100, blank=True, null=True, verbose_name='分销商名称')
    distributor_no = models.CharField(max_length=100, blank=True, null=True, verbose_name='分销商编号')
    paid = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='已付')
    pay_account = models.CharField(max_length=128, blank=True, null=True, verbose_name='付款账号')
    deadline_deliver_time = models.DateTimeField(blank=True, null=True, verbose_name='最晚发货时间')
    buyer_no = models.CharField(max_length=100, blank=True, null=True, verbose_name='客户编号')
    distribution_oid = models.CharField(max_length=100, blank=True, null=True, verbose_name='分销原始单号')

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['trade_no', 'oid', 'spec_no', 'goods_no', 'num'], name='unique_tradeno_oid_specno_goodsno_num')
        ]

class salesOutDetails(models.Model):
    trade_no = models.CharField(max_length=100, blank=True, null=True, verbose_name='订单编号')
    tid = models.CharField(max_length=512, blank=True, null=True, verbose_name='原始单号')
    oid = models.CharField(max_length=100, blank=True, null=True, verbose_name='原始子订单号')
    otid = models.CharField(max_length=255, blank=True, null=True, verbose_name='子单原始单号')
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
            models.UniqueConstraint(fields=['oid', 'stockout_no', 'spec_no', 'goods_no', 'num'], name='unique_oid_stockoutno_specno_goodsno_num')
        ]
        indexes = [
            models.Index(fields=["otid"])
        ]

class historySalesOutDetails(models.Model):
    trade_no = models.CharField(max_length=100, blank=True, null=True, verbose_name='订单编号')
    tid = models.CharField(max_length=512, blank=True, null=True, verbose_name='原始单号')
    oid = models.CharField(max_length=100, blank=True, null=True, verbose_name='原始子订单号')
    otid = models.CharField(max_length=255, blank=True, null=True, verbose_name='子单原始单号')
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
            models.UniqueConstraint(fields=['oid', 'stockout_no', 'spec_no', 'goods_no', 'num'], name='unique_history_salesout_details')
        ]
        indexes = [
            models.Index(fields=["otid"])
        ]

class StockDetail(models.Model):
    spec_no = models.CharField(max_length=100, verbose_name='商家编码')
    barcode = models.CharField(max_length=50, blank=True, null=True, verbose_name='条码')
    goods_no = models.CharField(max_length=100, blank=True, null=True, verbose_name='货品编号')
    goods_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='货品名称')
    goods_short_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='货品简称')
    goods_tag = models.CharField(max_length=100, blank=True, null=True, verbose_name='货品标签')
    spec_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='规格名称')
    spec_id = models.CharField(max_length=40, blank=True, null=True, verbose_name='规格码')
    brand_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='品牌')
    qa_num = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='已质检库存')
    todeliver_order_num = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='未发货订单总数')
    retail_price = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='零售价')
    wholesale_price = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='批发价')
    market_price = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='市场价')
    member_price = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='会员价')
    lowest_price = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='最低价')
    goods_type = models.CharField(max_length=255, blank=True, null=True, verbose_name='分类')
    stock = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='库存')
    weight = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='单品重量')
    total_weight = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='库存总重量')
    is_defective = models.CharField(max_length=40, blank=True, null=True, verbose_name='是否残次品')
    unit_name = models.CharField(max_length=50, blank=True, null=True, verbose_name='单位')
    aux_unit_name = models.CharField(max_length=50, blank=True, null=True, verbose_name='辅助单位')
    aux_remark = models.CharField(max_length=50, blank=True, null=True, verbose_name='辅助说明')
    deliverable_stock = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='可发库存')
    usable_stock = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='可用库存')
    min_alert_stock = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='警戒库存下限')
    max_alert_stock = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='警戒库存上限')
    unpaid_num = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='未付款量')
    preorder_num = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='预订单量')
    toreview_num = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='待审核量')
    todeliver_num = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='待发货量')
    lock_num = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='锁定量')
    topurchase_num = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='待采购量')
    purchase_ontheway_num = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='采购在途')
    purchase_arrival_num = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='采购到货量')
    totransfer_num = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='待调拨量')
    totransout_num = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='待调出量')
    toinstock_num = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='其他待入库量')
    tooutstock_num = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='其他待出库量')
    transfer_ontheway_num = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='调拨在途')
    purchase_return_num = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='采购退货')
    sale_return_ontheway_num = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='销售退货在途量')
    produce_tooutstock_num = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='生产待出库量')
    produce_toinstock_num = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='生产待入库量')
    toqa_num = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='待质检量')
    outside_stock_num = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='外部库存')
    stock_diff = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='库存差异')
    sync_time = models.DateTimeField(blank=True, null=True, verbose_name='同步时间')
    remark = models.CharField(max_length=1024, blank=True, null=True, verbose_name='备注')
    goods_remark = models.CharField(max_length=1024, blank=True, null=True, verbose_name='货品备注')
    specgoods_remark = models.CharField(max_length=1024, blank=True, null=True, verbose_name='单品备注')
    onsale_time = models.DateTimeField(blank=True, null=True, verbose_name='首销时间')
    last_inventory_time = models.DateTimeField(blank=True, null=True, verbose_name='最后盘点时间')
    actual_stock_num = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='实际库存')
    actual_todelivery_stock_num = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='实际可发库存')
    img_url = models.CharField(max_length=1024, blank=True, null=True, verbose_name='图片链接')
    img = models.CharField(max_length=1024, blank=True, null=True, verbose_name='图片')
    major_supplier = models.CharField(max_length=100, blank=True, null=True, verbose_name='主供应商')
    custom_stock_one = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='自定义库存1')
    custom_stock_two = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='自定义库存2')
    custom_stock_three = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='自定义库存3')
    custom_stock_four = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='自定义库存4')
    custom_stock_five = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='自定义库存5')

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['spec_no', 'barcode', 'goods_no', 'qa_num'], name='stockdetail_unique_specno_barcode_goodsno_qanum')
        ]

class WMSShipData(models.Model):
    order_num = models.IntegerField(verbose_name='今日总单量')
    to_print = models.IntegerField(blank=True, null=True, verbose_name='订单待打印')
    printed = models.IntegerField(blank=True, null=True, verbose_name='今日已打印')
    to_ship = models.IntegerField(blank=True, null=True, verbose_name='实时订单待发货')
    shipped = models.IntegerField(blank=True, null=True, verbose_name='实时今日己发货')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

class ExchangeManagement(models.Model):
    exchange_no = models.CharField(unique=True, max_length=100, verbose_name='退换单号')
    shop_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='店铺')
    type = models.CharField(max_length=40, blank=True, null=True, verbose_name='类型')
    status = models.CharField(max_length=40, blank=True, null=True, verbose_name='状态')
    stock_status = models.CharField(max_length=40, blank=True, null=True, verbose_name='入库状态')
    tid = models.CharField(max_length=512, blank=True, null=True, verbose_name='原始订单')
    trade_no = models.CharField(max_length=512, blank=True, null=True, verbose_name='系统订单')
    original_exchange_no = models.CharField(max_length=100, blank=True, null=True, verbose_name='原始退换单号')
    buyer_nick = models.CharField(max_length=100, blank=True, null=True, verbose_name='网名')
    receiver_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='姓名')
    receiver_telno = models.CharField(max_length=40, blank=True, null=True, verbose_name='电话')
    refund_amount = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='退货金额')
    platform_refund = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='平台退款金额')
    offline_refund = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='线下退款金额')
    collection_amount = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='收款金额')
    refund = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='实际退款')
    logistics_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='退回物流公司')
    logistics_no = models.CharField(max_length=100, blank=True, null=True, verbose_name='退回物流单号')
    warehouse = models.CharField(max_length=100, blank=True, null=True, verbose_name='退货仓库')
    data_source = models.CharField(max_length=40, blank=True, null=True, verbose_name='建单方式')
    exchange_remark = models.CharField(max_length=1024, blank=True, null=True, verbose_name='退换说明')
    refuse_reason = models.CharField(max_length=1024, blank=True, null=True, verbose_name='驳回原因')
    mark = models.CharField(max_length=1024, blank=True, null=True, verbose_name='标记')
    creater = models.CharField(max_length=40, blank=True, null=True, verbose_name='建单者')
    remark = models.CharField(max_length=1024, blank=True, null=True, verbose_name='备注')
    created_time = models.DateTimeField(blank=True, null=True, verbose_name='建单时间')
    updated_time = models.DateTimeField(blank=True, null=True, verbose_name='最后修改时间')
    exchange_info = models.CharField(max_length=40, blank=True, null=True, verbose_name='退换信息')
    distributor_exchange_no = models.CharField(max_length=100, blank=True, null=True, verbose_name='分销商退换单号')
    refund_num = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='退款数量')
    distributor_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='分销商名称')
    distributor_no = models.CharField(max_length=100, blank=True, null=True, verbose_name='分销商编号')
    refund_reason = models.CharField(max_length=255, blank=True, null=True, verbose_name='退款原因')
    wms_no = models.CharField(max_length=100, blank=True, null=True, verbose_name='wms业务单号')
    error_msg = models.CharField(max_length=255, blank=True, null=True, verbose_name='错误信息')
    distributor_tid = models.CharField(max_length=100, blank=True, null=True, verbose_name='分销原始单号')

class ShopTarget(models.Model):
    channel = models.CharField(max_length=40, blank=True, null=True, verbose_name='渠道')
    platform = models.CharField(max_length=40, blank=True, null=True, verbose_name='平台')
    principal = models.CharField(max_length=40, blank=True, null=True, verbose_name='负责人')
    shop_name = models.CharField(max_length=100, verbose_name='店铺名称')
    wdt_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='旺店通名称')
    year = models.IntegerField(blank=True, null=True, verbose_name='年份')
    target = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='年度目标')
    product_score = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True, verbose_name='商品体验分')
    logistic_score = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True, verbose_name='物流体验分')
    service_score = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True, verbose_name='服务体验分')
    dsr_date = models.DateField(blank=True, null=True, verbose_name='DSR日期')
