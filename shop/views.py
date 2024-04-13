import requests
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from .models import Product, Developer
from .services import add_model
from django.template.defaultfilters import slugify

def show_all_products(request):
    data = {
        'products': Product.objects.all(),
        'developers': Developer.objects.all()
    }
    return render(request, 'index.html', context=data)


def add_product(request):
    kwargs = dict(request.POST.items())
    kwargs['developer'] = Developer.objects.all().filter(name=request.POST.get('developer'))[0]
    kwargs.pop('csrfmiddlewaretoken')
    kwargs['slug'] = slugify(kwargs['name'])
    add_model(Product, **kwargs)
    # return HttpResponse(f'{kwargs}')
    return show_all_products(HttpRequest())

def add_developer(request):
    name = request.POST.get('name')
    add_model(Developer, name=name)
    return show_all_products(request)
