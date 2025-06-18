from django.shortcuts import render, redirect
from .forms import*
from django.contrib.auth import authenticate
from django.contrib.auth.models import auth

def index(request):
    return render(request, 'alyaqeen/index.html')

def my_login(request):
    form = LoginUserForm()
    if request.method == "POST":
        form = LoginUserForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('admin-dashboard')
    return render(request, 'alyaqeen/my-login.html', {'form': form})  # ✅ Make sure this is correct
