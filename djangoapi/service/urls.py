from django.urls import path

from service.views import weixinservice
urlpatterns = [
    path('wxopenid', weixinservice.get_openid, name='get_openid', ),

]