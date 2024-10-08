# Generated by Django 5.1.1 on 2024-10-03 08:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attribute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribute_name', models.CharField(max_length=100, null=True, unique=True)),
                ('type', models.CharField(max_length=100, null=True)),
                ('symbol', models.CharField(max_length=100, null=True)),
                ('description', models.TextField(max_length=500, null=True)),
                ('status', models.TextField(max_length=100, null=True)),
                ('created_at', models.DateTimeField(null=True)),
                ('created_by', models.CharField(max_length=200, null=True)),
                ('updated_at', models.DateTimeField(null=True)),
                ('updated_by', models.CharField(max_length=200, null=True)),
            ],
            options={
                'db_table': 'tbl_attribute',
            },
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('symbol', models.CharField(max_length=100, null=True)),
                ('description', models.TextField(max_length=500, null=True)),
                ('status', models.TextField(max_length=100, null=True)),
                ('created_at', models.DateTimeField(null=True)),
                ('created_by', models.CharField(max_length=200, null=True)),
                ('updated_at', models.DateTimeField(null=True)),
                ('updated_by', models.CharField(max_length=200, null=True)),
            ],
            options={
                'db_table': 'tbl_brand',
            },
        ),
        migrations.CreateModel(
            name='Variation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vairation_name', models.CharField(max_length=100, null=True)),
                ('symbol', models.CharField(max_length=100, null=True)),
                ('description', models.TextField(max_length=500, null=True)),
                ('status', models.TextField(max_length=100, null=True)),
                ('created_at', models.DateTimeField(null=True)),
                ('created_by', models.CharField(max_length=200, null=True)),
                ('updated_at', models.DateTimeField(null=True)),
                ('updated_by', models.CharField(max_length=200, null=True)),
                ('attribute_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='AppProduct.attribute', to_field='attribute_name')),
            ],
            options={
                'db_table': 'tbl_variation',
            },
        ),
    ]
