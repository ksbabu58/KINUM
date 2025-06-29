"""
URL configuration for kinum project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.urls import path
from signin.views import *

from sell.views import *
# urls.py
from django.conf import settings
from django.conf.urls.static import static
from sell.views import product_detail


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',login_view,name='login'),
    path('',login_view, name='login'),
    path('index/',index_veiw, name='index'),
    path('register/',register_view,name='register'),
    path('sell/',sell_veiw,name='sell'),
    path('sell/add/',add_product,name='add_product'),
    path('logout/', logout_view, name='logout'),
    path('cars/',cars_category,name='cars_category'),
    path('furniture/',furniture,name='furniture'),
    path('realestate/',realestate,name='realestate'),
    path('phones/', phones_category_view, name='phones_category'), 
    path('electronics/',electronics,name='electronics'),
    path('vehicles/',vehicles, name='vehicles'),
    path('product/<int:product_id>/', product_detail, name='product_detail'),
    path('checkout/<int:product_id>/', checkout_view, name='checkout'),
    path('password_reset/',reset_pw,name='password_reset'),
    path('datails/<int:product_id>/', detail_view, name='detail_view'),
    path('wishlist/toggle/',toggle_wishlist, name='toggle_wishlist'),
    path('wishlist/',wishlist, name='wishlist'),
    path('profile/',profile_view,name='profile'),
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('cart/', cart_view, name='cart_view'),
    path('search/', search_products, name='search_products'),
    path('edit/', profile_edit, name='edit_profile'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
