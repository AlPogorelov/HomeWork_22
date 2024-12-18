from django.urls import path, include
from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ProductDetailView, ContactView


app_name = CatalogConfig.name

urlpatterns = [
    path('contact/', ContactView.as_view(), name='contact'),
    path('', ProductListView.as_view(), name='product_list'),
    path('<int:pk>', ProductDetailView.as_view(), name='product_detail'),
]
