# Generated by Django 5.1.1 on 2024-12-17 07:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppPOS', '0003_alter_transactionreturn_quantity_and_more'),
        ('AppProduct', '0013_remove_product_size_remove_temporaryproduct_size_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='salesman',
            name='outlet_code',
        ),
        migrations.AddField(
            model_name='salesman',
            name='outlet',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='AppProduct.outlet'),
        ),
    ]