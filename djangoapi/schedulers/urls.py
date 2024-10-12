from django.urls import path
from . import views

urlpatterns = [
    path("send-dingtalk-msg/", views.schedule_send_dingtalk_msg),
    path("send-spu-daily-report/", views.schedule_send_spu_daily_report),
    path("get-dashboard-data/", views.schedule_get_dashboard_data),
    path("get-increment-data/", views.schedule_get_increment_data),
]
