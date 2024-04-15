from django.urls import path, re_path

from . import views
ordersapi = views.OrdersView.as_view({
    'get': 'list',
    'post': 'create',
})

ordersapione = views.OrdersView.as_view({
    'put': 'update',
    'delete': 'destroy',
})

getCustomerPurchaseCounts = views.OrdersView.as_view({
    'post': 'getCustomerPurchaseCounts',
})

getShopSalesAmount = views.OrdersView.as_view({
    'post': 'getShopSalesAmount',
})

salesOutDetailsapi = views.SalesOutDetailsView.as_view({
    'get': 'list',
    'post': 'create',
})

salesOutDetailsapione = views.SalesOutDetailsView.as_view({
    'put': 'update',
    'delete': 'destroy',
})

testGroupByCount = views.OrdersView.as_view({
    'get': 'testGroupByCount'
})
testGroupByAmount = views.OrdersView.as_view({
    'get': 'testGroupByAmount'
})

urlpatterns = [
    path("orders", ordersapi, name="ordersapi"),
    path("customercount", getCustomerPurchaseCounts, name="getCustomerPurchaseCounts"),
    path("shopsalesamount", getShopSalesAmount, name="getShopSalesAmount"),
    re_path("orders/(?P<pk>\d+)/", ordersapione, name='ordersapione'),
    path("salesout", salesOutDetailsapi, name="salesOutDetailsapi"),
    re_path("salesout/(?P<pk>\d+)/", salesOutDetailsapione, name='salesOutDetailsapione'),
    path("testcount", testGroupByCount, name="testGroupByCount"),
    path("testamount", testGroupByAmount, name="testGroupByAmount"),



]