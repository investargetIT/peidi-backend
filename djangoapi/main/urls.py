"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path, re_path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="PeiDiData",
        default_version="v1",
        description="PeiDiData-API",
        terms_of_service="https://www.peidibrand.com/#/",
        contact=openapi.Contact(email="yangxm@peidibrand.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
)

urlpatterns = [
    re_path(r'swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path(r'chats/', include("chats.urls")),
    path(r'service/', include("service.urls")),
    path(r'goods/', include("goods.urls")),
    path(r'orders/', include("orders.urls")),
    path(r'finance/', include("finance.urls")),
    path(r'schedulers/', include("schedulers.urls")),
    path(r'admin/', admin.site.urls),
]
