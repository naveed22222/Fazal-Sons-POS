# Generated by Django 5.1.1 on 2024-10-18 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppProduct', '0020_category_attribute_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='created_at',
            field=models.DateTimeField(null=True),
        ),
    ]
