from django.db import models
from django.urls import reverse
import datetime

# Create your models here.

class Hospital(models.Model):
    date_time 			=    	models.DateField()
    hospital_currently 	= 		models.IntegerField()
    ICU_currently		= 		models.IntegerField()
    hospital_increase 	= 		models.IntegerField()
    dead_daily			= 		models.IntegerField()
    tested_today		=		models.IntegerField()

    def get_absolute_url(self):
    	return reverse("hospital-list", kwargs={"id": self.id}) #f"/products/{self.id}/"
    	#return f"/covidapp/{self.id}/"