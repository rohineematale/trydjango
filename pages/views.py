from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
	return render(request, "home.html", {})

def contact_view(request, *args, **kwargs):
	return render(request, "contact.html", {})

def about_view(request, *args, **kwargs):
	context_params = {'test_arr_params': ['aboutus1', 'aboutus2', 'aboutus3', 100]}
	return render(request, "about.html", context_params)