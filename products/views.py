from django.http import HttpResponse
from django.shortcuts import render
from .forms import ProductForm
from .models import Product

def product_new_view(request):
	form = ProductForm(request.POST or None)
	if form.is_valid():
		form.save()
		form = ProductForm()
	context = {
		'form': form
	}
	return render(request, "products/new.html", context)

# Create your views here.
def product_detail_view(request, *args, **kwargs):
	obj = Product.objects.get(id=2)
	product_context = {
		"product": obj
	}
	return render(request, "products/show.html", product_context)

# def contact_view(request, *args, **kwargs):
# 	return render(request, "contact.html", {})

# def about_view(request, *args, **kwargs):
# 	return render(request, "about.html", {})