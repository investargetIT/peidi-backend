import json
import traceback

from django.core.cache import cache
from django.core.paginator import Paginator, EmptyPage
from django.core.serializers import serialize
from django.core.serializers.json import DjangoJSONEncoder
from django.db import transaction, connection, IntegrityError
from django.db.models import Sum, Count
from django.shortcuts import render
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django_filters import rest_framework as filters
from orders.models import orders, salesOutDetails, historySalesOutDetails
from orders.serializer import OrdersSerializer, SalesOutDetailsSerializer, HistorySalesOutDetailsSerializer, OrderDetailSerializer, StockDetailSerializer, WMSShipDataSerializer
from utils.customclass import SuccessResponse, PeiDiError, PeiDiErrorResponse, ExceptionResponse

from utils.util import read_from_cache, write_to_cache, getMysqlProcessResponseWithRedis


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
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

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
            key = 'GetCustomerPurchaseCounts'
            res_data = read_from_cache(key)
            if not res_data:
                queryset = self.filter_queryset(self.get_queryset())
                queryset = queryset.values('buyer_nick', 'receiver_area').annotate(
                    count=Count('pay_id')).order_by('-count')[:5]
                serializer = json.dumps(list(queryset), cls=DjangoJSONEncoder)
                res_data = json.loads(serializer)
                write_to_cache(key, res_data)
            return SuccessResponse(res_data)
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
            pay_time_start = request.data['start']
            pay_time_end = request.data['end']
            proc_name = 'GetCustomerPurchaseCounts'
            key = '{}{}{}'.format(proc_name, pay_time_start, pay_time_end)
            res_data = getMysqlProcessResponseWithRedis(redis_key=key, proc_name=proc_name,
                                                        args=(pay_time_start, pay_time_end))
            return SuccessResponse(res_data)
        except Exception:
            return ExceptionResponse(traceback.format_exc().split('\n')[-2])
    
    def getShopSalesAmount(self, request, *args, **kwargs):
        try:
            pay_time_start = request.data['start']
            pay_time_end = request.data['end']
            proc_name = 'GetShopSalesAmount'
            key = '{}{}{}'.format(proc_name, pay_time_start, pay_time_end)
            res_data = getMysqlProcessResponseWithRedis(redis_key=key, proc_name=proc_name,
                                                        args=(pay_time_start, pay_time_end))
            return SuccessResponse(res_data)
        except Exception:
            return ExceptionResponse(traceback.format_exc().split('\n')[-2])

class OrderDetailsView(viewsets.ModelViewSet):

    serializer_class = OrderDetailSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]    

    def create(self, request, *args, **kwargs):
        try:
            datas = request.data
            if isinstance(datas, list):
                success, fail = [], []
                for data in datas:
                    try:
                        with transaction.atomic():
                            serializer = self.serializer_class(data=data)
                            if serializer.is_valid():
                                serializer.save()
                                success.append(serializer.data)
                            else:
                                fail.append({'data': data, 'errmsg': serializer.errors})
                    except Exception as err:
                        fail.append({'data': data, 'errmsg': str(err)})
                return SuccessResponse({'success': success, 'fail': fail})
            else:
                with transaction.atomic():
                    serializer = self.serializer_class(data=datas)
                    if serializer.is_valid():
                        serializer.save()
                    else:
                        raise PeiDiError(20071, msg='新增订单明细失败', detail='%s' % serializer.errors)
                return SuccessResponse(serializer.data)
        except PeiDiError as err:
            return PeiDiErrorResponse(err)
        except Exception:
            return ExceptionResponse(traceback.format_exc().split('\n')[-2])  

class SalesOutDetailsView(viewsets.ModelViewSet):
    """
    list:获取销售出库明细列表
    create:新增销售出库明细订单
    update:修改销售出库明细（id）
    destroy:删除销售出库明细（id）
    """
    filter_backends = (DjangoFilterBackend, OrderingFilter,)
    queryset = salesOutDetails.objects.all()
    filterset_fields = ('id', 'tid', 'oid', 'stockout_no', 'goods_no', 'spec_no')
    serializer_class = SalesOutDetailsSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    ordering_fields = ['trade_time']
    ordering = ['-trade_time']

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
            datas = request.data
            if isinstance(datas, list):
                success, fail = [], []
                for data in datas:
                    try:
                        with transaction.atomic():
                            serializer = self.serializer_class(data=data)
                            if serializer.is_valid():
                                serializer.save()
                                success.append(serializer.data)
                            else:
                                fail.append({'data': data, 'errmsg': serializer.errors})
                    except Exception as err:
                        fail.append({'data': data, 'errmsg': str(err)})
                return SuccessResponse({'success': success, 'fail': fail})
            else:
                with transaction.atomic():
                    serializer = self.serializer_class(data=datas)
                    if serializer.is_valid():
                        serializer.save()
                    else:
                        raise PeiDiError(20071, msg='新增销售出库失败', detail='%s' % serializer.errors)
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
                    raise PeiDiError(20071, msg='编辑销售出库失败', detail='%s' % serializer.errors)
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

