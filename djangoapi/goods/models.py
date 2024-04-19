from django.db import models

# Create your models here.
class PlatformGoods(models.Model):
    '''
    平台货品
    '''
    shop_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='店铺名称')
    platform_goods_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="平台货品名称")
    platform_spec_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='平台规格名称')
    platform_spec_no = models.CharField(max_length=100, blank=True, null=True, verbose_name='平台商家编码')
    platform_outer_id = models.CharField(max_length=100, blank=True, null=True, verbose_name='平台货品编号')
    img_url = models.CharField(max_length=1024, blank=True, null=True, verbose_name='图片链接')
    platform_spec_outer_id = models.CharField(max_length=100, blank=True, null=True, verbose_name='平台规格编码')
    platform_spec_type = models.CharField(max_length=100, blank=True, null=True, verbose_name='平台类目')
    platform_goods_id = models.CharField(max_length=100, blank=True, null=True, verbose_name='平台货品id')
    platform_spec_id = models.CharField(max_length=100, blank=True, null=True, verbose_name='平台规格ID')
    platform_price = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='平台价格')
    platform_status = models.CharField(max_length=100, blank=True, null=True, verbose_name='平台状态')
    match_target_type = models.CharField(max_length=100, blank=True, null=True, verbose_name='是否组合装', help_text='0未指定，1单品，2组合装')
    spec_no = models.CharField(max_length=100, blank=True, null=True, verbose_name='商家编码')
    outer_id = models.CharField(max_length=100, blank=True, null=True, verbose_name='货品编号')
    spec_code = models.CharField(max_length=100, blank=True, null=True, verbose_name='规格码')
    spec_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='规格名称')
    retail_price = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='零售价')
    goods_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='货品名称')
    goods_type = models.CharField(max_length=100, blank=True, null=True, verbose_name='货品分类')
    goods_brand = models.CharField(max_length=100, blank=True, null=True, verbose_name='货品品牌')
    stock_num = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='平台库存')
    hold_stock = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='平台库存占用量')


class SpecGoods(models.Model):
    '''
    单品列表
    '''
    spec_no = models.CharField(max_length=100, blank=True, null=True, verbose_name='商家编码')
    goods_no = models.CharField(max_length=100, blank=True, null=True, verbose_name='货品编号')
    goods_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='货品名称')
    short_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='简称')
    goods_type = models.CharField(max_length=100, blank=True, null=True, verbose_name='分类')
    brand_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='品牌')
    spec_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='规格名称')
    spec_code = models.CharField(max_length=100, blank=True, null=True, verbose_name='规格码')
    barcode = models.CharField(max_length=100, blank=True, null=True, verbose_name='主条码')
    wms_process_mask = models.TextField(blank=True, null=True, verbose_name='仓库流程')
    retail_price = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='零售价')
    wholesale_price = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='批发价')
    member_price = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='会员价')
    market_price = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='市场价')
    lowest_price = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='最低价')
    single_price1 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='单品金额1')
    single_price2 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='单品金额2')
    validity_days = models.IntegerField(blank=True, null=True, verbose_name='有效期天数')
    length = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='长(cm)')
    width = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='宽(cm)')
    height = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='高(cm)')
    weight = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='重量(kg)')
    tax_code = models.CharField(max_length=100, blank=True, null=True, verbose_name='税务编码')
    sn_type = models.CharField(max_length=100, blank=True, null=True, verbose_name='启用序列号')
    goods_label = models.CharField(max_length=255, blank=True, null=True, verbose_name='货品标签',
                                   help_text='货品标签，多个标签用英文逗号隔开')
    large_type = models.CharField(max_length=100, blank=True, null=True, verbose_name='大件类别（拆分）',
                                     help_text='大件类别 0、非大件;1、普通大;2、独立大件（不可和小件一起发）;3、按箱规拆分;-1、非单发件')
    unit_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='基本单位')
    aux_unit_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='辅助单位')
    u9_no = models.CharField(max_length=100, blank=True, null=True, verbose_name='U9料号')
    allow_below_cost_price = models.CharField(max_length=100, blank=True, null=True, verbose_name='允许低于成本价')
    img_url = models.CharField(max_length=1024, blank=True, null=True, verbose_name='图片URL')
    aux_box_volume = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='辅助箱体积')
    tax_rate = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='税率')
    remark = models.TextField(blank=True, null=True, verbose_name='备注')
    prop2 = models.TextField(blank=True, null=True, verbose_name='单品属性2')
    prop3 = models.TextField(blank=True, null=True, verbose_name='单品属性3')
    prop4 = models.TextField(blank=True, null=True, verbose_name='单品属性4')
    prop5 = models.TextField(blank=True, null=True, verbose_name='单品属性5')
    prop6 = models.TextField(blank=True, null=True, verbose_name='单品属性6')
    spec_modified = models.DateTimeField(blank=True, null=True, help_text='修改时间')
    spec_created = models.DateTimeField(blank=True, null=True, help_text='创建时间')


    def save(self, *args, **kwargs):
        super(SpecGoods, self).save(*args, **kwargs)


class SuiteGoodsRec(models.Model):
    '''
    组合装明细
    '''
    img_url = models.CharField(max_length=1024, blank=True, null=True, verbose_name='图片链接')
    suite_name = models.CharField(max_length=255, blank=True,  null=True, verbose_name='组合装名称')
    suite_short_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='组合装简称')
    suite_no = models.CharField(max_length=100, blank=True, null=True, verbose_name='组合装商家编码')
    barcode = models.CharField(max_length=100, blank=True, null=True, verbose_name='条码')
    brand_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='品牌')
    goods_type = models.CharField(max_length=100, blank=True, null=True, verbose_name='类别')
    retail_price = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='零售价')
    wholesale_price = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='批发价')
    member_price = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='会员价')
    market_price = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='市场价')
    weight = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='重量(kg)')
    remark = models.TextField(blank=True, null=True, verbose_name='备注')
    goods_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='单品名称')
    goods_no = models.CharField(max_length=100, blank=True, null=True, verbose_name='单品货品编号')
    spec_no = models.CharField(max_length=100, blank=True, null=True, verbose_name='单品商家编码')
    spec_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='单品规格名称')
    ware_code = models.CharField(max_length=100, blank=True,  null=True, verbose_name='外部编码')
    num = models.DecimalField(max_digits=19, decimal_places=4, blank=True, default=0, verbose_name='数量')
    fixed_price = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='固定售价',
                                      help_text='固定售价/单价')
    ratio = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='金额占比')
    is_fixed_price = models.CharField(max_length=100, blank=True, null=True, verbose_name='是否固定价格')

