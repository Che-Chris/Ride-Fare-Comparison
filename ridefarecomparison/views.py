import requests
import geocoder

from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from . import config
from . import functions

# Create your views here.
def index(request):
    return render(request, "home.html", {'google_api': config.GOOGLE_API_KEY})

@csrf_exempt
def results(request):
    pickup = request.POST.get("PickupLocation")
    dropoff = request.POST.get("DropoffLocation")

    geo_pickup = geocoder.google(pickup).latlng
    geo_dropoff = geocoder.google(dropoff).latlng

    return render(request, "results.html", {'pickup': pickup, 'dropoff': dropoff, 'geo_pickup': geo_pickup, 'geo_dropoff': geo_dropoff})
