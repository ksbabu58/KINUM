from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.shortcuts import render, redirect
from .models import Product, ProductMedia
from .forms import ProductForm, ProductMediaForm
from django.shortcuts import render, get_object_or_404
from .models import Product
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from sell.models import Product
from signin.models import UserProfile
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
  # Remove this if you're manually handling CSRF tokens in the frontend
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Product, Wishlist
import json
from django.shortcuts import get_object_or_404, redirect
from .models import Product, Cart, CartItem
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Product, Wishlist
import json

@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)

        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user  # Set the user who uploaded the product
            product.save()

            media_files = request.FILES.getlist('file')
            for file in media_files:
                file_type='image' if file.content_type.startswith('image') else 'video'
                ProductMedia.objects.create(
                    product=product, 
                    file=file, 
                    file_type=file_type,
                )
            return redirect('index')
        else:
            print(form.errors)
    else:
        form = ProductForm()
        media_form = ProductMediaForm()

    return render(request, 'sell.html', {'form': form, 'media_form': media_form})

# views.py

def phones_category_view(request):
    products = Product.objects.filter(category='Mobile')  # Adjust the category name as needed
    return render(request,'output.html',{'products':products})

def electronics(request):
    products = Product.objects.filter(category='Mobile')
    return render(request,'output.html',{'products':products})

def vehicles(request):
    products = Product.objects.filter(category='vehicles')
    return render(request,'output.html',{'products':products})

def furniture(request):
    products = Product.objects.filter(category='furniture')
    return render(request,'output.html',{'products':products})

def realestate(request):
    products = Product.objects.filter(category='realestate')
    return render(request,'output.html',{'products':products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'buy_now.html', {'product': product})

def checkout_view(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'buy_now.html')


def sell_veiw(request):
    return render(request,'sell.html')

def cars_category(request):
    products = Product.objects.filter(category='Car')
    return render(request,'output.html',{'products':products})

def detail_view(request, product_id):
    product = Product.objects.get(id=product_id)  # Fetch the product
    media_files = product.media.all()  # Fetch related media files
    return render(request, 'swipable.html', {'product': product, 'media_files': media_files})
import json
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from .models import Product, Wishlist

@login_required
@require_POST
def toggle_wishlist(request):
    # Parse the JSON body
    data = json.loads(request.body)
    product_id = data.get('product_id')
    response = {}

    try:
        product = Product.objects.get(id=product_id)
        wishlist_item, created = Wishlist.objects.get_or_create(user=request.user, product=product)

        if not created:
            # The item was already in the wishlist, so remove it.
            wishlist_item.delete()
            response['in_wishlist'] = False
        else:
            # The item was not in the wishlist, so now it is added.
            response['in_wishlist'] = True

        return JsonResponse(response)
    except Product.DoesNotExist:
        return JsonResponse({'error': 'Product not found.'}, status=404)
 
from django.shortcuts import render
from .models import Wishlist

def wishlist(request):
    wishlist_items = Wishlist.objects.filter(user=request.user)
    return render(request, 'wishlist.html', {'wishlist': [item.product for item in wishlist_items]})



def cart_view(request):
    cart, _ = Cart.objects.get_or_create(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})


def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, _ = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += 1
    cart_item.save()
    return redirect('cart_view')

from django.db.models import Q

def search_products(request):
    query = request.GET.get('query')  # Get the search query
    if query:
        products = Product.objects.filter(
            Q(title__icontains=query) | Q(category__icontains=query)
        )  # Search in both title and category
    else:
        products = Product.objects.none()  # Return empty queryset if no query
    return render(request, 'output.html', {'products': products})
