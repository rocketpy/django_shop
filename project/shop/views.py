from django.shortcuts import render


def index(request):
    return render(request, 'templ/base_html.html')
