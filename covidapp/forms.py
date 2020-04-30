from django import forms
import datetime
from .models import Hospital


class HospitalForm(forms.ModelForm):
	date_time   			= forms.DateField(initial=datetime.date.today)
	hospitalCurrently 		= forms.CharField()
						# 			required=False, 
						# 			widget=forms.Textarea(
						# 		  	attrs={
						# 		  		"cols": 20, "rows":5,
						# 		  		"placeholder": "your description",
						# 		  		"class": "new-class-name two",
						# 		  		"id": "my-id-for-textarea",
						# 		  		# "rows": 20,
						# 		  		# "cols": 26,
						# 		  	}
						# 	)
						# )
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

	