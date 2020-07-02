from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.contrib import messages


def index(request):
    return render(request, 'templ/base.html')


def main(request):
    products = ProductCategory.name.all()
    elements = ProductCategory.name.count()
    context = {
               'customCSS': '/static/css/shop-homepage.css',
               'title': ProductCategory.name,
               'products': products,
               'elements': elements,
               }
    return render(request, 'templ/main.html', context)


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
               'customCSS': '/static/css/shop-homepage.css',
               'title': ProductCategory.name,
               'products': products,
               }
    return render(request, 'templ/main.html', context)


def register_page(request):
    # form = UserCreationForm()
    # context = {'form': form}
    if request.user.is_authenticated:
        return redirect('main')
    else:
        form = UserCreationForm()
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)

                return redirect('login')

        context = {'form': form}
        return render(request, 'accounts/register.html', context)
    # return render(request, 'templ/register.html', context)


def login_page(request):
    # context = {}
    if request.user.is_authenticated:
        return redirect('main')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('main')
            else:
                messages.info(request, 'Username or password is incorrect')

        context = {}
        return render(request, 'accounts/login.html', context)
    #breturn render(request, 'templ/login.html', context)


def logout(request):
    logout(request)
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
