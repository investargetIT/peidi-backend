from django.contrib import admin
from django.utils.html import format_html
from .models import PlatformGoods, SpecGoods, SuiteGoodsRec, SPU

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
class SpecGoodsAdmin(admin.ModelAdmin):
    list_display = [
        "spec_no",
        "goods_no",
        "goods_name",
        "short_name",
        "goods_type",
        "brand_name",
        "spec_name",
        "spec_code",
        "barcode",
        "wms_process_mask",
        "retail_price",
        "wholesale_price",
        "member_price",
        "market_price",
        "lowest_price",
        "single_price1",
        "single_price2",
        "validity_days",
        "length",
        "width",
        "height",
        "weight",
        "tax_code",
        "sn_type",
        "goods_label",
        "large_type",
        "unit_name",
        "aux_unit_name",
        "u9_no",
        "allow_below_cost_price",
        "img_url",
        "aux_box_volume",
        "tax_rate",
        "remark",
        "prop2",
        "prop3",
        "prop4",
        "prop5",
        "prop6",
        "spec_modified",
        "spec_created",
    ]
    search_fields = ["spec_no", "goods_no", "goods_name"]
    list_filter = ("brand_name", "goods_type")

@admin.register(SuiteGoodsRec)
class SuiteGoodsRecAdmin(admin.ModelAdmin):
    list_display = [
        # "img_url",
        "suite_no",
        "suite_name",
        "suite_short_name",
        "barcode",
        "brand_name",
        "goods_type",
        # "retail_price",
        # "wholesale_price",
        # "member_price",
        # "market_price",
        "weight",
        "remark",
        "goods_name",
        "goods_no",
        "spec_no",
        "spec_name",
        "ware_code",
        "num",
        "fixed_price",
        "ratio",
        "is_fixed_price",
    ]
    search_fields = ["suite_name", "suite_no", "goods_name", "goods_no", "spec_no"]
    list_filter = ("brand_name", "goods_type")

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
