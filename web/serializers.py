from rest_framework import serializers
from .models import Customer, Product, BuildOrder, BuildOrderItem, PurchaseOrder, PurchaseOrderItem, Stock, StockLocation, Supplier, SubComponent, Component, SupplierComponent, ProductSerialNumber, BuildOrder, BuildOrderItem

class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class BuildOrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BuildOrder
        fields = '__all__'

class BuildOrderItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BuildOrderItem
        fields = '__all__'

class PurchaseOrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = '__all__'

class PurchaseOrderItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PurchaseOrderItem
        fields = '__all__'

class StockSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Stock
        fields = '__all__'

class StockLocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StockLocation
        fields = '__all__'

class SupplierSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'

class SubComponentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SubComponent
        fields = '__all__'

class ComponentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Component
        fields = '__all__'

class SupplierComponentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SupplierComponent
        fields = '__all__'

class ProductSerialNumberSerializer(serializers.HyperlinkedModelSerializer):
    serialNumber = serializers.CharField(allow_blank=True)
    class Meta:
        model = ProductSerialNumber
        fields = '__all__'
