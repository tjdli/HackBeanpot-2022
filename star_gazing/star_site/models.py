from django.db import models

# Create your models here.
from django.utils import timezone

CHOICES = ((1, 1), (2, 2), (3, 3), (4, 4), (5, 5))


class Location(models.Model):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=1000)
    description = models.TextField()
    pub_date = models.DateTimeField('date published', default=timezone.now)
    rating = models.IntegerField(choices=CHOICES)
    # address = map_fields.AddressField(max_length=200)
    # position = map_fields.GeoLocationField(max_length=100)


"""
class Constellation(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to="star_site/images", blank=True)
    months = models.CharField(max_length=255)
"""
