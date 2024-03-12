import traceback

from django.core.paginator import Paginator, EmptyPage
from django.db import transaction
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from orders.models import orders
from orders.serializer import OrdersSerializer
from utils.customclass import SuccessResponse, PeiDiError, PeiDiErrorResponse, ExceptionResponse


# Create your views here.
class OrdersView(viewsets.ModelViewSet):
    """
    list:获取平台货品列表
    create:新增平台货品
    update:修改平台货品信息（id）
    destroy:删除平台货品（id）
    """
    filter_backends = (DjangoFilterBackend,)
    queryset = orders.objects.all()
    filter_fields = ('tid', 'oid', 'goods_id', 'spec_id', 'goods_no', 'spec_no', 'goods_name', 'spec_name')
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