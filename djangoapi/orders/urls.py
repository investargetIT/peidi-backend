from django.urls import path


from . import views
ordersapi = views.OrdersView.as_view({
    'get': 'list',
    'post': 'create',
})

ordersapione = views.OrdersView.as_view({
        'put': 'update',
        'delete': 'destroy',
})

traderordersapi = views.TraderOrdersView.as_view({
    'get': 'list',
    'post': 'create',
})

traderordersapione = views.TraderOrdersView.as_view({
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
    path("orders/(?P<pk>\d+)/", ordersapione, name='ordersapione'),
    path("traderorders", traderordersapi, name="traderordersapi"),
    path("traderorders/(?P<pk>\d+)/", traderordersapione, name='traderordersapione'),
    path("testcount", testGroupByCount, name="testGroupByCount"),
    path("testamount", testGroupByAmount, name="testGroupByAmount"),



]