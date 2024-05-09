from rest_framework import serializers
from finance.models import TmallRefund

class TmallRefundSerializer(serializers.ModelSerializer):
    class Meta:
        model = TmallRefund
        fields = '__all__'
