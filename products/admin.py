from django.contrib import admin
from .models import Category, Ingredient, Brand, Type, Product, ProductImages, Rating, RatingStar, Review

admin.site.register(Category)
admin.site.register(Ingredient)
admin.site.register(Brand)
admin.site.register(Type)
admin.site.register(Product)
admin.site.register(ProductImages)
admin.site.register(Rating)
admin.site.register(RatingStar)
admin.site.register(Review)
