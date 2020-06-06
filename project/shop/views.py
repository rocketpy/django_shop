from django.shortcuts import render
# from django.template.response import TemplateResponse


def index(request):
    return render(request, 'templ/base.html')

# def index(request):
#    return TemplateResponse(request,  "shop/base.html")

