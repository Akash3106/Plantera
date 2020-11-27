"""plantshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('gallery', views.gallery, name='gallery'),
    path('shop-details/cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('contact/', views.contact, name='contact'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('single-portfolio/', views.singleportfolio, name='single-portfolio'),
    path('single-post/', views.singlepost, name='single-post'),
    path('eshop/', views.shop, name='shop'),
    path('basic/', views.basic, name='basic'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path("signup/signupp", views.handelSignup, name="handelSignup"),
    path("login/signin", views.handellogin, name="handellogin"),
    path("logout/", views.handellogot, name="handellogout"),
    path('shop-details/<int:myid>', views.shopdetails, name='shop-details')
]
