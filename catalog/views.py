from django.shortcuts import render
from .models import Product
from .forms import ProductForm, ProductModeratorForm
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.utils import timezone
from django.views.generic import DetailView, ListView, TemplateView, CreateView, DeleteView, UpdateView, View
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponseForbidden
from django.core.exceptions import PermissionDenied
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.core.cache import cache
from .services import get_products_in_category
from .models import Category


class CategoryListView(ListView):
    model = Category
    template_name = 'catalog/category_list.html'
    context_object_name = 'categories'


class ProductByCategoryListView(ListView):

    template_name = 'catalog/category_products.html'
    context_object_name = 'products'

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        return get_products_in_category(category_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_id = self.kwargs['category_id']
        context['category'] = Category.objects.get(pk=category_id)
        return context



class ProductCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:product_list')
    permission_required = 'catalog.add_product'

    def form_valid(self, form):
        form.instance.created_at = timezone.now().date()
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ContactView(TemplateView):
    template_name = 'catalog/contact.html'


@method_decorator(cache_page(60 * 15, key_prefix=lambda request: request.user.id), name='dispatch')
class ProductListView(ListView):
    model = Product
    template_name = 'catalog/product_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        queryset = cache.get('product_list')
        if not queryset:
            queryset = super().get_queryset()
            cache.set('product_list', queryset, 60 * 15)
        return queryset


@method_decorator(cache_page(60 * 15), name='dispatch')
class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'
    pk_url_kwarg = 'pk'


class ProductUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:product_list')
    permission_required = 'catalog.change_product'

    def form_valid(self, form):
        form.instance.updated_at = timezone.now().date()
        return super().form_valid(form)

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return ProductForm
        if user.has_perm('catalog.can_unpublish_product'):
            return ProductModeratorForm
        raise PermissionDenied


class ProductDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Product
    template_name = 'catalog/product_delete.html'
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('product_list')
    permission_required = 'catalog.delete_product'

    def get_form_class(self):
        user = self.request.user
        if not user.has_perm('catalog.delete_product') or not user == self.object.owner:
            raise PermissionDenied
