import json
import traceback
from django.db import transaction
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from utils.customclass import SuccessResponse, PeiDiError, PeiDiErrorResponse, ExceptionResponse
from finance.serializer import TmallRefundSerializer, PddRefundSerializer, JdRefundSerializer, DouyinRefundSerializer, InvoiceSerializer

class TmallRefundView(viewsets.ModelViewSet):

    serializer_class = TmallRefundSerializer
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
                        raise PeiDiError(20071, msg='新增天猫仅退款失败', detail='%s' % serializer.errors)
                return SuccessResponse(serializer.data)
        except PeiDiError as err:
            return PeiDiErrorResponse(err)
        except Exception:
            return ExceptionResponse(traceback.format_exc().split('\n')[-2])

class PddRefundView(viewsets.ModelViewSet):

    serializer_class = PddRefundSerializer
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
                        raise PeiDiError(20071, msg='新增拼多多仅退款失败', detail='%s' % serializer.errors)
                return SuccessResponse(serializer.data)
        except PeiDiError as err:
            return PeiDiErrorResponse(err)
        except Exception:
            return ExceptionResponse(traceback.format_exc().split('\n')[-2])

class JdRefundView(viewsets.ModelViewSet):

    serializer_class = JdRefundSerializer
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
                        raise PeiDiError(20071, msg='新增京东仅退款失败', detail='%s' % serializer.errors)
                return SuccessResponse(serializer.data)
        except PeiDiError as err:
            return PeiDiErrorResponse(err)
        except Exception:
            return ExceptionResponse(traceback.format_exc().split('\n')[-2])

class DouyinRefundView(viewsets.ModelViewSet):

    serializer_class = DouyinRefundSerializer
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
                        raise PeiDiError(20071, msg='新增抖音仅退款失败', detail='%s' % serializer.errors)
                return SuccessResponse(serializer.data)
        except PeiDiError as err:
            return PeiDiErrorResponse(err)
        except Exception:
            return ExceptionResponse(traceback.format_exc().split('\n')[-2])

class InvoiceView(viewsets.ModelViewSet):

    serializer_class = InvoiceSerializer
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
                        raise PeiDiError(20071, msg='新增发票失败', detail='%s' % serializer.errors)
                return SuccessResponse(serializer.data)
        except PeiDiError as err:
            return PeiDiErrorResponse(err)
        except Exception:
            return ExceptionResponse(traceback.format_exc().split('\n')[-2])
