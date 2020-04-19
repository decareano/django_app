from django import forms

class CommentForm(forms.Form):
   name = forms.CharField(label='marcelo')
   url = forms.URLField(label='www.myname.com', required=False)
   comment = forms.CharField()

f = CommentForm(auto_id=False)
print(f)
