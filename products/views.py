from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from products.models import Product

def home_view(request):
    print(request)
    return HttpResponse('<h1>Hello World</h1>')

def index_view(request):
    return render(request,'products/index.html',{})

def template_view(request):
    return render(request, 'products/home.html', {})

def extended_view(request):
    return render(request, 'products/extended.html', {
        'products': Product.objects.all
    })

def contexted_view(request):
    return render(request,'products/contexted.html',{
        'name': 'Kevin',
        'account': 20,
        'isAdult': True,
        'languages': ['python','web dev','android dev']
    })
