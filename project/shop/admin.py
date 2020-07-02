from django.contrib import admin
from .models import Customer, ProductCategory, Product, CartItem, ShoppingCart


admin.site.register(Customer)
admin.site.register(ProductCategory)
admin.site.register(Product)
admin.site.register(CartItem)
admin.site.register(ShoppingCart)

