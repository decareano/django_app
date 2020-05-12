from django.db import models
from django.urls import reverse
import datetime

# Create your models here.

class Hospital(models.Model):
    date_time 			=    	models.DateField()
    hospital_currently 	= 		models.IntegerField(null=True)
    icucurrently		= 		models.IntegerField(null=True)
    hospital_increase 	= 		models.IntegerField(null=True)
    dead_daily			= 		models.IntegerField(null=True)
    tested_today		=		models.IntegerField(null=True)

    def get_absolute_url(self):
    	return reverse("hospital-list", kwargs={"id": self.id}) #f"/products/{self.id}/"
    	#return f"/covidapp/{self.id}/"