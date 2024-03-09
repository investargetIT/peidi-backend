from django.shortcuts import render

# Create your views here.
#coding=utf-8
import json
import traceback
import requests
from rest_framework.decorators import api_view

from configs.wechatconfig import WX_APPID, WX_APPSECRET
from utils.customclass import PeiDiError, SuccessResponse, ExceptionResponse, PeiDiErrorResponse


@api_view(['GET'])
def get_openid(request):
    try:
        code = request.GET.get('code')
        url = 'https://api.weixin.qq.com/sns/jscode2session?appid=%s&secret=%s&js_code=%s&grant_type=authorization_code' % (WX_APPID, WX_APPSECRET, code)
        response = requests.get(url).content
        res = json.loads(response.decode())
        return SuccessResponse(result=res)
    except Exception:
        return ExceptionResponse(msg=traceback.format_exc())


def getAccessTokenWithCode(code):
    url = 'https://api.weixin.qq.com/sns/oauth2/access_token?appid=%s&secret=%s&code=%s&grant_type=authorization_code' \
          % (WX_APPID, WX_APPSECRET, code)
    response = requests.get(url).content
    res = json.loads(response.decode())
    openid = res.get('openid')
    if not openid:
        raise PeiDiError(2050, msg=res['errmsg'])
    access_token, open_id = res['access_token'], res['openid']
    expires_in = res['expires_in'] < 360
    if expires_in:
        access_token, open_id = refreshAccessToken(res['refresh_token'])
    return access_token, open_id


def refreshAccessToken(refresh_token):
    url = 'https://api.weixin.qq.com/sns/oauth2/refresh_token?appid=%s&grant_type=refresh_token&refresh_token=%s' % \
          (WX_APPID, refresh_token)
    response = requests.get(url).content
    res = json.loads(response.decode())
    openid = res.get('openid')
    if not openid:
        raise PeiDiError(2050, msg=res['errmsg'])
    access_token, open_id = res['access_token'], res['openid']
    return access_token, open_id

def getUserInfo(access_token , open_id):
    url = 'https://api.weixin.qq.com/sns/userinfo?access_token=%s&openid=%s&lang=zh_CN' % (access_token, open_id)
    response = requests.get(url).content
    res = json.loads(response.decode())
    openid = res.get('openid')
    if not openid:
        raise PeiDiError(2050, msg=res['errmsg'])
    return res


@api_view(['POST'])
def getWeiXinUserInfo(request):
    try:
        code = request.data.get('code')
        access_token, open_id = getAccessTokenWithCode(code)
        userinfo = getUserInfo(access_token, open_id)
        return SuccessResponse(result=userinfo)
    except PeiDiError as err:
        return PeiDiErrorResponse(err)
    except Exception:
        return ExceptionResponse(traceback.format_exc().split('\n')[-2])
