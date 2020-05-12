from django import forms
import datetime
from .models import Hospital


class HospitalForm(forms.Form):
	date_time   			= forms.DateField(initial=datetime.date.today)
	hospitalCurrently 		= forms.IntegerField()
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
	icucurrently   			= forms.IntegerField()
	hospitalIncrease       	= forms.IntegerField()
	deadDaily				= forms.IntegerField()
	testedToday				= forms.IntegerField()

	class Meta:
		model = Hospital
		fields = [
			'date_time',
			'hospitalCurrently',
			'icucurrently',
			'hospitalIncrease',
			'deadDaily',
			'testedToday',
		]

	