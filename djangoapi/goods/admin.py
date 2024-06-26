from django.contrib import admin
from django.utils.html import format_html
from .models import PlatformGoods, SpecGoods, SuiteGoodsRec, SPU, GoodsSalesTarget
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from import_export.fields import Field

class SpecGoodsResource(resources.ModelResource):
    spec_no = Field(attribute='spec_no', column_name='商家编码')
    goods_no = Field(attribute='goods_no', column_name='货品编号')
    goods_name = Field(attribute='goods_name', column_name='货品名称')
    goods_type = Field(attribute='goods_type', column_name='分类')
    brand_name = Field(attribute='brand_name', column_name='品牌')
    spec_name = Field(attribute='spec_name', column_name='规格名称')
    barcode = Field(attribute='barcode', column_name='主条码')
    validity_days = Field(attribute='validity_days', column_name='有效期天数')
    u9_no = Field(attribute='u9_no', column_name='U9料号')
    tax_rate = Field(attribute='tax_rate', column_name='税率')
    spec_modified = Field(attribute='spec_modified', column_name='修改时间')
    spec_created = Field(attribute='spec_created', column_name='创建时间')
    
    def before_import(self, dataset, **kwargs):
        SpecGoods.objects.all().delete()

    def before_import_row(self, row, **kwargs):
        if not row['税率']:
            row['税率'] = None
            
    class Meta:
        model = SpecGoods

class SuiteGoodsRecResource(resources.ModelResource):
    suite_no = Field(attribute='suite_no', column_name='商家编码')
    suite_name = Field(attribute='suite_name', column_name='组合装名称')
    brand_name = Field(attribute='brand_name', column_name='品牌')
    goods_type = Field(attribute='goods_type', column_name='类别')
    spec_no = Field(attribute='spec_no', column_name='单品商家编码')
    goods_no = Field(attribute='goods_no', column_name='单品货品编号')
    goods_name = Field(attribute='goods_name', column_name='单品名称')
    spec_name = Field(attribute='spec_name', column_name='单品规格名称')
    num = Field(attribute='num', column_name='数量')
    fixed_price = Field(attribute='fixed_price', column_name='固定售价')
    ratio = Field(attribute='ratio', column_name='金额占比')
    is_fixed_price = Field(attribute='is_fixed_price', column_name='是否固定价格')

    def before_import(self, dataset, **kwargs):
        SuiteGoodsRec.objects.all().delete()

    class Meta:
        model = SuiteGoodsRec

# Register your models here.
@admin.register(PlatformGoods)
class PlatformGoodsAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" style="width:70px;"/>'.format(obj.img_url))
    image_tag.short_description = '图片'

    list_display = [
        "shop_name",
        "platform_goods_name",
        "platform_spec_name",
        "platform_spec_no",
        "platform_outer_id",
        "image_tag",
        "platform_spec_outer_id",
        "platform_spec_type",
        "platform_goods_id",
        "platform_spec_id",
        "platform_price",
        "platform_status",
        "match_target_type",
        "spec_no",
        "outer_id",
        "spec_code",
        "spec_name",
        "retail_price",
        "goods_name",
        "goods_type",
        "goods_brand",
        "stock_num",
        "hold_stock",
    ]
    search_fields = ["platform_spec_no"]
    list_filter = ("shop_name",)

@admin.register(SpecGoods)
class SpecGoodsAdmin(ImportExportModelAdmin):
    list_display = [
        "spec_no",
        "goods_no",
        "goods_name",
        # "short_name",
        "goods_type",
        "brand_name",
        "spec_name",
        # "spec_code",
        "barcode",
        # "wms_process_mask",
        # "retail_price",
        # "wholesale_price",
        # "member_price",
        # "market_price",
        # "lowest_price",
        # "single_price1",
        # "single_price2",
        # "validity_days",
        # "length",
        # "width",
        # "height",
        # "weight",
        # "tax_code",
        # "sn_type",
        # "goods_label",
        # "large_type",
        # "unit_name",
        # "aux_unit_name",
        "u9_no",
        # "allow_below_cost_price",
        # "img_url",
        # "aux_box_volume",
        "tax_rate",
        # "remark",
        # "prop2",
        # "prop3",
        # "prop4",
        # "prop5",
        # "prop6",
        "spec_modified",
        "spec_created",
    ]
    search_fields = ["spec_no", "goods_no", "goods_name"]
    # list_filter = ("brand_name", "goods_type")
    resource_classes = [SpecGoodsResource]

@admin.register(SuiteGoodsRec)
class SuiteGoodsRecAdmin(ImportExportModelAdmin):
    list_display = [
        # "img_url",
        "suite_no",
        "suite_name",
        # "suite_short_name",
        # "barcode",
        "brand_name",
        "goods_type",
        # "retail_price",
        # "wholesale_price",
        # "member_price",
        # "market_price",
        # "weight",
        # "remark",
        "goods_name",
        "goods_no",
        "spec_no",
        "spec_name",
        # "ware_code",
        "num",
        "fixed_price",
        "ratio",
        "is_fixed_price",
    ]
    search_fields = ["suite_name", "suite_no", "goods_name", "goods_no", "spec_no"]
    # list_filter = ("brand_name", "goods_type")
    resource_classes = [SuiteGoodsRecResource]

@admin.register(SPU)
class SPUAdmin(admin.ModelAdmin):
    list_display = [
        "brand",
        "spu",
        "suite_no",
        "u9_name",
    ]
    search_fields = ["suite_no", "u9_name"]
    list_filter = ("brand", "spu")

@admin.register(GoodsSalesTarget)
class GoodsSalesTargetAdmin(admin.ModelAdmin):
    list_display = [
        "spu",
        "time",
        "num",
        "amount",
        "created_at",
        "updated_at",
    ]