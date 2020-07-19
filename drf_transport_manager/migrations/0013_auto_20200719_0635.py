# Generated by Django 3.0 on 2020-07-19 06:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('drf_transport_manager', '0012_auto_20200719_0621'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehiclestaffmodel',
            name='agency_name',
        ),
        migrations.AddField(
            model_name='vehiclestaffmodel',
            name='agency',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='transport_agency_staff', to='drf_transport_manager.TransportAgencyModel', verbose_name='Agency Name'),
        ),
    ]