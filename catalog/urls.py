from django.urls import path, include
from catalog.apps import CatalogConfig
from catalog.views import (ProductListView, ProductDetailView, ContactView, ProductUpdateView,
                           ProductDeleteView, ProductCreateView, CategoryListView, ProductByCategoryListView)


app_name = CatalogConfig.name

urlpatterns = [
    path('contact/', ContactView.as_view(), name='contact'),
    path('', ProductListView.as_view(), name='product_list'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('create/', ProductCreateView.as_view(), name='product_create'),
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('category/<int:category_id>/', ProductByCategoryListView.as_view(), name='category_products'),

]
