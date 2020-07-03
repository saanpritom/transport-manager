from django.db import models
from django.contrib.auth import get_user_model
from .configs import get_media_directory


# Create your models here.

""" VehicleTypeModel holds the data of the types of vehicle. Like Bus, Truck, Mini Truck etc.
    Upon migrating this class seeding a list of default vehicle type values. These values are reside in
    on the vehicle_types.json file in the fixtures directory inside this app"""


class VehicleTypeModel(models.Model):
    type_name = models.CharField(max_length=50, null=False, blank=False, verbose_name='Type Name')
    is_active = models.BooleanField(default=True, verbose_name='Is Active')
    created_by = models.ForeignKey(get_user_model(), related_name='vehicle_types', on_delete=models.CASCADE, null=False,
                                   verbose_name='Created by', default=1)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated at')

    def __str__(self):
        return self.type_name

    class Meta:
        verbose_name = 'Vehicle Type'
        verbose_name_plural = 'Vehicle Types'
        ordering = ['type_name']


""" VehicleManufacturerModel holds the data about the details of a vehicle manufacturer. Like a Manufacturer company
    name, country of origin, website, email, contact number and address. Some manufacturer data are initially
    given. You will find those initial on the vehicle_manufacturers.json file in the fixtures directory inside
    this app. In order to upload images of the manufactures logo please set MEDIA_ROOT on your settings.py file
    and place the drf_transport_manager_images folder to your media directory. All the default images used in
    this package is in the drf_transport_manager_images folder."""


class VehicleManufacturerModel(models.Model):
    manufacturer_name = models.CharField(max_length=50, null=False, blank=False, verbose_name='Manufacturer Name')
    country_of_origin = models.CharField(max_length=50, null=True, blank=True, verbose_name='Country of Origin')
    website_url = models.URLField(max_length=200, null=True, blank=True, verbose_name='Website')
    email = models.EmailField(max_length=254, null=True, blank=True, verbose_name='Email')
    contact_number = models.CharField(max_length=50, null=True, blank=True, verbose_name='Contact Number')
    address = models.TextField(null=True, blank=True, verbose_name='Address')
    logo = models.ImageField(upload_to=get_media_directory('drf_transport_manager_images/manufacturer_logo/'),
                             null=True, blank=True, verbose_name='Manufacturer Logo')
    is_active = models.BooleanField(default=True, verbose_name='Is Active')
    created_by = models.ForeignKey(get_user_model(), related_name='vehicle_manufacturers', on_delete=models.CASCADE, null=False,
                                   verbose_name='Created by', default=1)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated at')

    def __str__(self):
        return self.manufacturer_name

    class Meta:
        verbose_name = 'Vehicle Manufacturer'
        verbose_name_plural = 'Vehicle Manufacturers'
        ordering = ['manufacturer_name']


"""TransportAgencyModel holds the data belongs to a transport company. It is not necessary that every vehichle
   belongs to an agency. In that case the vehicle will be a member of a N/A agency. The N/A instance ID will always
   be 1. Here an agency can be a fully operational transport company or can be any individual person.
   Some default data are on the transport_agencies.json file at the fixtures directory in this app"""


class TransportAgencyModel(models.Model):
    agency_name = models.CharField(max_length=80, null=False, blank=False, default='N/A',
                                   verbose_name='Manufacturer Name')
    contact_person = models.CharField(max_length=80, null=False, blank=False, default='N/A',
                                      verbose_name='Contact Person Name')
    website_url = models.URLField(max_length=200, null=True, blank=True, verbose_name='Website')
    email = models.EmailField(max_length=254, null=True, blank=True, verbose_name='Email')
    contact_number = models.CharField(max_length=50, null=True, blank=True, verbose_name='Contact Number')
    address = models.TextField(null=True, blank=True, verbose_name='Address')
    is_active = models.BooleanField(default=True, verbose_name='Is Active')
    created_by = models.ForeignKey(get_user_model(), related_name='transport_agency', on_delete=models.CASCADE, null=False,
                                   verbose_name='Created by', default=1)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated at')

    def __str__(self):
        return self.agency_name

    class Meta:
        verbose_name = 'Transport Agency'
        verbose_name_plural = 'Transport Agencies'
        ordering = ['agency_name']
