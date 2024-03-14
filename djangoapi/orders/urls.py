from django.urls import path


from . import views
ordersapi = views.OrdersView.as_view({
    'get': 'list',
    'post': 'create',
    'update': 'update',
    'delete': 'destroy'
})
traderordersapi = views.TraderOrdersView.as_view({
    'get': 'list',
    'post': 'create',
    'update': 'update',
    'delete': 'destroy'
})
testGroupByCount = views.OrdersView.as_view({
    'get': 'testGroupByCount'
})
testGroupByAmount = views.OrdersView.as_view({
    'get': 'testGroupByAmount'
})
urlpatterns = [
    path("orders", ordersapi, name="ordersapi"),
    path("traderorders", traderordersapi, name="traderordersapi"),
    path("testcount", testGroupByCount, name="testGroupByCount"),
    path("testamount", testGroupByAmount, name="testGroupByAmount"),



]