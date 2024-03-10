from django.urls import path

from . import views
platformGoodsapi = views.PlatformGoodsView.as_view({
    'get': 'list',
    'post': 'create',
    'update': 'update',
    'delete': 'delete'
})

specGoodsapi = views.SpecGoodsView.as_view({
    'get': 'list',
    'post': 'create',
    'update': 'update',
    'delete': 'delete'
})

suiteGoodsRecapi = views.SuiteGoodsRecView.as_view({
    'get': 'list',
    'post': 'create',
    'update': 'update',
    'delete': 'delete'
})


urlpatterns = [
    path("platformGoods", platformGoodsapi, name="PlatformGoods"),
    path("specGoods", specGoodsapi, name="specGoodsapi"),
    path("suiteGoodsRec", suiteGoodsRecapi, name="suiteGoodsRecapi"),


]