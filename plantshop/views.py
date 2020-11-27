from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate ,logout
from django.contrib.auth import login as auth_login
from math import ceil


def index(request):
    return render(request,'index.html')


def about(request):
    return render(request,'about.html')



def blog(request):
    return render(request,'blog.html')



def cart(request):
    return render(request,'cart.html')


def checkout(request):
    return render(request,'checkout.html')


def contact(request):
    return render(request,'contact.html')



def portfolio(request):
    return render(request,'portfolio.html')



def shop(request):
    return render(request,'shop.html')



def shopdetails(request):
    return render(request,'shop-details.html')




def singleportfolio(request):
    return render(request,'single-portfolio.html')


def singlepost(request):
    return render(request,'single-post.html')



def basic(request):
    return render(request,'basic.html')