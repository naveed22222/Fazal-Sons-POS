# Generated by Django 5.1.1 on 2024-10-07 13:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppProduct', '0010_remove_product_brand_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='AppProduct.category', to_field='category_name'),
        ),
        migrations.AddField(
            model_name='product',
            name='pc_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='AppProduct.parentcategory', to_field='pc_name'),
        ),
        migrations.AddField(
            model_name='product',
            name='sub_category_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='AppProduct.subcategory', to_field='sub_category_name'),
        ),
    ]
