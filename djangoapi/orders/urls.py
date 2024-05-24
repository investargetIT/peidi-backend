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

orderDetailsapi = views.OrderDetailsView.as_view({
    'post': 'create',
})

stockDetailsapi = views.StockDetailView.as_view({
    'post': 'create',
})

WMSShipDataAPI = views.WMSShipDataView.as_view({
    'post': 'create',
})

ExchangeManagementAPI = views.ExchangeManagementView.as_view({
    'get': 'list',
    'post': 'create',
})

ShopTargetAPI = views.ShopTargetView.as_view({
    'get': 'list',
    'post': 'create',
})

ShopTargetAPI2 = views.ShopTargetView.as_view({
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

historySalesOutDetailsapi = views.HistorySalesOutDetailsView.as_view({
    'get': 'list',
    'post': 'create',
})

historySalesOutDetailsapione = views.HistorySalesOutDetailsView.as_view({
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
    path("hissalesout", historySalesOutDetailsapi, name="historySalesOutDetailsapi"),
    re_path("hissalesout/(?P<pk>\d+)/", historySalesOutDetailsapione, name='historySalesOutDetailsapione'),
    path("orderdetails", orderDetailsapi, name="orderDetailsapi"),
    path("stockdetails", stockDetailsapi, name="stockDetailsapi"),
    path("wmsshipdata", WMSShipDataAPI, name="WMSShipDataAPI"),
    path('exchange', ExchangeManagementAPI, name="ExchangeManagementAPI"),
    path('shop_target', ShopTargetAPI, name="ShopTargetAPI"),
    re_path("shop_target/(?P<pk>\d+)/", ShopTargetAPI2, name='ShopTargetAPI2'),
    path("testcount", testGroupByCount, name="testGroupByCount"),
    path("testamount", testGroupByAmount, name="testGroupByAmount"),
]
