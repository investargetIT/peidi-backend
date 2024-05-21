from rest_framework import serializers
from finance.models import TmallRefund, PddRefund, JdRefund, DouyinRefund, Invoice, GoodsSalesSummary

class TmallRefundSerializer(serializers.ModelSerializer):
    class Meta:
        model = TmallRefund
        fields = '__all__'

class PddRefundSerializer(serializers.ModelSerializer):
    class Meta:
        model = PddRefund
        fields = '__all__'

class JdRefundSerializer(serializers.ModelSerializer):
    class Meta:
        model = JdRefund
        fields = '__all__'

class DouyinRefundSerializer(serializers.ModelSerializer):
    class Meta:
        model = DouyinRefund
        fields = '__all__'

class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = '__all__'

class GoodsSalesSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsSalesSummary
        fields = '__all__'
