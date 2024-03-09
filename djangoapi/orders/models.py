from django.db import models

# Create your models here.



class orders(models.Model):
    tid = models.CharField(max_length=40, blank=True, null=True, verbose_name='原始单号')
    oid = models.CharField(max_length=40, blank=True, null=True, verbose_name='原始子订单号')
    status = models.CharField(max_length=40, blank=True, null=True, verbose_name='状态')
    process_status = models.CharField(max_length=40, blank=True, null=True, verbose_name='处理状态')
    refund_status = models.CharField(max_length=40, blank=True, null=True, verbose_name='退款状态')
    order_type = models.CharField(max_length=40, blank=True, null=True, verbose_name='子订单类型')
    goods_id = models.CharField(max_length=40, blank=True, null=True, verbose_name='平台货品id')
    spec_id = models.CharField(max_length=40, blank=True, null=True, verbose_name='平台规格id')
    goods_no = models.CharField(max_length=40, blank=True, null=True, verbose_name='货品编号')
    spec_no = models.CharField(max_length=40, blank=True, null=True, verbose_name='规格编码')
    goods_name = models.CharField(max_length=40, blank=True, null=True, verbose_name='货品名称')
    spec_name = models.CharField(max_length=40, blank=True, null=True, verbose_name='规格名称')
    num = models.IntegerField(blank=True, null=True, verbose_name='数量')
    price = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='单价')
    adjust_amount = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='调整')
    discount = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='优惠')
    total_amount = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='总价')
    share_discount = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='分摊优惠')
    share_amount = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='分摊后应收')
    refund_amount = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='退款金额')
    refund_id = models.CharField(max_length=40, blank=True, null=True, verbose_name='退款单编号')
    end_time = models.DateTimeField(blank=True, null=True, help_text='子单完成时间')
    modified = models.DateTimeField(blank=True, null=True, help_text='修改时间')
    created = models.DateTimeField(blank=True, null=True, help_text='创建时间')
