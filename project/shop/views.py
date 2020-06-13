from django.shortcuts import render
# from django.template.response import TemplateResponse


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
    return render(request, 'templ/.html')


# def index(request):
#    return TemplateResponse(request,  "shop/base.html")

