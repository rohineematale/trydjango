from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ProductForm, RawProductForm
from .models import Product

def product_list_view(request):
	products = Product.objects.all()
	context = {
		"products": products
	}
	return render(request, "products/index.html", context)

# default Django form
def product_new_view(request):
	initial_data = {
		"title": "sample text for intial data"
	}
	form = ProductForm(request.POST or None, initial=initial_data)
	if form.is_valid():
		form.save()
		form = ProductForm()
	context = {
		'form': form
	}
	return render(request, "products/new.html", context)

def product_edit_view(request,id):
	# obj = Product.objects.get(id=id)
	# obj = get_object_or_404(Product, id=id)
	try:
		obj = Product.objects.get(id=id)
	except Product.DoesNotExist:
		raise Http404
	form = ProductForm(request.POST or None, instance=obj)
	if form.is_valid():
		form.save()
		product_context = {"product": obj }
		return redirect("/products/{0}/show".format(id))
	else: 
		context = {'form': form}
		return render(request, "products/edit.html".format(id), context)

# raw html form
# def product_new_view(request):
# 	# context = {}
# 	# print(request.POST)
# 	# return render(request, "products/new.html", context)
# 	product_form = RawProductForm()
# 	if request.method == 'POST':
# 		product_form = RawProductForm(request.POST)
# 		if product_form.is_valid():
# 			print(product_form.cleaned_data)
# 			#Product.objects.create(title=request.POST['title'])
# 			Product.objects.create(**product_form.cleaned_data)
# 		else:
# 			print(product_form.errors)
# 	context = {"form": product_form}
# 	return render(request, "products/new.html", context)

# Create your views here.
def product_detail_view(request, id):
	obj = Product.objects.get(id=id)
	product_context = {
		"product": obj
	}
	return render(request, "products/show.html", product_context)

# def contact_view(request, *args, **kwargs):
# 	return render(request, "contact.html", {})

# def about_view(request, *args, **kwargs):
# 	return render(request, "about.html", {})