from django import forms

from .models import Article


class ArticleForm(forms.ModelForm):
	title 		= forms.CharField(label='', 
					widget=forms.TextInput(attrs={"placeholder": "pinga"}))
	content 		= forms.Content()
	active		 = forms.Boolean(
						required=False, 
						widget=forms.Textarea(
								  	attrs={
								  		"placeholder": "your description",
								  		"class": "new-class-name two",
								  		"id": "my-id-for-textarea",
								  		"rows": 20,
								  		"cols": 26,
								  	}
								)
						)
	price 		= forms.DecimalField(initial=2000.00)

	class Meta:
		model = Product
		fields = [
			'title',
			'description',
			'price'
		]

	def clean_title(self, *args, **kwargs):
		title = self.cleaned_data.get("title")
		if "CFE" in title:
			return title
		else:
			raise forms.ValidationError("this is not a valid title")

	def clean_email(self, *args, **kwargs):
		email = self.cleaned_data.get('email')
		if not email.endswith("edu"):
			raise forms.ValidationError("this is not a valid title")
		return email