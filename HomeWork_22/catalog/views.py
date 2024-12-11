from django.shortcuts import render, get_object_or_404

from .models import Product


def home(request):
    return render(request, 'catalog/home.html')


def contact(request):
    return render(request, 'catalog/contact.html')


def product_list(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'catalog/product_list.html', context)


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {'product': product}
    return render(request, 'catalog/product_detail.html', context)

