from django.db import models
from django.db.models import Model 
# Create your models here.


class Image(models.Model):
    image = models.FileField(max_length=2555)