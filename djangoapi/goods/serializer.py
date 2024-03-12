from rest_framework import serializers

from goods.models import PlatformGoods, SpecGoods, SuiteGoodsRec


class PlatformGoodsSerializer(serializers.ModelSerializer):


    class Meta:
        model = PlatformGoods
        fields = '__all__'
        # exclude = ('is_deleted','datasource')

class SpecGoodsSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()

    class Meta:
        model = SpecGoods
        fields = '__all__'

class SuiteGoodsRecSerializer(serializers.ModelSerializer):


    class Meta:
        model = SuiteGoodsRec
        fields = '__all__'

