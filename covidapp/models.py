from django.db import models
from django.urls import reverse
import datetime

# Create your models here.

class Hospital(models.Model):
    date_time 			=    	models.DateField()
    hospital_currently 	= 		models.IntegerField(blank=True, null=True)
    icucurrently		= 		models.IntegerField(blank=True, null=True)
    hospital_increase 	= 		models.IntegerField(blank=True, null=True)
    dead_daily			= 		models.IntegerField(blank=True, null=True)
    tested_today		=		models.IntegerField(blank=True, null=True)

    def get_absolute_url(self):
    	return reverse("hospital-list", kwargs={"id": self.id}) #f"/products/{self.id}/"
    	#return f"/covidapp/{self.id}/"