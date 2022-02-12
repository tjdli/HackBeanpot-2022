from django.shortcuts import render

# Create your views here.
from django.utils import timezone
from django.views import generic

from .models import Location


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
    locations = Location.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')
    return render(request, "star_site/star_locations.html", {'locations': locations})
