from django.urls import path

from . import views

urlpatterns = [
    path("", views.get_sales_amount_ranking, name="get_sales_amount_ranking"),
]
