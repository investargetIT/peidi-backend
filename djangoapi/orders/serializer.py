from rest_framework import serializers

from djangoapi.orders.models import orders


class OrdersSerializer(serializers.ModelSerializer):


    class Meta:
        model = orders
        fields = '__all__'