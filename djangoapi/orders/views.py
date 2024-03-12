import traceback

from django.core.paginator import Paginator, EmptyPage
from django.db import transaction
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from orders.models import orders, tradeOrders
from orders.serializer import OrdersSerializer, TradeOrdersSerializer
from utils.customclass import SuccessResponse, PeiDiError, PeiDiErrorResponse, ExceptionResponse


# Create your views here.
class OrdersView(viewsets.ModelViewSet):
    """
    list:获取原始订单列表
    create:新增原始订单
    update:修改原始订单（id）
    destroy:删除原始订单（id）
    """
    filter_backends = (DjangoFilterBackend,)
    queryset = orders.objects.all()
    filter_fields = ('tid',)
    serializer_class = OrdersSerializer

    def list(self, request, *args, **kwargs):
        try:
            page_size = request.GET.get('page_size', 10)
            page_index = request.GET.get('page_index', 1)
            lang = request.GET.get('lang', 'cn')
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
                    raise PeiDiError(20071, msg='新增组合装失败', detail='%s' % serializer.error_messages)
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
                    raise PeiDiError(20071, msg='编辑组合装失败', detail='%s' % serializer.error_messages)
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

class TraderOrdersView(viewsets.ModelViewSet):
    """
    list:获取原始订单明细列表 （子订单）
    create:新增原始明细订单（子订单）
    update:修改原始订单明细（id）（子订单）
    destroy:删除原始订单明细（id）（子订单）
    """
    filter_backends = (DjangoFilterBackend,)
    queryset = tradeOrders.objects.all()
    filter_fields = ('tid', 'oid', 'goods_id', 'spec_id', 'goods_no', 'spec_no', 'goods_name', 'spec_name')
    serializer_class = TradeOrdersSerializer

    def list(self, request, *args, **kwargs):
        try:
            page_size = request.GET.get('page_size', 10)
            page_index = request.GET.get('page_index', 1)
            lang = request.GET.get('lang', 'cn')
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
                    raise PeiDiError(20071, msg='新增组合装失败', detail='%s' % serializer.error_messages)
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
                    raise PeiDiError(20071, msg='编辑组合装失败', detail='%s' % serializer.error_messages)
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