from django.urls import path, re_path

from . import views
platformGoodsapi = views.PlatformGoodsView.as_view({
    'get': 'list',
    'post': 'create',
})

platformGoodsapione = views.PlatformGoodsView.as_view({
    'update': 'update',
    'delete': 'destroy'
})

specGoodsapi = views.SpecGoodsView.as_view({
    'get': 'list',
    'post': 'create',
})

specGoodsapione = views.SpecGoodsView.as_view({
    'update': 'update',
    'delete': 'destroy'
})

suiteGoodsRecapi = views.SuiteGoodsRecView.as_view({
    'get': 'list',
    'post': 'create',
})

suiteGoodsRecapione = views.SuiteGoodsRecView.as_view({
    'update': 'update',
    'delete': 'destroy'
})

urlpatterns = [
    path("platformGoods", platformGoodsapi, name="PlatformGoods"),
    re_path("platformGoods/(?P<pk>\d+)/", platformGoodsapione, name='platformGoodsapione'),
    path("specGoods", specGoodsapi, name="specGoodsapi"),
    re_path("specGoods/(?P<pk>\d+)/", specGoodsapione, name="specGoodsapione"),
    path("suiteGoodsRec", suiteGoodsRecapi, name="suiteGoodsRecapi"),
    re_path("suiteGoodsRec/(?P<pk>\d+)/", suiteGoodsRecapione, name="suiteGoodsRecapione"),


]