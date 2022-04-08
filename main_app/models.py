from django.db import models
from django.urls import reverse

# Create your models here.
class Widget(models.Model):
    description = models.CharField(max_length=650)
    quantity = models.IntegerField()
    
    def get_absolute_url(self):
        return reverse("create")
    