# Generated by Django 3.0 on 2020-07-13 17:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('drf_transport_manager', '0008_auto_20200703_1732'),
    ]

    operations = [
        migrations.CreateModel(
            name='VehicleStaffModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staff_name', models.CharField(max_length=80, verbose_name='Staff Name')),
                ('staff_position', models.CharField(choices=[('Assistant', 'Assistant'), ('Driver', 'Driver'), ('Supervisor', 'Supervisor')], default='Driver', max_length=80, verbose_name='Staff Position')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email')),
                ('contact_number', models.CharField(blank=True, max_length=50, null=True, verbose_name='Contact Number')),
                ('license_number', models.CharField(blank=True, max_length=80, null=True, verbose_name='License Number')),
                ('address', models.TextField(blank=True, null=True, verbose_name='Address')),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/drf_transport_manager_images/driver_images/', verbose_name='Driver Image')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('agency_name', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='transport_agency_driver', to='drf_transport_manager.TransportAgencyModel', verbose_name='Agency Name')),
                ('created_by', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='transport_driver', to=settings.AUTH_USER_MODEL, verbose_name='Created by')),
            ],
            options={
                'verbose_name': 'Vehicle Staff Detail',
                'verbose_name_plural': 'Vehicle Staff Details',
                'ordering': ['staff_name'],
            },
        ),
    ]