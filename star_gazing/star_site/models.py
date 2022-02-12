from django.db import models


# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=1000)
    description = models.TextField()
    pub_date = models.DateTimeField('date published')
    # address = map_fields.AddressField(max_length=200)
    # position = map_fields.GeoLocationField(max_length=100)
