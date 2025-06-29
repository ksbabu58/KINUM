from django.db import models
from django.conf import settings
from signin.models import User, UserProfile
class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50)
    condition = models.CharField(max_length=50)
    location = models.CharField(max_length=255)
    price_negotiable = models.BooleanField(default=False)
    brand = models.CharField(max_length=255)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Links to the User model
    created = models.DateTimeField(auto_now_add=True,blank=True)  # Track when the product was added

    def __str__(self):
        return self.title

class ProductMedia(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='media')
    file = models.FileField(upload_to='product_media/', null=True, blank=True)
    file_type = models.CharField(max_length=10, choices=[('image', 'Image'), ('video', 'Video')])

    def __str__(self):
        return f"{self.product.title} - {self.file_type}"


class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='wishlist')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    added_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'product')  # Prevent duplicate wishlist items

    def __str__(self):
        return f"{self.user.username} - {self.product.title}"


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  # Allow null values temporarily
    created_at = models.DateTimeField(auto_now_add=True)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

