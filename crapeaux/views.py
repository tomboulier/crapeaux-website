from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, "crapeaux/index.html")


def apropos(request):
    return render(request, "crapeaux/a-propos.html")


def calendrier(request):
    return en_construction(request)


def blog(request):
    return en_construction(request)


def contact(request):
    return en_construction(request)


def en_construction(request):
    return render(request, "crapeaux/en-construction.html")


def page_not_found_view(request, exception):
    return render(request, 'crapeaux/404.html', status=404)
