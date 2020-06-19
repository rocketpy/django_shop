from django.shortcuts import render
from . models import *


def index(request):
    return render(request, 'templ/base.html')


def about(request):
    return render(request, 'templ/about.html')


def services(request):
    return render(request, 'templ/services.html')


def contacts(request):
    return render(request, 'templ/contacts.html')


def items(request):
    return render(request, 'templ/item.html')


def notebooks(request):
    return render(request, 'templ/notebooks.html')


def tablets(request):
    return render(request, 'templ/tablets.html')


def smartphones(request):
    return render(request, 'templ/smartphones.html')


def cart(request):
    return render(request, 'templ/cart.html')


def login(request):
    return render(request, 'templ/cart.html')


def logout(request):
    return render(request, 'templ/cart.html')


def product(request, product_id):
    prod = Product.name.get(id=product_id)

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
