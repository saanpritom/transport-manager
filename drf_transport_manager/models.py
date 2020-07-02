from django.db import models
from django.contrib.auth.models import User


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
