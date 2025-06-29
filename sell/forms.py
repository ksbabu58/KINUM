# forms.py
from django import forms
from .models import Product, ProductMedia

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'description', 'price', 'category', 'condition', 'location', 'price_negotiable', 'brand']

class ProductMediaForm(forms.Form):
    file = forms.FileField(required=False)

