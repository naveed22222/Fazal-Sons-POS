# Generated by Django 5.1.1 on 2024-10-09 14:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppCustomer', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='Province',
            new_name='province',
        ),
    ]
