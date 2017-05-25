from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    foo = "Hello Zachery!"
    return render(request, "home.html", {'message': foo})
