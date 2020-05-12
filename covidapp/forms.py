from django import forms
import datetime
from .models import Hospital


class HospitalForm(forms.ModelForm):
	date_time   			= forms.DateField(initial=datetime.date.today)
	hospital_currently 		= forms.IntegerField(required=False)
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
	icucurrently   			= forms.IntegerField(required=False)
	hospital_increase       = forms.IntegerField(required=False)
	dead_daily				= forms.IntegerField(required=False)
	tested_today			= forms.IntegerField(required=False)

	class Meta:
		model = Hospital
		fields = [
			'date_time',
			'hospital_currently',
			'icucurrently',
			'hospital_increase',
			'dead_daily',
			'tested_today',
		]

	