from django.db import models
from django_google_maps import fields as map_fields


# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length=255)
    address = map_fields.AddressField(max_length=200)
    position = map_fields.GeoLocationField(max_length=100)
