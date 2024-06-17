from django.urls import path

from . import views

urlpatterns = [
    path("call-proc", views.call_procedure),
]
