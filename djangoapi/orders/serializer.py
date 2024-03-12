from rest_framework import serializers

from orders.models import orders, tradeOrders


class OrdersSerializer(serializers.ModelSerializer):


    class Meta:
        model = orders
        fields = '__all__'

class TradeOrdersSerializer(serializers.ModelSerializer):


    class Meta:
        model = tradeOrders
        fields = '__all__'