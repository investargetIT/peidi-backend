from django.urls import path
from . import views

urlpatterns = [
    path("send-dingtalk-msg", views.schedule_send_dingtalk_msg),
    # path("get-dashboard-data", views.schedule_get_dashboard_data),
]
