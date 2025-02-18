from django.contrib import admin

from .models import Customer, Product, PurchaseOrder, PurchaseOrderItem, Stock, StockLocation, Supplier, SubComponent, Component, SupplierComponent, ProductSerialNumber, BuildOrder, BuildOrderItem

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(PurchaseOrder)
admin.site.register(PurchaseOrderItem)
admin.site.register(Stock)
admin.site.register(StockLocation)
admin.site.register(Supplier)
admin.site.register(SubComponent)
admin.site.register(Component)
admin.site.register(SupplierComponent)
admin.site.register(ProductSerialNumber)
admin.site.register(BuildOrder)
admin.site.register(BuildOrderItem)
