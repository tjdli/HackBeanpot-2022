from django.urls import path
from . import views

app_name = 'star_site'
urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
]