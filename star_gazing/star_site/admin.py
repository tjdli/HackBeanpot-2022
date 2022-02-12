from django.contrib import admin
from django_google_maps import fields as map_fields
from django_google_maps import widgets as map_widgets

# Register your models here.
from .models import Location


class LocationAdmin(admin.ModelAdmin):
    formfield_overrides = {
        map_fields.AddressField: {'widget': map_widgets.GoogleMapsAddressWidget},
    }
    list_display = ('id', 'name')


admin.site.register(Location, LocationAdmin)
