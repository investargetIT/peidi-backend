#coding=utf-8
import datetime
import hashlib
import hmac
import os
import json
import time
import traceback
from urllib.parse import urlencode

import requests
from rest_framework.decorators import api_view

from utils.customclass import PeiDiError, SuccessResponse, ExceptionResponse, PeiDiErrorResponse

DingDing_AppKey = os.environ.get('DingDing_APPKEY')
DingDing_AppSecret = os.environ.get('DingDing_APPSECRET')


def compute_sign(appsecret):
    """
    计算钉钉免登签名
    """
    millis_unix_timestamp = int(time.time() * 1000)
    # HMAC-SHA1 加密
    sign = hmac.new(appsecret.encode('utf-8'), str(millis_unix_timestamp).encode('utf-8'), hashlib.sha1).hexdigest()
    return sign


def getAccessToken():
    url = 'https://oapi.dingtalk.com/gettoken?appkey=%s&appsecret=%s' % (DingDing_AppKey, DingDing_AppSecret)
    response = requests.get(url).content
    res = json.loads(response.decode())
    errcode = res.get('errcode')
    if errcode != 0:
        raise PeiDiError(20500, msg=res['errmsg'])
    access_token = res['access_token']
    expires_in = res['expires_in'] < 360
    if expires_in:
        access_token = getAccessToken()
    return access_token


# def getUnionid_bycode(code):
#     timestamp = int(time.time() * 1000)
#     sign = compute_sign(DingDing_AppSecret)
#     url = 'https://oapi.dingtalk.com/sns/getuserinfo_bycode?accessKey=%s&timestamp=%s&signature=%s' % (DingDing_AppKey, timestamp,  sign)
#     response = requests.post(url, data={'tmp_auth_code': code}).content
#     res = json.loads(response.decode())
#     errcode = res.get('errcode')
#     if errcode != 0:
#         raise PeiDiError(2050, msg=res['errmsg'])
#     return res['user_info']['unionid']

# def getUserid_byUnionid(union_id):
#     access_token = getAccessToken()
#     url = 'https://oapi.dingtalk.com/topapi/user/getbyunionid?access_token=%s' % access_token
#     response = requests.post(url, data={'unionid': union_id}).content
#     res = json.loads(response.decode())
#     errcode = res.get('errcode')
#     if errcode != 0:
#         raise PeiDiError(2050, msg=res['errmsg'])
#     return res['result']['userid']
def getUserid_byCode(code):
    access_token = getAccessToken()
    url = 'https://oapi.dingtalk.com/topapi/v2/user/getuserinfo?access_token=%s' % access_token
    response = requests.post(url, data={'code': code}).content
    res = json.loads(response.decode())
    errcode = res.get('errcode')
    if errcode != 0:
        raise PeiDiError(20501, msg=res['errmsg'])
    return res['result']['userid']

def getUserinfo_byUserid(user_id):
    access_token = getAccessToken()
    url = 'https://oapi.dingtalk.com/topapi/v2/user/get?access_token=%s' % access_token
    response = requests.post(url, data={'userid': user_id}).content
    res = json.loads(response.decode())
    errcode = res.get('errcode')
    if errcode != 0:
        raise PeiDiError(20502, msg=res['errmsg'])
    return res


@api_view(['POST'])
def getUserInfoWithCode(request):
    try:
        code = request.data.get('code')
        user_id = getUserid_byCode(code)
        userinfo = getUserinfo_byUserid(user_id)
        return SuccessResponse(result=userinfo)
    except PeiDiError as err:
        return PeiDiErrorResponse(err)
    except Exception:
        return ExceptionResponse(traceback.format_exc().split('\n')[-2])
