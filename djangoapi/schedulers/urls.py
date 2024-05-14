from django.urls import path
from . import views

urlpatterns = [
    path("senddingtalkmsg", views.schedule_send_dingtalk_msg),
]
