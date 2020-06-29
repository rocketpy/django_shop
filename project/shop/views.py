from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import *


def index(request):
    return render(request, 'templ/base.html')


def about(request):
    return render(request, 'templ/about.html')


def services(request):
    return render(request, 'templ/services.html')


def contacts(request):
    return render(request, 'templ/contacts.html')


def notebooks(request):
    return render(request, 'templ/notebooks.html')


def tablets(request):
    return render(request, 'templ/tablets.html')


def smartphones(request):
    return render(request, 'templ/smartphones.html')


def cart(request):
    return render(request, 'templ/cart.html')


def category(request):
    products = ProductCategory.name.all()
    context = {
        'customCSS': '/static/css/product_list.min.css',
        'title': ProductCategory.name,
        'products': products,
    }
    return render(request, 'templ/main.html', context)


def register_page(request):
    form = UserCreationForm()
    context = {'form': form}
    return render(request, 'templ/register.html', context)


def login_page(request):
    context = {}
    return render(request, 'templ/login.html', context)


def logout(request):
    return render(request, 'templ/main.html')


def product(request, product_id):
    # products = Product.objects.all()
    prodt = Product.objects.get(id=product_id)

    session_key = request.session.session_key
    
    if not session_key:
        # request.session["session_key"] = 123 
        request.session.cycle_key()
    print(request.session.session_key)
    return render(request, 'products/product.html', locals())


"""
# get User id from auth_user table
from django.contrib.auth.models import User

User.objects.get(username=the_username).pk
"""
