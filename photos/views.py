from django.shortcuts import render
from django.http import HttpResponse, Http404# responsible for returning a response to a user
import datetime as dt
from .models import Image,Location,Photographer,Category


def index(request):
    images = Image.get_all_images()
    locations = Location.objects.all()
    title = 'Blair-creations'

    return render(request, 'index.html', {'title':title, 'images':images, 'locations':locations})