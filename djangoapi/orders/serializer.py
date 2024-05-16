from rest_framework import serializers

from orders.models import orders, salesOutDetails, historySalesOutDetails, OrderDetail, WMSShipData, StockDetail


class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = orders
        fields = '__all__'

class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetail
        fields = '__all__'

class SalesOutDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = salesOutDetails
        fields = '__all__'

class HistorySalesOutDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = historySalesOutDetails
        fields = '__all__'

class StockDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockDetail
        fields = '__all__'

class WMSShipDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = WMSShipData
        fields = '__all__'
