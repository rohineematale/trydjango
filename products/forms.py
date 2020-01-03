from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
	title					= forms.CharField(
											label='Name',
											widget=forms.TextInput(
												attrs={
													"placeholder": "Title Input"
												}
											)
										)
	email 				= forms.EmailField()
	description 	= forms.CharField(
										required=False, #by default require is true
										widget=forms.Textarea(
											attrs={
												"class": "class1 class2",
												"rows": 5,
												"cols": 75
											}
										)
									)
	price					= forms.DecimalField(initial=199.99)
	class Meta:
		model = Product
		fields = [
			'title',
			'description',
			'price',
			'summary',
			'email'
		 ]

	# add custom validation to check if title contains CFE string
	def clean_title(self, *args, **kwargs):
		title = self.cleaned_data.get("title")
		if not "CEF" in title:
			raise forms.ValidationError("Invalid title")
		return title

	def clean_email(self, *args, **kwargs):
		email = self.cleaned_data.get("email")
		if not email.endswith(".edu"):
			raise forms.ValidationError("This is not valid email")
		return email

class RawProductForm(forms.Form):
	title					= forms.CharField(
											label='Name',
											widget=forms.TextInput(
												attrs={
													"placeholder": "Title Input"
												}
											)
										)
	description 	= forms.CharField(
											required=False, #by default require is true
											widget=forms.Textarea(
												attrs={
													"class": "class1 class2",
													"rows": 5,
													"cols": 75
												}
											)
										)
	price					= forms.DecimalField(initial=199.99)