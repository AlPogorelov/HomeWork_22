from django.shortcuts import render
from .models import Product
from django.views.generic import DetailView, ListView, TemplateView


class ContactView(TemplateView):
    template_name = 'catalog/contact.html'


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/product_list.html'
    context_object_name = 'products'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'
    pk_url_kwarg = 'pk'
