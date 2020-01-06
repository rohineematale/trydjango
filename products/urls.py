# from django.contrib import admin
from django.urls import path
# from pages.views import home_view, contact_view, about_view
from .views import product_detail_view, product_new_view, product_edit_view, product_list_view

urlpatterns = [
    path('', product_list_view, name="products-list"),
    path('new', product_new_view, name="products-new"),
    path('<int:id>/edit', product_edit_view, name="products-edit"),
    path('<int:id>/show', product_detail_view, name="products-show")
]
