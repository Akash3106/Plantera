from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate ,logout
from django.contrib.auth import login as auth_login
from .models import Product, relprod
from math import ceil


def index(request):
    return render(request,'index.html')


def about(request):
    return render(request,'about.html')



def gallery(request):
    return render(request,'gallery.html')



def cart(request):
    return render(request,'cart.html')


def checkout(request):
    return render(request,'checkout.html')


def contact(request):
    return render(request,'contact.html')



def portfolio(request):
    return render(request,'portfolio.html')



def shop(request):
    products = Product.objects.all()
    n = len(products)
    proinfo = {'range': range(1, n), 'product': products}
    return render(request,'shop.html',proinfo)


def shopdetails(request, myid):
    products = Product.objects.filter(id=myid)
    relate= relprod.objects.all()
    parama = {'product': products , 'relatepr':relate}
    return render(request, 'shop-details.html', parama)


def singleportfolio(request):
    return render(request,'single-portfolio.html')


def singlepost(request):
    return render(request,'single-post.html')



def basic(request):
    return render(request,'basic.html')

def signup(request):
    return render(request,'signup.html')


def handelSignup(request):
    if request.method =='POST':
        username=request.POST['Username']
        email=request.POST['Email']
        pass1=request.POST['Password']

        newuser=User.objects.create_user(username, email, pass1)
        newuser.save()
        return redirect('home')
    else:
        return HttpResponse("ERORR")


def login(request):
    return render(request,'login.html')


def handellogin(request):
    if request.method == 'POST':
        loginusername = request.POST['loUsername']
        loginpass1 = request.POST['loPassword']
        user=authenticate(username=loginusername,password=loginpass1)
        if user is not None:
            auth_login(request,user)
            return redirect('home')
        else:
            return HttpResponse("erorr")


def handellogot(request):
    logout(request)
    return redirect('home')