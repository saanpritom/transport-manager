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
    created_by = models.ForeignKey(get_user_model(), related_name='vehicle_types_creator', on_delete=models.CASCADE, null=False,
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
    created_by = models.ForeignKey(get_user_model(), related_name='vehicle_manufacturer_creator', on_delete=models.CASCADE, null=False,
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
    created_by = models.ForeignKey(get_user_model(), related_name='transport_agency_creator', on_delete=models.CASCADE, null=False,
                                   verbose_name='Created by', default=1)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated at')

    def __str__(self):
        return self.agency_name

    class Meta:
        verbose_name = 'Transport Agency'
        verbose_name_plural = 'Transport Agencies'
        ordering = ['agency_name']


"""VehicleStaffModel holds the data belongs to a vehicle staff like driver or assistant.
   Here a staff can be under a TransportAgency or staff can be an individual person.
   In case of individual person that staff must belongs to the N/A TransportAgencyModel instance"""


class VehicleStaffModel(models.Model):
    STAFF_POSITION_CHOICES = [
        ('Assistant', 'Assistant'),
        ('Driver', 'Driver'),
        ('Supervisor', 'Supervisor'),
    ]
    staff_name = models.CharField(max_length=80, null=False, blank=False, verbose_name='Staff Name')
    agency_name = models.ForeignKey(TransportAgencyModel, related_name='transport_agency_driver', on_delete=models.CASCADE,
                                    null=False, verbose_name='Agency Name', default=1)
    staff_position = models.CharField(max_length=80, choices=STAFF_POSITION_CHOICES, default='Driver',
                                      verbose_name='Staff Position')
    email = models.EmailField(max_length=254, null=True, blank=True, verbose_name='Email')
    contact_number = models.CharField(max_length=50, null=True, blank=True, verbose_name='Contact Number')
    license_number = models.CharField(max_length=80, null=True, blank=True, verbose_name='License Number')
    address = models.TextField(null=True, blank=True, verbose_name='Address')
    image = models.ImageField(upload_to=get_media_directory('drf_transport_manager_images/driver_images/'),
                              null=True, blank=True, verbose_name='Driver Image')
    is_active = models.BooleanField(default=True, verbose_name='Is Active')
    created_by = models.ForeignKey(get_user_model(), related_name='transport_driver_creator', on_delete=models.CASCADE, null=False,
                                   verbose_name='Created by', default=1)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated at')

    def __str__(self):
        return self.staff_name

    class Meta:
        verbose_name = 'Vehicle Staff Detail'
        verbose_name_plural = 'Vehicle Staff Details'
        ordering = ['staff_name']


"""VehicleDetailModel holds the data of the vehicles. A vehicle must be under a TransportAgencyModel instance.
    If that vehicle is alone then the value will be 1"""


class VehicleDetailModel(models.Model):
    registration_number = models.CharField(max_length=80, null=True, blank=True, verbose_name='Registration Number',
                                           default='N/A')
    chasis_number = models.CharField(max_length=80, null=True, blank=True, verbose_name='Chasis Number')
    type = models.ForeignKey(VehicleTypeModel, related_name='vehicle_type', on_delete=models.CASCADE,
                             null=False, verbose_name='Vehicle Type')
    manufacturer = models.ForeignKey(VehicleManufacturerModel, related_name='vehicle_manufacturer', on_delete=models.CASCADE,
                                     null=False, verbose_name='Vehicle Manufacturer')
    agency = models.ForeignKey(TransportAgencyModel, related_name='vehicle_agency', on_delete=models.CASCADE,
                               null=False, verbose_name='Agency', default=1)
    color = models.CharField(max_length=80, null=True, blank=True, verbose_name='Color')
    driver = models.ForeignKey(VehicleStaffModel, related_name='vehicle_driver', on_delete=models.CASCADE,
                               null=False, verbose_name='Driver', default=1)
    assistant = models.ForeignKey(VehicleStaffModel, related_name='vehicle_assistant', on_delete=models.CASCADE,
                                  null=False, verbose_name='Assistant', default=1)
    capacity = models.CharField(max_length=30, null=True, blank=True, verbose_name='Capacity')
    image = models.ImageField(upload_to=get_media_directory('drf_transport_manager_images/vehicle_images/'),
                              null=True, blank=True, verbose_name='Vehicle Image')
    is_active = models.BooleanField(default=True, verbose_name='Is Active')
    created_by = models.ForeignKey(get_user_model(), related_name='vehicle_detail_creator', on_delete=models.CASCADE, null=False,
                                   verbose_name='Created by', default=1)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated at')

    def __str__(self):
        return self.registration_number

    class Meta:
        verbose_name = 'Vehicle Detail'
        verbose_name_plural = 'Vehicle Details'
        ordering = ['registration_number']
