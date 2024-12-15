from django.urls import path, include
from catalog.apps import CatalogConfig
from catalog.views import home, contact, product_list, product_detail

app_name = CatalogConfig.name

urlpatterns = [
    # path('', home, name='home'),
    path('contact/', contact, name='contact'),
    path('/', product_list, name='product_list'),
    path('<int:pk>', product_detail, name='product_detail')
]
