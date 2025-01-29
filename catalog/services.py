
from .models import Category, Product


def get_products_in_category(category_id):

    return Product.objects.filter(category_id=category_id)