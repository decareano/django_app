from django import forms
import datetime
from .models import Hospital


class HospitalForm(forms.ModelForm):
	date_time   			= forms.DateField(initial=datetime.date.today)
	hospitalCurrently 		= forms.CharField()
	ICUcurrently   			= forms.CharField()
	hospitalIncrease       	= forms.CharField()
	deadDaily				= forms.CharField()
	testedToday				= forms.CharField()

	class Meta:
		model = Hospital
		fields = [
			'date_time',
			'hospitalCurrently',
			'ICUcurrently',
			'hospitalIncrease',
			'deadDaily',
			'testedToday',
		]

	