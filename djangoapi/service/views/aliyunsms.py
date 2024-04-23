#coding=utf-8
import datetime
import json
import os
import traceback

from alibabacloud_dysmsapi20170525.models import SendSmsResponse
from rest_framework.decorators import api_view

from service.models import MobileAuthCode
from alibabacloud_dysmsapi20170525.client import Client as Dysmsapi20170525Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dysmsapi20170525 import models as dysmsapi_20170525_models
from utils.customclass import PeiDiError, SuccessResponse, ExceptionResponse, PeiDiErrorResponse


def sendSms(mobile, sign_name, template_code, template_param):
    try:
        config = open_api_models.Config(
            access_key_id=os.environ['ALIYUNSMS_KEY'],
            access_key_secret=os.environ['ALIYUNSMS_SECRET'],
            endpoint='dysmsapi.aliyuncs.com'
        )
        client = Dysmsapi20170525Client(config)
        send_sms_request = dysmsapi_20170525_models.SendSmsRequest(
            phone_numbers=mobile,
            sign_name=sign_name,
            template_code=template_code,
            template_param=template_param
        )
        res = client.send_sms(send_sms_request)
        print('正常请求', res.body.message)
        return res
    except Exception as error:
        print('异常报错请求', error)
        return error


@api_view(['POST'])
def sendALiYunSmsCode(request):
    try:
        if 'HTTP_X_FORWARDED_FOR' in request.META:
            ip = request.META['HTTP_X_FORWARDED_FOR']
        else:
            ip = request.META['REMOTE_ADDR']
        sign_name = 'Peidi验证码'
        template_code = 'SMS_465348269'
        mobile = request.data.get('mobile')  # 目标手机号
        areacode = request.data.get('areacode', '86')
        now = datetime.datetime.now()
        start = now - datetime.timedelta(minutes=1)
        if ip and MobileAuthCode.objects.filter(ip=ip, createTime__gt=start).exists():
            raise PeiDiError(30501, msg='请求频率太高，请稍后重试')
        if MobileAuthCode.objects.filter(createTime__gt=start).filter(mobile=mobile, is_used=False).exists():
            raise PeiDiError(30501, msg='请求频率太高，请稍后重试')
        mobilecode = MobileAuthCode(mobile=mobile, areacode=areacode)
        mobilecode.save()
        template_param = json.dumps({"code": mobilecode.sms_code})
        res = sendSms(mobile, sign_name, template_code, template_param)
        if isinstance(res, SendSmsResponse):
            if res.body.code == "OK":
                return SuccessResponse({"sms_token": mobilecode.sms_token, "sms_code": mobilecode.sms_code, "res": res.body.message})
            else:
                raise PeiDiError(30501, msg='发送短信失败', detail=res.body.message)
        else:
            raise PeiDiError(30501, msg='发送短信失败', detail=str(res))
    except PeiDiError as err:
        return PeiDiErrorResponse(err)
    except Exception:
        print(traceback.format_exc())
        return ExceptionResponse(traceback.format_exc().split('\n')[-2])

@api_view(['POST'])
def checkALiYunSmsCode(request):
    try :
        data = request.data
        sms_code = data.get('sms_code', None)
        sms_token = data.get('sms_token', None)
        mobile = data.get('mobile', None)
        if mobile and sms_code and sms_token:
            try:
                mobileauthcode = MobileAuthCode.objects.get(mobile=mobile, sms_code=sms_code, sms_token=sms_token, is_used=False)
            except MobileAuthCode.DoesNotExist:
                raise PeiDiError(code=30502, msg='验证码不存在')
            else:
                if mobileauthcode.isexpired():
                    raise PeiDiError(code=30502, msg='验证码已过期')
                mobileauthcode.is_used = True
                mobileauthcode.save()
        else:
            raise PeiDiError(code=30502, msg='验证码无效', detail='sms_code/sms_token/mobile不能为空')
        return SuccessResponse('验证通过')
    except PeiDiError as err:
        return PeiDiErrorResponse(err)
    except Exception:
        print(traceback.format_exc())
        return ExceptionResponse(traceback.format_exc().split('\n')[-2])
