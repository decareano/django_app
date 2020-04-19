# Create your models here.

from django.db import models

class Page(models.Model):
    first_page = models.CharField(max_length=30)
    last_page = models.CharField(max_length=30)
    middle_page = models.CharField(max_length=30)
