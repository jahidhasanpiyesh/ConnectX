from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Index view
def index(request):
    return render(request, 'index.html')

# Registration view
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created successfully! You can now log in.')
            return redirect('login')  # Replace 'login' with your login URL name
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = RegisterForm()

    context = {
        'form': form
    }
    return render(request, 'register.html', context)

# Email-based login view
def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user_obj = User.objects.get(email=email)
            user = authenticate(request, username=user_obj.username, password=password)
        except User.DoesNotExist:
            user = None

        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome back, {user.first_name}!')
            return redirect('dashboard')  # Replace 'dashboard' with your home page or dashboard URL
        else:
            messages.error(request, 'Invalid email or password. Please try again.')

    return render(request, 'login.html')

# Optional: Logout view
def user_logout(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('login')

# Dashboard view
@login_required
def dashboard(request):
    full_name = f"{request.user.first_name} {request.user.last_name}".strip()
    return render(request, 'dashboard.html', {'name': full_name})


# Video call view
@login_required
def videocall(request):
    full_name = f"{request.user.first_name} {request.user.last_name}".strip()
    return render(request, 'videocall.html', {'name': full_name})


# Join room view
@login_required
def join_room(request):
    if request.method == 'POST':
        roomID = request.POST.get('roomID', '').strip()
        if roomID:
            # Use named URL for meeting; adjust as needed
            return redirect(f"/meeting?roomID={roomID}")
        else:
            messages.error(request, "Please enter a valid Room ID.")
            return redirect('join_room')
    return render(request, 'joinroom.html')