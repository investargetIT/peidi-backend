from django.urls import path
from . import views

tmallRefundapi = views.TmallRefundView.as_view({
    'post': 'create',
})
pddRefundapi = views.PddRefundView.as_view({
    'post': 'create',
})
jdRefundapi = views.JdRefundView.as_view({
    'post': 'create',
})
douyinRefundapi = views.DouyinRefundView.as_view({
    'post': 'create',
})

urlpatterns = [
    path("refund/tmall", tmallRefundapi, name="tmallRefundapi"),
    path("refund/pdd", pddRefundapi, name="pddRefundapi"),
    path("refund/jd", jdRefundapi, name="jdRefundapi"),
    path("refund/douyin", douyinRefundapi, name="douyinRefundapi"),
]