import imp
from math import prod
import re
from cv2 import log
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import login, logout,authenticate
from .models import *
from django.core.paginator import Paginator

# Create your views here.
context={}

def RegistrationView(request):
    if request.method =="GET":
        return render(request,'registration.html')

    if request.method== "POST":
        first_name=request.POST['fname']
        last_name=request.POST['lname']
        email=request.POST['email']
        username=request.POST['username']
        password=request.POST['password']

        User.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            username=username,
            password=make_password(password),
        )
        return render(request,'login.html')


def Login(request):
    next=""
    if request.method == "GET":
        if request.user.is_authenticated:
            if next:
                return redirect(next)
            else:
                return redirect('home')
        return render(request,'login.html')

    if request.method =="POST":
        username=request.POST['username']
        password=request.POST['password']
        next=request.POST.get('next')

        user=authenticate(username=username,password=password)
        if user:
            login(request,user)
            if next:
                return redirect(next)
            else:
                return render(request,'home.html')
        else:
            print("in else")
            return render(request,'login.html',{'msg':"Credential Wrong"})


def logout_view(request):
    logout(request)
    return redirect('login')


def home(request):
    return render(request,'home.html')

def ProductView(request):
    return render(request,'product.html')

def ProductListView(request):
    product =ProductModel.objects.all()
    pagen_no=request.GET.get('page',1)
    p = Paginator(product, 2)
    
    try:
        page=p.page(pagen_no)
    except:
        page=p.page(1)

    context['product']=page
    return render(request,'product_list.html',context)


def ProductUpdateView(request,id):
    context['product']=ProductModel.objects.get(id=id)
    return render(request,'product_update.html',context)