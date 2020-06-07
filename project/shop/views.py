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

# def index(request):
#    return TemplateResponse(request,  "shop/base.html")

