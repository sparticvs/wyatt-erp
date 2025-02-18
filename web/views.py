from django.shortcuts import render
from .serializers import *
from .models import *

from rest_framework import viewsets


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class PurchaseOrderViewSet(viewsets.ModelViewSet):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

class PurchaseOrderItemViewSet(viewsets.ModelViewSet):
    queryset = PurchaseOrderItem.objects.all()
    serializer_class = PurchaseOrderItemSerializer

class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

class StockLocationViewSet(viewsets.ModelViewSet):
    queryset = StockLocation.objects.all()
    serializer_class = StockLocationSerializer

class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

class SubComponentViewSet(viewsets.ModelViewSet):
    queryset = SubComponent.objects.all()
    serializer_class = SubComponentSerializer

class ComponentViewSet(viewsets.ModelViewSet):
    queryset = Component.objects.all()
    serializer_class = ComponentSerializer

class SupplierComponentViewSet(viewsets.ModelViewSet):
    queryset = SupplierComponent.objects.all()
    serializer_class = SupplierComponentSerializer

class ProductSerialNumberViewSet(viewsets.ModelViewSet):
    queryset = ProductSerialNumber.objects.all()
    serializer_class = ProductSerialNumberSerializer

class BuildOrderViewSet(viewsets.ModelViewSet):
    queryset = BuildOrder.objects.all()
    serializer_class = BuildOrderSerializer

class BuildOrderItemViewSet(viewsets.ModelViewSet):
    queryset = BuildOrderItem.objects.all()
    serializer_class = BuildOrderItemSerializer
