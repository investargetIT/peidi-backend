from django.urls import path

from .views import weixinservice
from .views import dingdingservice
from .views import aliyunsms
urlpatterns = [
    path('wxopenid', weixinservice.get_openid, name='get_openid'),
    path('wxuserinfo', weixinservice.getWeiXinUserInfo, name='getWeixinUserInfo'),
    path('dinguserinfo', dingdingservice.getUserInfoWithCode, name='getUserInfoWithCode'),
    path('sendsms', aliyunsms.sendALiYunSmsCode, name='sendALiYunSmsCode'),
    path('checksms', aliyunsms.checkALiYunSmsCode, name='checkALiYunSmsCode'),
]