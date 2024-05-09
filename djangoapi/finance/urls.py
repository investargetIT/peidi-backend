from django.urls import path
from . import views

tmallRefundapi = views.TmallRefundView.as_view({
    'post': 'create',
})

urlpatterns = [
    path("refund/tmall", tmallRefundapi, name="tmallRefundapi"),
]
