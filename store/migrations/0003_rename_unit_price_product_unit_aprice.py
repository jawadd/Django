# Generated by Django 4.1.5 on 2023-05-01 11:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_rename_price_product_unit_price_product_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='unit_price',
            new_name='unit_aprice',
        ),
    ]