from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CreateUserForm
# Create your views here.


def login_view(request):
    """Render HTTML page"""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('gallaryHomePage')
        else:
            messages.info(request, "Username and password incorrect")
    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    return redirect('loginPage')


def register_view(request):
    """Render HTTML page"""
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, "Account was created for "+ user)
            return redirect('loginPage')

    context = {'form': form}
    return render(request, 'register.html', {'data': context})
