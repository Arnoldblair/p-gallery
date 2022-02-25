from django.db import models
from pyuploadcare.dj.models import ImageField

# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length =50)
