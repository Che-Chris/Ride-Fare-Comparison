from django.shortcuts import render, HttpResponse
from . import config

# Create your views here.
def index(request):
    return render(request, "home.html", {'google_api': config.GOOGLE_API_KEY})

def prices(request):
    return render(request, "results.html")
