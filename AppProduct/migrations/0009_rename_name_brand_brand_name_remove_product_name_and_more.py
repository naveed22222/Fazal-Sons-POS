# Generated by Django 5.1.1 on 2024-10-07 13:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppProduct', '0008_rename_brand_name_product_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='brand',
            old_name='name',
            new_name='brand_name',
        ),
        migrations.RemoveField(
            model_name='product',
            name='name',
        ),
        migrations.AddField(
            model_name='product',
            name='brand_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='AppProduct.brand', to_field='brand_name'),
        ),
    ]
