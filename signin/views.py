from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_login
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib import messages
from .models import UserProfile
import requests
# Create your views here.
from django.shortcuts import render
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout
from django.contrib import messages
from django.shortcuts import redirect

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        recaptcha_response = request.POST.get('g-recaptcha-response')

        if not username or not password:
            messages.error(request, 'Please enter both username and password.')
            return redirect('login')

        # Verify reCAPTCHA
        data = {
            'secret': settings.RECAPTCHA_SECRET_KEY,
            'response': recaptcha_response
        }
        r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
        result = r.json()

        if not result.get('success'):
            messages.error(request, 'Invalid reCAPTCHA. Please try again.')
            return redirect('login')

        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('index')
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('login')

    return render(request, 'login.html')

    # Your login logic here


def register_view(request):
    if request.method == 'POST':
        
        username = request.POST['username']
        f_name = request.POST['f_name']
        l_name = request.POST['l_name']
        password = request.POST['password']
        email = request.POST['email']
        dob = request.POST['dob']
        sex = request.POST['sex']
        phone = request.POST['phone']
        profile_pic = request.FILES.get('profile_pic')

        # Check if user already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return redirect('register')
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists.')
            return redirect('register')

        # Create new user
        user = User.objects.create_user(username=username, password=password, email=email)
        
        # Create user profile
        UserProfile.objects.create(user=user, dob=dob, sex=sex, phone=phone,f_name=f_name,l_name=l_name, profile_pic=profile_pic)
        
        # Automatically log in the user after registration
        auth_login(request, user)
        messages.success(request, 'Registration successful!')
        return redirect('index')

    return render(request, 'register.html')


def logout_view(request):
    auth_logout(request)
    messages.success(request, 'You have been logged out successfully!')
    return redirect('login')  # Redirect to the login page after logging out



def index_veiw(request):
    return render(request, 'index.html')

from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from .models import UserProfile  # Assuming dob is stored in a related model
from django.shortcuts import render
from django.contrib.auth.models import User  # Assuming you're using Django's default User model
from django.shortcuts import render
from .models import UserProfile

def reset_pw(request):
    if request.method == 'POST': 
        uname = request.POST['username']
        dob = request.POST['date_of_birth']
        new_pass = request.POST.get('password1')
        confirm_pass = request.POST.get('password2')
        # Check if the username and date of birth match
        try:
            user_profile = UserProfile.objects.get(user__username=uname)  # Retrieve UserProfile by username
            if str(user_profile.dob) == dob:  # Compare dob (convert to string for match)
                # Success: User found and DOB matches
                if new_pass != confirm_pass:
                    messages.error(request, "Passwords do not match.")
                    return redirect('password_reset')
                elif new_pass== confirm_pass:
                    user_profile.user.password = make_password(new_pass)  # Hash the password
                    user_profile.user.save()  # Save the changes to the User model
                    return render(request, 'index.html', {'user_profile': user_profile})
            else:
                # DOB does not match
                return render(request, 'forgot.html', {'error': 'Date of birth does not match!'})
        except UserProfile.DoesNotExist:
            # UserProfile not found for the given username
            return render(request, 'forgot.html', {'error': 'User not found!'})

    # Render the reset password page if GET method
    return render(request, 'forgot.html')

def profile_view(request):
    return render(request,'profile.html')

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import UserProfile  # Import your UserProfile model

@login_required
def profile_edit(request):
    if request.method == 'POST':
        user_profile = request.user.userprofile  # Get the logged-in user's profile
        user_profile.f_name = request.POST.get('first_name')
        user_profile.l_name = request.POST.get('last_name')
        user_profile.phone = request.POST.get('mobile')
        user_profile.dob = request.POST.get('dob')

        # Handle file upload for profile picture
        if 'profile_pic' in request.FILES:
            user_profile.profile_pic = request.FILES['profile_pic']
        
        user_profile.save()  # Save changes to the database
        return redirect('profile')  # Redirect to a profile view or any other page

    return render(request, 'edit_profile.html')  # Render the form template

'''
def home(request):
    if request.user.is_authenticated:
        return render(request,"home.html")
    else:
         return redirect('/signin')

def signin(request):
    if request.user.is_authenticated:
         return redirect('')
    else:
        if request.method=="POST":
            uname= request.POST['username']
            pword= request.POST['password']
            user=authenticate(username=uname,password=pword)
            if user is not None:
                login(request,user)
            else:
                return redirect('/signin')
        else:
            return render(request,"home.html")

'''