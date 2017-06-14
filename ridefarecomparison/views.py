from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from . import config

# Create your views here.
def index(request):
    return render(request, "home.html", {'google_api': config.GOOGLE_API_KEY})

@csrf_exempt
def results(request):
    pickup = request.POST.get("PickupLocation")
    dropoff = request.POST.get("DropoffLocation")
    return render(request, "results.html", {'pickup': pickup, 'dropoff': dropoff})
