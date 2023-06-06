from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import RegisterForm, LoginForm

# Create your views here.
def register(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'register/register.html',{'form':form})
    
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request,'Successfully signed up!')
            login(request, user)
            return redirect('login')
        else:
            return render(request, 'register/register.html',{'form':form})

def sign_in(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('fileupload')

        form = LoginForm()
        return render(request, 'register/login.html', {'form':form})
    elif request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,username=username,password=password)
            
            if user:
                login(request, user)
                messages.success(request,f'Hi {username.title()}, welcome back!')
                return redirect('fileupload')
        
        messages.error(request,f'Invalid username or password')
        return render(request,'register/login.html',{'form':form})

def sign_out(request):
    logout(request)
    messages.success(request,f'You have been logged out.')
    return redirect('login')