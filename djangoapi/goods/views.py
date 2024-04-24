import datetime
import traceback

from django.core.paginator import Paginator, EmptyPage
from django.db import transaction
from django.shortcuts import render
from django_filters import FilterSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from goods.models import PlatformGoods, SpecGoods, SuiteGoodsRec, SPU
from goods.serializer import PlatformGoodsSerializer, SpecGoodsSerializer, SuiteGoodsRecSerializer , SPUSerializer
from utils.customclass import SuccessResponse, PeiDiError, PeiDiErrorResponse, ExceptionResponse


# Create your views here.


class PlatformGoodsView(viewsets.ModelViewSet):
    """
    list:获取平台货品列表
    create:新增平台货品
    update:修改平台货品信息（id）
    destroy:删除平台货品（id）
    """
    filter_backends = (DjangoFilterBackend,)
    queryset = PlatformGoods.objects.all()
    filterset_fields = ('id', 'goods_name','spec_name')
    serializer_class = PlatformGoodsSerializer

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
                    raise PeiDiError(20071, msg='新增平台货品失败', detail='%s' % serializer.error_messages)
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
                    raise PeiDiError(20071, msg='编辑平台货品失败', detail='%s' % serializer.error_messages)
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



class SpecGoodsView(viewsets.ModelViewSet):
    """
    list:获取单品列表
    create:新增单品
    update:修改单品信息（id）
    destroy:删除单品（id）
    """
    filter_backends = (DjangoFilterBackend,)
    queryset = SpecGoods.objects.all()
    filterset_fields = ('id', 'spec_no', 'goods_no', 'goods_name', 'spec_name', 'spec_code')
    serializer_class = SpecGoodsSerializer

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
                    raise PeiDiError(20071, msg='新增单品失败', detail='%s' % serializer.error_messages)
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
                    raise PeiDiError(20071, msg='编辑单品失败', detail='%s' % serializer.error_messages)
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


class SuiteGoodsRecView(viewsets.ModelViewSet):
    """
    list:获取平台货品列表
    create:新增平台货品
    update:修改平台货品信息（id）
    destroy:删除平台货品（id）
    """
    filter_backends = (DjangoFilterBackend,)
    queryset = SuiteGoodsRec.objects.all()
    filterset_fields = ('id', 'goods_name','spec_name')
    serializer_class = SuiteGoodsRecSerializer

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
                    raise PeiDiError(20071, msg='新增组合装失败', detail='%s' % serializer.errors)
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


class SPUView(viewsets.ModelViewSet):
    """
    list:获取SPU列表
    create:新增SPU
    update:修改SPU信息（id）
    destroy:删除SPU（id）
    """
    filter_backends = (DjangoFilterBackend,)
    queryset = SPU.objects.all()
    filterset_fields = ('id', 'brand', 'suite_no', 'spu', 'u9_name')
    serializer_class = SPUSerializer

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
                    raise PeiDiError(20071, msg='新增SPU失败', detail='%s' % serializer.errors)
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
                    raise PeiDiError(20071, msg='编辑SPU失败', detail='%s' % serializer.error_messages)
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