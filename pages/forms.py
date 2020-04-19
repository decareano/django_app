from django import forms

from .models import Page


class PageForm(forms.ModelForm):
	first_name 		= forms.CharField(label='', 
					widget=forms.TextInput(attrs={"placeholder": "pinga"}))
	# middle_name 		= forms.EmailField()
	# last_name = forms.CharField(
	# 					required=False, 
	# 					widget=forms.Textarea(
	# 							  	attrs={
	# 							  		"placeholder": "your description",
	# 							  		"class": "new-class-name two",
	# 							  		"id": "my-id-for-textarea",
	# 							  		"rows": 20,
	# 							  		"cols": 26,
	# 							  	}
	# 							)
	# 					)
	# price 		= forms.DecimalField(initial=2000.00)

	class Meta:
		model = Page
		fields = [
			'first_name',
			'middle_name',
			'last_name'
		]

	# def clean_title(self, *args, **kwargs):
	# 	title = self.cleaned_data.get("title")
	# 	if "CFE" in title:
	# 		return title
	# 	else:
	# 		raise forms.ValidationError("this is not a valid title")

	# def clean_email(self, *args, **kwargs):
	# 	email = self.cleaned_data.get('email')
	# 	if not email.endswith("edu"):
	# 		raise forms.ValidationError("this is not a valid title")
	# 	return email