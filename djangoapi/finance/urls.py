from django.urls import path
from . import views

# tmallRefundapi = views.TmallRefundView.as_view({
#     'post': 'create',
# })
# pddRefundapi = views.PddRefundView.as_view({
#     'post': 'create',
# })
# jdRefundapi = views.JdRefundView.as_view({
#     'post': 'create',
# })
# douyinRefundapi = views.DouyinRefundView.as_view({
#     'post': 'create',
# })
# invoiceapi = views.InvoiceView.as_view({
#     'post': 'create',
# })
GoodsSalesSummaryAPI = views.GoodsSalesSummaryView.as_view({
    'post': 'create',
})
FinanceSalesAndInvoiceAPI = views.FinanceSalesAndInvoiceView.as_view({
    'post': 'create',
})
PDMaterialNOListAPI = views.PDMaterialNOListView.as_view({
    'post': 'create',
})

urlpatterns = [
    # path("invoice", invoiceapi, name="invoiceapi"),
    path("goods_sales_summary", GoodsSalesSummaryAPI, name="GoodsSalesSummaryAPI"),
    path("sales_and_invoice", FinanceSalesAndInvoiceAPI, name="FinanceSalesAndInvoiceAPI"),
    path("pd_material_no", PDMaterialNOListAPI, name="PDMaterialNOListAPI"),
    # path("refund/tmall", tmallRefundapi, name="tmallRefundapi"),
    # path("refund/pdd", pddRefundapi, name="pddRefundapi"),
    # path("refund/jd", jdRefundapi, name="jdRefundapi"),
    # path("refund/douyin", douyinRefundapi, name="douyinRefundapi"),
]
