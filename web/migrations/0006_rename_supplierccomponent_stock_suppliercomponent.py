# Generated by Django 5.1.3 on 2024-11-24 04:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_alter_stock_serialnumber'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stock',
            old_name='suppliercComponent',
            new_name='supplierComponent',
        ),
    ]
