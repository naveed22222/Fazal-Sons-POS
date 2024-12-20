# Generated by Django 5.1.1 on 2024-11-25 10:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppProduct', '0008_rename_category_name_subcategory_category_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubCatrgoryAttribute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppProduct.attribute')),
                ('sub_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppProduct.subcategory')),
            ],
            options={
                'db_table': 'tbl_subcategory_attribute',
            },
        ),
        migrations.AddField(
            model_name='subcategory',
            name='attribute_group',
            field=models.ManyToManyField(through='AppProduct.SubCatrgoryAttribute', to='AppProduct.attribute'),
        ),
    ]
