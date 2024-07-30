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

# specGoodsapi = views.SpecGoodsView.as_view({
#     'get': 'list',
#     'post': 'create',
# })

# specGoodsapione = views.SpecGoodsView.as_view({
#     'update': 'update',
#     'delete': 'destroy'
# })

suiteGoodsRecapi = views.SuiteGoodsRecView.as_view({
    'get': 'list',
    'post': 'create',
})

suiteGoodsRecapione = views.SuiteGoodsRecView.as_view({
    'update': 'update',
    'delete': 'destroy'
})


SPUapi = views.SPUView.as_view({
    'get': 'list',
    'post': 'create',
})

SPUapione = views.SPUView.as_view({
    'update': 'update',
    'delete': 'destroy'
})

urlpatterns = [
    # path("platformGoods", platformGoodsapi, name="PlatformGoods"),
    # re_path("platformGoods/(?P<pk>\d+)/", platformGoodsapione, name='platformGoodsapione'),
    # path("specGoods", specGoodsapi, name="specGoodsapi"),
    # re_path("specGoods/(?P<pk>\d+)/", specGoodsapione, name="specGoodsapione"),
    path("spec-goods/", views.override_spec_goods),
    path("suite-goods-rec/", views.override_suite_goods_rec),
    # re_path("suiteGoodsRec/(?P<pk>\d+)/", suiteGoodsRecapione, name="suiteGoodsRecapione"),
    # path("spu", SPUapi, name="SPUapi"),
    # re_path("spu/(?P<pk>\d+)/", SPUapione, name="SPUapione"),

]