from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
import datetime
import hashlib
import uuid

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address1 = models.CharField(max_length=200)
    address2 = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    state = models.CharField(max_length=2, null=True, blank=True)
    zip_code = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.address1}"

class PurchaseOrder(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    order_date = models.DateField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    items = models.ManyToManyField('Product', through='PurchaseOrderItem')

    def __str__(self):
        return f"Order #{self.id}"

class PurchaseOrderItem(models.Model):
    order = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"Order #{self.order.id} - {self.product.name}"


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    sku = models.CharField(max_length=50, unique=True)
    component = models.ForeignKey(
        'Component',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        limit_choices_to={'isFinal': True}
    )

    def __str__(self):
        return self.name

class StockLocation(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    is_root = models.BooleanField(default=False)
    parentLocation = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)

    def clean(self):
        if self.is_root and self.parentLocation is not None:
            raise ValidationError({'parentLocation': 'A root location cannot have a parent'})
        if not self.is_root and self.parentLocation is None:
            raise ValidationError({'parentLocation': 'A non-root location must have a parent'})
        if self.parentLocation is not None and StockLocation.objects.exclude(pk=self.pk).filter(parentLocation=self.parentLocation, name=self.name).exists():
            raise ValidationError({'name': 'A location with the same name already exists in the same parent location'})

    def __str__(self):
        path = []
        location = self
        while location:
            path.insert(0, location.name)
            location = location.parentLocation
        return '/'.join(path)


class Stock(models.Model):
    location = models.ForeignKey(StockLocation, on_delete=models.PROTECT)
    supplierComponent = models.ForeignKey('SupplierComponent', on_delete=models.PROTECT, null=True, blank=True)
    # Direct access to this field is not atomic!
    quantity = models.PositiveIntegerField(default=1)
    units = models.CharField(max_length=5, default='pcs')
    cost_basis = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    batchNumber = models.CharField(max_length=50, default="!! UNSET !!")

    # This transaction must be atomic in nature to ensure that the quantity is updated correctly
    def increment(self, delta=1):
        Stock.objects.select_for_update().filter(pk=self.pk).update(quantity=models.F('quantity') + delta)

    # This transaction must be atomic in nature to ensure that the quantity is updated correctly
    def decrement(self, delta=1):
        if self.quantity >= delta:
            Stock.objects.select_for_update().filter(pk=self.pk).update(quantity=models.F('quantity') - delta)
        else:
            raise ValidationError({'quantity': 'Cannot decrement more than available stock'})

    def __str__(self):
        return f"{self.quantity} {self.units} - {self.supplierComponent} - {self.location.name} - {self.batchNumber}"

    def save(self, *args, **kwargs):
        if Stock.objects.filter(batchNumber=self.batchNumber, supplierComponent=self.supplierComponent).exists():
            raise ValidationError({'batchNumber': 'Batchnumber already exists for this suppliercomponent'})
        return super().save(*args, **kwargs)


class Component(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    isFinal = models.BooleanField(default=False)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    units = models.CharField(max_length=5, default='pcs')
    cost_basis = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return self.name


class SubComponent(models.Model):
    component = models.ForeignKey(Component, on_delete=models.PROTECT, related_name='subcomponents')
    subcomponent = models.ForeignKey(Component, on_delete=models.PROTECT, related_name='as_subcomponent')
    quantity = models.PositiveIntegerField()
    units = models.CharField(max_length=5, default='pcs')

    def __str__(self):
        return f"{self.component.name} - {self.subcomponent.name} - {self.quantity} {self.units}"
    

class SupplierComponent(models.Model):
    supplier = models.ForeignKey('Supplier', on_delete=models.PROTECT)
    component = models.ForeignKey('Component', on_delete=models.PROTECT)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    units = models.CharField(max_length=5, default='pcs')

    def __str__(self):
        return f"{self.supplier.name} - {self.component.name}"
    

class Supplier(models.Model):
    name = models.CharField(max_length=100, unique=True)
    url = models.URLField(blank=True, null=True)
    components = models.ManyToManyField(Component, through='SupplierComponent')

    def __str__(self):
        return self.name


class ProductSerialNumber(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    serialNumber = models.CharField(max_length=100, unique=True)
    isAssigned = models.BooleanField(default=False)

    def generate_serialnumber(self):
        return hashlib.sha256(uuid.uuid4().bytes).hexdigest()[:100]

    def save(self, *args, **kwargs):
        if not self.serialNumber:
            self.serialNumber = self.generate_serialnumber()
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.product.name} - {self.serialNumber}"


class BuildOrder(models.Model):
    description = models.TextField(blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True)
    class BuildStateType(models.TextChoices):
        PENDING = 'pending', 'Pending'
        IN_PROGRESS = 'in_progress', 'In Progress'
        DONE = 'done', 'Done'
    status = models.CharField(max_length=20, choices=BuildStateType.choices, default=BuildStateType.PENDING)

    def get_id(self):
        return f"BO-{self.id}"

    def __str__(self):
        return f"{self.get_id()} - {self.owner} - {self.status}"

class BuildOrderItem(models.Model):
    buildOrder = models.ForeignKey(BuildOrder, on_delete=models.PROTECT)
    component = models.ForeignKey(Component, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()
    units = models.CharField(max_length=5, default='pcs')
    batchNumber = models.CharField(max_length=100, editable=False)

    def save(self, *args, **kwargs):
        if not self.pk:
            now = datetime.datetime.now()
            self.batchNumber = f"{now.strftime('%Y%m%d')}-{now.strftime('%H%M%S')}-{self.quantity}"
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.buildOrder.get_id()} - {self.component.name} - {self.quantity} {self.units}"