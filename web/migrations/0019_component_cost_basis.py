# Generated by Django 5.1.3 on 2024-11-26 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0018_productserialnumber_isassigned'),
    ]

    operations = [
        migrations.AddField(
            model_name='component',
            name='cost_basis',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
