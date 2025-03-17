from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# Create your views here.


def RegisterUser(request):
    if request.method == "POST":
        form_data = UserCreationForm(request.POST)
        if form_data.is_valid():
            form_data.save()
            messages.success(request, 'User successfully created!')
            return redirect('login_user')
    create_user = UserCreationForm()
    return render(request, 'auth_app/register.html', context={'create_user':create_user})


def LoginUser(request):
    if request.method == 'POST':
        formd_data = AuthenticationForm(data = request.POST)
        print("-------========-------")
        if formd_data.is_valid():
            print("{[[[[[[[]]]]]]]}")
            username = request.cleaned_data('username')
            passwaord = request.cleaned_data('passwaord')
            
            print(username, passwaord)
    forms = AuthenticationForm()
    return render(request, 'auth_app/login.html', context={'forms':forms})