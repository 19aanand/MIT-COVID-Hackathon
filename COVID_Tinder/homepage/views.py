from django.shortcuts import render
from . import generateCoordinates

def home(request):
    context = {
            "latitude":generateCoordinates.getLatitudeArray(),
            "longitude":generateCoordinates.getLongitudeArray()
        }
    return render(request, "homepage/home.htm", context)
    
