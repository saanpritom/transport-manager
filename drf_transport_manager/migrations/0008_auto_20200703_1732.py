# Generated by Django 3.0 on 2020-07-03 17:32

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('drf_transport_manager', '0007_transportagencymodel'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='VehicleManufacturer',
            new_name='VehicleManufacturerModel',
        ),
        migrations.RenameModel(
            old_name='VehicleType',
            new_name='VehicleTypeModel',
        ),
    ]
