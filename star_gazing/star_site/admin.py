from django.contrib import admin
# from django_google_maps import fields as map_fields
# from django_google_maps import widgets as map_widgets

# Register your models here.
from .models import Location


class LocationAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name']}),
        ("Position", {'fields': ['position']}),
        ("Content", {'fields': ['description']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    list_display = ('name', 'pub_date')

"""
class ConstellationAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name']}),
        ("Description", {'fields': ['description]}),
        ("Image", {'fields': ['image']}),
        ('Months', {'fields': ['months']}),
    ]
    list_display = ('name', 'id')
"""


admin.site.register(Location, LocationAdmin)
# admin.site.register(Constellation, ConstellationAdmin)
