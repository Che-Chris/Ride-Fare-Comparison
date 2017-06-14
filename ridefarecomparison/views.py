import geocoder

from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from config import *
from functions import *

# Create your views here.
def index(request):
    return render(request, "home.html", {'google_api': GOOGLE_API_KEY})

@csrf_exempt
def results(request):
    pickup = request.POST.get("PickupLocation")
    dropoff = request.POST.get("DropoffLocation")
    seats = request.POST.get("SeatCount")

    pickup_lat, pickup_long = geocoder.google(pickup).latlng
    dropoff_lat, dropoff_long = geocoder.google(dropoff).latlng

    uber_prices = getUberPrice(pickup_lat, pickup_long, dropoff_lat, dropoff_long, seats)

    return render(request, "results.html", {'uber_prices': uber_prices})
