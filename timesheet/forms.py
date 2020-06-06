from django import forms

class CodeForm(forms.Form):
	unique_code = forms.IntegerField()
	


