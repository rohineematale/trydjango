from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
	class Meta:
		model = Product
		fields = [
			'title',
			'description',
			'price',
			'summary'
		 ]


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