from django.shortcuts import render

# Create your views here.
from django.views import generic


class HomePageView(generic.TemplateView):
    template_name = "star_site/home.html"