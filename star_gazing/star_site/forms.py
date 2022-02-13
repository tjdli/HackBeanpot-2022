from django import forms

from .models import Location


class LocationForm(forms.ModelForm):

    class Meta:
        model = Location
        fields = ['name', 'position', 'description', 'rating']


class AddressForm(forms.Form):
    address = forms.CharField(max_length=255)
