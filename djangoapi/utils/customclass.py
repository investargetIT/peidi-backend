from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer


class PeiDiError(Exception):
    def __init__(self, code, msg, detail=None):
        self.code = code
        self.msg = msg
        self.detail_msg = detail if detail else msg

class SuccessResponse(HttpResponse):

    def __init__(self, result, msg=None, **kwargs):
        data = {'code': 1000, 'errormsg': msg, 'result': result, 'detail': msg}
        content = JSONRenderer().render(data=data)
        kwargs['content_type'] = 'application/json; charset=utf-8'
        super(SuccessResponse, self).__init__(content , **kwargs)


class PeiDiErrorResponse(HttpResponse):

    def __init__(self, peidierr, **kwargs):
        data = {'code': peidierr.code, 'errormsg': peidierr.msg, 'result': None, 'detail': peidierr.detail_msg}
        content = JSONRenderer().render(data=data)
        kwargs['content_type'] = 'application/json; charset=utf-8'
        super(PeiDiErrorResponse, self).__init__(content, **kwargs)


class ExceptionResponse(HttpResponse):

    def __init__(self, msg, **kwargs):
        data = {'code': 9999, 'errormsg': '系统错误，请联系工作人员', 'result': None, 'detail': msg}
        content = JSONRenderer().render(data=data)
        kwargs['content_type'] = 'application/json; charset=utf-8'
        super(ExceptionResponse, self).__init__(content, **kwargs)


