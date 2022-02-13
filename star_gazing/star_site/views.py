from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.utils import timezone
from django.views import generic

from .forms import LocationForm, AddressForm
from .models import Location

import requests, json


class HomePageView(generic.TemplateView):
    template_name = "star_site/home.html"


class StarLocationsView(generic.TemplateView):
    template_name = "star_site/star_locations.html"
    context_object_name = "latest_locations_list"

    def get_queryset(self):
        """Returns most recent description"""
        return Location.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')


def location_list(request):
    form = AddressForm()
    ordered_locations = Location.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')
    locations = Location.objects.filter(pub_date__lte=timezone.now()).all()
    if request.method == "POST":
        form = AddressForm(request.POST)
        if form.is_valid():

            sorted_locations = sorted(locations, key=lambda position: sort_by_distance(form.cleaned_data["address"], position.position))
            return render(request, "star_site/star_locations.html", {'form': form, 'locations': sorted_locations})
    return render(request, "star_site/star_locations.html", {'form': form, 'locations': ordered_locations})


def location_form(request):
    form = LocationForm()
    if request.method == "POST":
        form = LocationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/star_locations')
    # locations = Location.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')
    return render(request, "star_site/location_add_form.html", {'form': form})


def distance_list(request):
    form = AddressForm()
    ordered_locations = Location.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')
    locations = Location.objects.filter(pub_date__lte=timezone.now()).all()
    if request.method == "POST":
        form = AddressForm(request.POST)
        if form.is_valid():
            sorted_locations = sorted(locations, key=lambda position: sort_by_distance(form.address, position))
            return render(request, "star_site/star_locations.html", {'locations': sorted_locations})
    return render(request, "star_site/star_locations.html", {'locations': ordered_locations})


def sort_by_distance(source, dest):
    url = 'https://maps.googleapis.com/maps/api/distancematrix/json?'
    r = requests.get(url + '&destinations = ' + dest +
                     'origins = ' + source +
                     '&key = ' + "AIzaSyDV6nqMJ7_iY1nU3reiUDrltej_Laf5BCw")
    result = r.json()
    print(result)
    return result['rows'][0]['elements'][0]["distance"]["value"]
