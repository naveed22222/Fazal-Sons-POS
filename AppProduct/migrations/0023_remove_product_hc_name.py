# Generated by Django 5.1.1 on 2024-10-18 08:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppProduct', '0022_remove_product_head_category_product_hc_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='hc_name',
        ),
    ]
