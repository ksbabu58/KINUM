from django.contrib import admin
from .models import Product, Wishlist, ProductMedia, Cart, CartItem

admin.site.register(Product)
admin.site.register(ProductMedia)
admin.site.register(Wishlist)
admin.site.register(Cart)
admin.site.register(CartItem)
