"""
URL configuration for wyatt_erp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include, re_path
from rest_framework import routers
from web import views

router = routers.DefaultRouter()
router.register(r'customer', views.CustomerViewSet)
router.register(r'product', views.ProductViewSet)
router.register(r'purchaseorder', views.PurchaseOrderViewSet)
router.register(r'purchaseorderitem', views.PurchaseOrderItemViewSet)
router.register(r'stock', views.StockViewSet)
router.register(r'stocklocation', views.StockLocationViewSet)
router.register(r'supplier', views.SupplierViewSet)
router.register(r'subcomponent', views.SubComponentViewSet)
router.register(r'component', views.ComponentViewSet)
router.register(r'suppliercomponent', views.SupplierComponentViewSet)
router.register(r'productserialnumber', views.ProductSerialNumberViewSet)
router.register(r'buildorder', views.BuildOrderViewSet)
router.register(r'buildorderitem', views.BuildOrderItemViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
