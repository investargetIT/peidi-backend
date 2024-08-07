from rest_framework import serializers

from goods.models import PlatformGoods, SpecGoods, SuiteGoodsRec, SPU


class PlatformGoodsSerializer(serializers.ModelSerializer):


    class Meta:
        model = PlatformGoods
        fields = '__all__'
        # exclude = ('is_deleted','datasource')

class SpecGoodsSerializer(serializers.ModelSerializer):


    class Meta:
        model = SpecGoods
        fields = [
            'spec_no',
            'goods_no',
            'goods_name',
            'goods_type',
            'brand_name',
            'spec_name',
            'barcode',
            'validity_days',
            'u9_no',
            'tax_rate',
            'spec_modified',
            'spec_created',
        ]

class SuiteGoodsRecSerializer(serializers.ModelSerializer):


    class Meta:
        model = SuiteGoodsRec
        fields = [
            'suite_no',
            'suite_name',
            'brand_name',
            'goods_type',
            'spec_no',
            'goods_no',
            'goods_name',
            'spec_name',
            'num',
            'fixed_price',
            'ratio',
            'is_fixed_price'
        ]

class SPUSerializer(serializers.ModelSerializer):


    class Meta:
        model = SPU
        fields = '__all__'