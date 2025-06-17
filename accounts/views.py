from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login , logout
from django.contrib import messages
from django.contrib.auth.models import User
from allauth.account.auth_backends import AuthenticationBackend


def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome back, {user.username}!')
            return redirect('home')  # ya dashboard
        else:
            messages.error(request, 'Invalid email or password.')
    return render(request, 'accounts/login.html')



def signup_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        username = email
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, " Passwords do not match.")
        elif User.objects.filter(username=username).exists():
            messages.error(request, " User already exists.")
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            login(request, user)
            messages.success(request, " Signup successful!")
            return redirect('/')  # Go to homepage

    return render(request, 'accounts/signup.html')

def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect('home')
