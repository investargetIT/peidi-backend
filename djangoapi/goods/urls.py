from django.urls import path

from . import views
platformGoodsapi = views.PlatformGoodsView.as_view({
    'get': 'list',
    'post': 'create',
    'update': 'update',
    'delete': 'destroy'
})

specGoodsapi = views.SpecGoodsView.as_view({
    'get': 'list',
    'post': 'create',
    'update': 'update',
    'delete': 'destroy'
})

suiteGoodsRecapi = views.SuiteGoodsRecView.as_view({
    'get': 'list',
    'post': 'create',
    'update': 'update',
    'delete': 'destroy'
})


urlpatterns = [
    path("platformGoods", platformGoodsapi, name="PlatformGoods"),
    path("specGoods", specGoodsapi, name="specGoodsapi"),
    path("suiteGoodsRec", suiteGoodsRecapi, name="suiteGoodsRecapi"),


]