from django.urls import path
from . import views

app_name = 'star_site'
urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    # path('star_locations', views.StarLocationsView.as_view(), name='star_locations'),
    path('star_locations', views.location_list, name='location_list'),
]