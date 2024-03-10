from django.urls import path


from . import views
ordersapi = views.OrdersView.as_view({
    'get': 'list',
    'post': 'create',
    'update': 'update',
    'delete': 'delete'
})


urlpatterns = [
    path("orders", ordersapi, name="ordersapi"),



]