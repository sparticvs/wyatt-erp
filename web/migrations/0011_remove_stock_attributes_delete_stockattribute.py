# Generated by Django 5.1.3 on 2024-11-24 18:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0010_stock_batchnumber_alter_supplier_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock',
            name='attributes',
        ),
        migrations.DeleteModel(
            name='StockAttribute',
        ),
    ]
