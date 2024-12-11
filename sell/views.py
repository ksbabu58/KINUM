from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm
from django.shortcuts import render, get_object_or_404
from .models import Product
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from sell.models import Product
from signin.models import UserProfile
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Product
@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user  # Set the user who uploaded the product
            product.save()
            return redirect('index')
        else:
            print(form.errors)
    else:
        form = ProductForm()
    return render(request, 'sell.html', {'form': form})

# views.py

def phones_category_view(request):
    products = Product.objects.filter(category='Mobile')  # Adjust the category name as needed
    return render(request, 'output.html', {'products': products})
def laptop(request):
    products = Product.objects.filter(category='laptops')
    return render(request,'output.html',{'products':products})
def tablet(request):
    products = Product.objects.filter(category='tablets')
    return render(request,'output.html',{'products':products})

def product_detail(request, product_id): 
    product = get_object_or_404(Product, id=product_id) 
    return render(request, 'buy_now.html',{'product':product}) 
# views.py
@login_required
def checkout_view(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    return render(request, 'buy_now.html')

def sell_veiw(request):

    return render(request,'sell.html')
def cars_category(request):
    products = Product.objects.filter(category='Car')
    return render(request,'output.html',{'products':products})
def furniture(request):
    products = Product.objects.filter(category='Home&Furniture')
    return render(request,'output.html',{'products':products})
# Create your views here.
