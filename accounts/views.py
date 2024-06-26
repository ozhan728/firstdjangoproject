from django.shortcuts import render
from django.template.context_processors import request

# from django.http import HttpResponse
# Create your views here.
from .forms import UserRegistrationForm , UserLoginForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render , redirect
from django.contrib.auth import authenticate , login , logout


def user_register(request) :
    if request.method == 'POST' :
        form = UserRegistrationForm(request.POST)
        if form.is_valid() :
            cd = form.cleaned_data
            user = User.objects.create_user(cd['username'],cd['email'],cd['password'])
            user.first_name = cd['first_name']
            user.last_name = cd['last_name']
            user.save()
            messages.success(request,'user registered successfully','success')
            return redirect('home')

    else :
        form = UserRegistrationForm()
    return render(request,'register.html',{'form':form})

def user_login(request) :
    if request.method == 'POST' :
        form = UserLoginForm(request.POST)
        if form.is_valid() :
            cd = form.cleaned_data
            user = authenticate(request,username=cd['username'],password=cd['password'])
            if user is not None :
                login(request,user)
                messages.success(request,'logged in success','success')
                return redirect('home')
            else :
                messages.error(request,'user or pass is wrong','danger')
                return redirect('home')

    else :
        form = UserLoginForm()
        return render(request,'login.html',{'form':form})


def user_logout(request) :
    logout(request)
    messages.success(request,'logged out','success')
    return redirect('home')