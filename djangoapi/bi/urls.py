from django.urls import path

from . import views

urlpatterns = [
    path("call-proc", views.call_procedure),
    path("get-dashboard-data/", views.get_dashboard_data),
]
