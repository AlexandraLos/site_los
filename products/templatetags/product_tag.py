from django import template
from products.models import Category, Product

register = template.Library()


@register.simple_tag()
def get_categories():
    """Вывод всех категорий"""
    return Category.objects.all()


@register.inclusion_tag('products/tags/last_product.html')
def get_last_products(count=3):
    products = Product.objects.order_by("-id")[:count]
    return {"last_products": products}