class HistorySalesOutDetailsView(viewsets.ModelViewSet):
    """
    list:获取历史销售出库明细列表
    create:新增历史销售出库明细订单
    update:修改历史销售出库明细（id）
    destroy:删除历史销售出库明细（id）
    """
    filter_backends = (DjangoFilterBackend,)
    queryset = historySalesOutDetails.objects.all()
    filterset_fields = ('id', 'tid', 'oid', 'stockout_no', 'goods_no', 'spec_no')
    serializer_class = HistorySalesOutDetailsSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

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
            datas = request.data
            if isinstance(datas, list):
                success, fail = [], []
                for data in datas:
                    try:
                        with transaction.atomic():
                            serializer = self.serializer_class(data=data)
                            if serializer.is_valid():
                                serializer.save()
                                success.append(serializer.data)
                            else:
                                fail.append({'data': data, 'errmsg': serializer.errors})
                    except Exception as err:
                        fail.append({'data': data, 'errmsg': str(err)})
                return SuccessResponse({'success': success, 'fail': fail})
            else:
                with transaction.atomic():
                    serializer = self.serializer_class(data=datas)
                    if serializer.is_valid():
                        serializer.save()
                    else:
                        raise PeiDiError(20071, msg='新增历史销售出库失败', detail='%s' % serializer.errors)
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
                    raise PeiDiError(20071, msg='编辑历史销售出库失败', detail='%s' % serializer.errors)
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

class StockDetailView(viewsets.ModelViewSet):

    serializer_class = StockDetailSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]    

    def create(self, request, *args, **kwargs):
        try:
            datas = request.data
            if isinstance(datas, list):
                success, fail = [], []
                for data in datas:
                    try:
                        with transaction.atomic():
                            serializer = self.serializer_class(data=data)
                            if serializer.is_valid():
                                serializer.save()
                                success.append(serializer.data)
                            else:
                                fail.append({'data': data, 'errmsg': serializer.errors})
                    except Exception as err:
                        fail.append({'data': data, 'errmsg': str(err)})
                return SuccessResponse({'success': success, 'fail': fail})
            else:
                with transaction.atomic():
                    serializer = self.serializer_class(data=datas)
                    if serializer.is_valid():
                        serializer.save()
                    else:
                        raise PeiDiError(20071, msg='新增库存明细失败', detail='%s' % serializer.errors)
                return SuccessResponse(serializer.data)
        except PeiDiError as err:
            return PeiDiErrorResponse(err)
        except Exception:
            return ExceptionResponse(traceback.format_exc().split('\n')[-2])

class WMSShipDataView(viewsets.ModelViewSet):

    serializer_class = WMSShipDataSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]    

    def create(self, request, *args, **kwargs):
        try:
            datas = request.data
            if isinstance(datas, list):
                success, fail = [], []
                for data in datas:
                    try:
                        with transaction.atomic():
                            serializer = self.serializer_class(data=data)
                            if serializer.is_valid():
                                serializer.save()
                                success.append(serializer.data)
                            else:
                                fail.append({'data': data, 'errmsg': serializer.errors})
                    except Exception as err:
                        fail.append({'data': data, 'errmsg': str(err)})
                return SuccessResponse({'success': success, 'fail': fail})
            else:
                with transaction.atomic():
                    serializer = self.serializer_class(data=datas)
                    if serializer.is_valid():
                        serializer.save()
                    else:
                        raise PeiDiError(20071, msg='新增WMS发货数据失败', detail='%s' % serializer.errors)
                return SuccessResponse(serializer.data)
        except PeiDiError as err:
            return PeiDiErrorResponse(err)
        except Exception:
            return ExceptionResponse(traceback.format_exc().split('\n')[-2])
