from django.shortcuts import render
from django.http import HttpResponse, Http404# responsible for returning a response to a user
import datetime as dt
from .models import Image,Location,Photographer,Category


def index(request):
    images = Image.get_all_images()
    locations = Location.objects.all()
    title = 'Blair-creations'

    return render(request, 'index.html', {'title':title, 'images':images, 'locations':locations})




def single(request,category_name,image_id):
    # images = Image.get_image_by_id(image_id)
    title = 'Image'
    locations = Location.objects.all()
    # category = Category.get_category_id(id = image_category)
    image_category = Image.objects.filter(image_category__name = category_name)
    try:
        image = Image.objects.get(id = image_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"single.html",{'title':title,"image":image, "locations":locations, "image_category":image_category})
