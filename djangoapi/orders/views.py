import json
import traceback

from django.core.paginator import Paginator, EmptyPage
from django.core.serializers import serialize
from django.core.serializers.json import DjangoJSONEncoder
from django.db import transaction, connection
from django.db.models import Sum, Count
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from django_filters import rest_framework as filters
from orders.models import orders, tradeOrders
from orders.serializer import OrdersSerializer, TradeOrdersSerializer
from utils.customclass import SuccessResponse, PeiDiError, PeiDiErrorResponse, ExceptionResponse


# Create your views here.
class OrdersFilter(filters.FilterSet):
    pay_time = filters.DateTimeFromToRangeFilter()
    class Meta:
        model = orders
        fields = ('id', 'tid', 'buyer_nick', 'receiver_area', 'trade_status', 'pay_status', 'process_status')


class OrdersView(viewsets.ModelViewSet):
    """
    list:获取原始订单列表
    create:新增原始订单
    update:修改原始订单（id）
    destroy:删除原始订单（id）
    """
    filter_backends = (DjangoFilterBackend,)
    queryset = orders.objects.all()
    filterset_class = OrdersFilter
    serializer_class = OrdersSerializer

    def list(self, request, *args, **kwargs):
        try:
            page_size = request.GET.get('page_size', 10)
            page_index = request.GET.get('page_index', 1)
            queryset = self.filter_queryset(self.get_queryset())
            try:
                count = queryset.count()
                queryset = Paginator(queryset, page_size)
                queryset = queryset.page(page_index)
            except EmptyPage:
                return SuccessResponse({'count': 0, 'data': []})
            serializer = self.serializer_class(queryset, many=True)
            return SuccessResponse({'count': count, 'data': serializer.data})
        except PeiDiError as err:
            return PeiDiErrorResponse(err)
        except Exception:
            return ExceptionResponse(traceback.format_exc().split('\n')[-2])

    def create(self, request, *args, **kwargs):
        try:
            data = request.data
            with transaction.atomic():
                if isinstance(data, list):
                    serializer = self.serializer_class(data=data, many=True)
                else:
                    serializer = self.serializer_class(data=data)
                if serializer.is_valid():
                    serializer.save()
                else:
                    raise PeiDiError(20071, msg='新增原始订单失败', detail='%s' % serializer.errors)
                return SuccessResponse(serializer.data)
        except PeiDiError as err:
            return PeiDiErrorResponse(err)
        except Exception:
            return ExceptionResponse(traceback.format_exc().split('\n')[-2])

    def update(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            data = request.data

            with transaction.atomic():
                serializer = self.serializer_class(instance, data=data)
                if serializer.is_valid():
                    serializer.save()
                else:
                    raise PeiDiError(20071, msg='编辑原始订单失败', detail='%s' % serializer.errors)
                return SuccessResponse(serializer.data)
        except PeiDiError as err:
            return PeiDiErrorResponse(err)
        except Exception:
            return ExceptionResponse(traceback.format_exc().split('\n')[-2])


    def destroy(self, request, *args, **kwargs):
        try:

            instance = self.get_object()

            with transaction.atomic():
                instance.delete()
                return SuccessResponse({'isdeleted': 'success'})
        except PeiDiError as err:
            return PeiDiErrorResponse(err)
        except Exception:
            return ExceptionResponse(traceback.format_exc().split('\n')[-2])

    def testGroupByCount(self, request, *args, **kwargs):
        try:
            queryset = self.filter_queryset(self.get_queryset())
            queryset = queryset.values('buyer_nick', 'receiver_area').annotate(
                count=Count('pay_id')).order_by('-count')[:5]
            serializer = json.dumps(list(queryset), cls=DjangoJSONEncoder)
            print(json.loads(serializer))
            return SuccessResponse(json.loads(serializer))
        except PeiDiError as err:
            return PeiDiErrorResponse(err)
        except Exception:
            return ExceptionResponse(traceback.format_exc().split('\n')[-2])
    def testGroupByAmount(self, request, *args, **kwargs):
        try:
            queryset = self.filter_queryset(self.get_queryset())
            queryset = queryset.values('buyer_nick', 'receiver_area').annotate(
                sum_amount=Sum('consumer_amount')).order_by('-sum_amount')[:5]
            serializer = json.dumps(list(queryset), cls=DjangoJSONEncoder)
            print(json.loads(serializer))
            return SuccessResponse(json.loads(serializer))
        except PeiDiError as err:
            return PeiDiErrorResponse(err)
        except Exception:
            return ExceptionResponse(traceback.format_exc().split('\n')[-2])


    def getCustomerPurchaseCounts(self, request, *args, **kwargs):
        try:
            with connection.cursor() as cursor:
                pay_time_start = request.data['start']
                pay_time_end = request.data['end']
                cursor.callproc('GetCustomerPurchaseCounts', (pay_time_start, pay_time_end))
                row = cursor.fetchall()
                return SuccessResponse(str(row))
        except Exception:
            return ExceptionResponse(traceback.format_exc().split('\n')[-2])
    
    def getShopSalesAmount(self, request, *args, **kwargs):
        try:
            with connection.cursor() as cursor:
                pay_time_start = request.data['start']
                pay_time_end = request.data['end']
                cursor.callproc('GetShopSalesAmount', (pay_time_start, pay_time_end))
                row = cursor.fetchall()
                return SuccessResponse(str(row))
        except Exception:
            return ExceptionResponse(traceback.format_exc().split('\n')[-2])


class TraderOrdersView(viewsets.ModelViewSet):
    """
    list:获取原始订单明细列表 （子订单）
    create:新增原始明细订单（子订单）
    update:修改原始订单明细（id）（子订单）
    destroy:删除原始订单明细（id）（子订单）
    """
    filter_backends = (DjangoFilterBackend,)
    queryset = tradeOrders.objects.all()
    filterset_fields = ('id', 'tid', 'oid', 'goods_id', 'spec_id', 'goods_no', 'spec_no', 'goods_name', 'spec_name')
    serializer_class = TradeOrdersSerializer

    def list(self, request, *args, **kwargs):
        try:
            page_size = request.GET.get('page_size', 10)
            page_index = request.GET.get('page_index', 1)
            queryset = self.filter_queryset(self.get_queryset())
            try:
                count = queryset.count()
                queryset = Paginator(queryset, page_size)
                queryset = queryset.page(page_index)
            except EmptyPage:
                return SuccessResponse({'count': 0, 'data': []})
            serializer = self.serializer_class(queryset, many=True)
            return SuccessResponse({'count': count, 'data': serializer.data})
        except PeiDiError as err:
            return PeiDiErrorResponse(err)
        except Exception:
            return ExceptionResponse(traceback.format_exc().split('\n')[-2])

    def create(self, request, *args, **kwargs):
        try:
            data = request.data
            with transaction.atomic():
                serializer = self.serializer_class(data=data)
                if serializer.is_valid():
                    serializer.save()
                else:
                    raise PeiDiError(20071, msg='新增原始订单子单失败', detail='%s' % serializer.errors)
                return SuccessResponse(serializer.data)
        except PeiDiError as err:
            return PeiDiErrorResponse(err)
        except Exception:
            return ExceptionResponse(traceback.format_exc().split('\n')[-2])

    def update(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            data = request.data
            with transaction.atomic():
                serializer = self.serializer_class(instance, data=data)
                if serializer.is_valid():
                    serializer.save()
                else:
                    raise PeiDiError(20071, msg='编辑原始订单子单失败', detail='%s' % serializer.errors)
                return SuccessResponse(serializer.data)
        except PeiDiError as err:
            return PeiDiErrorResponse(err)
        except Exception:
            return ExceptionResponse(traceback.format_exc().split('\n')[-2])


    def destroy(self, request, *args, **kwargs):
        try:

            instance = self.get_object()

            with transaction.atomic():
                instance.delete()
                return SuccessResponse({'isdeleted': 'success'})
        except PeiDiError as err:
            return PeiDiErrorResponse(err)
        except Exception:
            return ExceptionResponse(traceback.format_exc().split('\n')[-2])