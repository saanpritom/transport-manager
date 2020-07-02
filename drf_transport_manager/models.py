from django.db import models
from django.contrib.auth.models import User
from .configs import get_media_directory


# Create your models here.

""" VehicleType Model holds the data of the types of vehicle. Like Bus, Truck, Mini Truck etc.
    Upon migrating this class seeding a list of default vehicle type values. These values are reside in
    on the vehicle_types.json file in the fixtures directory inside this app"""


class VehicleType(models.Model):
    type_name = models.CharField(max_length=50, null=False, blank=False, verbose_name='Type Name')
    is_active = models.BooleanField(default=True, verbose_name='Is Active')
    created_by = models.ForeignKey(User, related_name='vehicle_types', on_delete=models.CASCADE, null=False,
                                   verbose_name='Created by', default=1)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated at')

    def __str__(self):
        return self.type_name

    class Meta:
        verbose_name = 'Vehicle Type'
        verbose_name_plural = 'Vehicle Types'
        ordering = ['type_name']


""" VehicleManufacturer holds the data about the details of a vehicle manufacturer. Like a Manufacturer company
    name, country of origin, website, email, contact number and address. Some manufacturer data are initially
    given. You will find those initial on the vehicle_manufacturers.json file in the fixtures directory inside
    this app. In order to upload images of the manufactures logo please set MEDIA_ROOT on your settings.py file
    and place the drf_transport_manager_images folder to your media directory. All the default images used in
    this package is in the drf_transport_manager_images folder."""


class VehicleManufacturer(models.Model):
    manufacturer_name = models.CharField(max_length=50, null=False, blank=False, verbose_name='Manufacturer Name')
    country_of_origin = models.CharField(max_length=50, null=True, blank=True, verbose_name='Country of Origin')
    website_url = models.URLField(max_length=200, null=True, blank=True, verbose_name='Website')
    email = models.EmailField(max_length=254, null=True, blank=True, verbose_name='Email')
    contact_number = models.CharField(max_length=50, null=True, blank=True, verbose_name='Contact Number')
    address = models.TextField(null=True, blank=True, verbose_name='Address')
    logo = models.ImageField(upload_to=get_media_directory('drf_transport_manager_images/manufacturer_logo/'),
                             null=True, blank=True, verbose_name='Manufacturer Logo')
    is_active = models.BooleanField(default=True, verbose_name='Is Active')
    created_by = models.ForeignKey(User, related_name='vehicle_manufacturers', on_delete=models.CASCADE, null=False,
                                   verbose_name='Created by', default=1)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated at')

    def __str__(self):
        return self.manufacturer_name

    class Meta:
        verbose_name = 'Vehicle Manufacturer'
        verbose_name_plural = 'Vehicle Manufacturers'
        ordering = ['manufacturer_name']
