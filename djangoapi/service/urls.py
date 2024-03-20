from django.urls import path

from .views import weixinservice
from .views import dingdingservice
urlpatterns = [
    path('wxopenid', weixinservice.get_openid, name='get_openid', ),
    path('dinguserinfo', dingdingservice.getUserInfoWithCode, name='getUserInfoWithCode', ),

]