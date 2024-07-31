from rest_framework import serializers
from finance.models import TmallRefund, PddRefund, JdRefund, DouyinRefund, Invoice, GoodsSalesSummary, FinanceSalesAndInvoice, PDMaterialNOList

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
        fields = [
            'start_date',
            'end_date',
            'spec_no',
            'major_supplier',
            'shop_name',
            'brand_name',
            'goods_type',
            'goods_no',
            'goods_name',
            'spec_name',
            'goods_category',
            'average_price',
            'retail_price',
            'ship_num',
            'return_num',
            'return_count_num',
            'sales_num',
            'ship_amount',
            'sales_amount',
            'sales_amount_unknown_cost',
            'return_amount',
            'actual_sales_amount',
            'gift_sales_num',
            'post_amount',
            'post_cost',
            'ship_refund_num',
            'ship_refund_amount',
            'abnormal_warehouse_sales_num',
            'refund_stockin',
        ]

class FinanceSalesAndInvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinanceSalesAndInvoice
        fields = '__all__'

class PDMaterialNOListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PDMaterialNOList
        fields = '__all__'
