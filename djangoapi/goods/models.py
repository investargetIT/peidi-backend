from django.db import models

# Create your models here.
class PlatformGoods(models.Model):
    '''
    平台货品
    '''
    shop_name = models.CharField(max_length=40, blank=True, null=True, verbose_name='店铺名称')
    goods_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='货品名称')
    spec_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='规格名称')
    outer_id = models.CharField(max_length=40, blank=True, null=True, verbose_name='平台货品编号')
    spec_outer_id = models.CharField(max_length=40, blank=True, null=True, verbose_name='平台规格编码')
    goods_id = models.CharField(max_length=40, blank=True, null=True, verbose_name='货品id')
    spec_id = models.CharField(max_length=40, blank=True, null=True, verbose_name='规格ID')
    is_deleted = models.CharField(max_length=40, blank=True, null=True, verbose_name='活动状态')
    price = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='价格')
    stock_num = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='平台库存')
    hold_stock = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='占用库存')
    hold_stock_type = models.CharField(max_length=40, blank=True, null=True, verbose_name='占用方式')
    is_auto_listing = models.CharField(max_length=40, blank=True, null=True, verbose_name='自动上架')
    is_auto_delisting = models.CharField(max_length=40, blank=True, null=True, verbose_name='自动下架')
    status = models.CharField(max_length=40, blank=True, null=True, verbose_name='状态')
    is_auto_match = models.CharField(max_length=40, blank=True, null=True, verbose_name='自动匹配')
    match_target_type = models.CharField(max_length=40, blank=True, null=True, verbose_name='系统货品', help_text='0未指定，1单品，2组合装')
    disable_syn_until = models.CharField(max_length=40, blank=True, null=True, verbose_name='不同步库存')
    is_disable_syn = models.CharField(max_length=40, blank=True, null=True, verbose_name='是否需要同步')
    last_syn_num = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='最后同步库存量')
    last_syn_time = models.DateTimeField(blank=True, null=True, help_text='最后同步时间')
    disabled_reason = models.CharField(max_length=255, blank=True, null=True, verbose_name='停止同步原因')
    modified = models.DateTimeField(blank=True, null=True, help_text='最后修改时间')
    flag_name = models.TextField(blank=True, null=True, verbose_name='标记')
    syn_platform_allocation_ratio = models.IntegerField(blank=True, null=True, verbose_name='同步平台分配比例')

class SpecGoods(models.Model):
    '''
    单品列表
    '''
    spec_no = models.CharField(max_length=40, blank=True, verbose_name='商家编码')
    goods_no = models.CharField(max_length=40, blank=True, verbose_name='货品编号')
    goods_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='货品名称')
    short_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='货品简称')
    goods_type = models.CharField(max_length=40, blank=True, null=True, verbose_name='分类')
    brand_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='品牌')
    spec_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='规格名称')
    spec_code = models.CharField(max_length=40, blank=True, null=True, verbose_name='规格码')
    barcode = models.CharField(max_length=50, blank=True, null=True, verbose_name='主条码')
    wms_process_mask = models.TextField(blank=True, null=True, verbose_name='仓库流程')
    lowest_price = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='最低价')
    retail_price = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='零售价')
    wholesale_price = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='批发价')
    member_price = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='会员价')
    market_price = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='市场价')
    single_price1 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='单品金额1')
    single_price2 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='单品金额2')
    validity_days = models.IntegerField(blank=True, null=True, verbose_name='有效期天数')
    length = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='长(cm)')
    width = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='宽(cm)')
    height = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='高(cm)')
    weight = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='重量(kg)')
    tax_code = models.CharField(max_length=40, blank=True, null=True, verbose_name='税务编码')
    sn_type = models.CharField(max_length=40, blank=True, null=True, verbose_name='启用序列号')
    goods_label = models.CharField(max_length=255, blank=True, null=True, verbose_name='货品标签',
                                   help_text='货品标签，多个标签用英文逗号隔开')
    large_type = models.CharField(max_length=50, blank=True, null=True, verbose_name='大件类别（拆分）',
                                     help_text='大件类别 0、非大件;1、普通大;2、独立大件（不可和小件一起发）;3、按箱规拆分;-1、非单发件')
    unit_name = models.CharField(max_length=20, blank=True, null=True, verbose_name='基本单位')
    aux_unit_name = models.CharField(max_length=20, blank=True, null=True, verbose_name='辅助单位')
    img_url = models.CharField(max_length=1024, blank=True, null=True, verbose_name='图片URL')
    tax_rate = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='税率')
    spec_modified = models.DateTimeField(blank=True, null=True, help_text='最后修改时间')
    spec_created = models.DateTimeField(blank=True, null=True, help_text='创建时间')


    def save(self, *args, **kwargs):
        super(SpecGoods, self).save(*args, **kwargs)


class SuiteGoodsRec(models.Model):
    '''
    组合装明细
    '''
    suite_name  = models.CharField(max_length=255, blank=True,  null=True, verbose_name='组合装名称')
    spec_no = models.CharField(max_length=40, blank=True, null=True, verbose_name='商家编码')
    barcode = models.CharField(max_length=50, blank=True,  null=True, verbose_name='条码')
    goods_no = models.BigIntegerField(blank=True, null=True, verbose_name='货品编号')
    goods_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='货品名称')
    short_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='货品简称')
    spec_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='规格名称')
    spec_code = models.CharField(max_length=40, blank=True,  null=True, verbose_name='规格码')
    num = models.DecimalField(max_digits=19, decimal_places=4, blank=True, default=0, verbose_name='数量')
    fixed_price = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='固定售价',
                                      help_text='固定售价/单价')
    ratio = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='金额占比')
    is_fixed_price = models.CharField(max_length=40, blank=True,  null=True, verbose_name='是否固定价格')
    modified = models.DateTimeField(blank=True, null=True, help_text='组合装明细修改时间')
    created = models.DateTimeField(blank=True, null=True, help_text='组合装明细创建时间')


