from django.urls import path
from . import views

app_name = 'star_site'
urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('star_locations', views.location_list, name='star_locations'),
    path('add_location', views.location_form, name='add_location'),

]