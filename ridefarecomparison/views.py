from django.shortcuts import render, HttpResponse
from . import config
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
    return render(request, "home.html", {'google_api': config.GOOGLE_API_KEY})

@csrf_exempt
def results(request):
    form = request.POST.get("PickupLocation")
    return render(request, "results.html", {'location': form})
