from django.db import models
# models.py
from django.db import models
from django.contrib.auth.models import User

from signin.models import UserProfile

class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images/')
    category = models.CharField(max_length=50)
    condition = models.CharField(max_length=50)
    location = models.CharField(max_length=255)
    price_negotiable = models.BooleanField()
    brand = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Links to the User model
    def __str__(self):
        return self.title

# Create your models here.
