# Generated by Django 5.1.1 on 2024-12-12 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppProduct', '0012_alter_product_season_alter_temporaryproduct_season'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='size',
        ),
        migrations.RemoveField(
            model_name='temporaryproduct',
            name='size',
        ),
        migrations.AddField(
            model_name='product',
            name='notes',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='temporaryproduct',
            name='notes',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]