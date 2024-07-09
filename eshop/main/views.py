from django.shortcuts import render
from django.http import HttpResponse
from main.models import Product

def product_view(request):
    return render(request, template_name='index.html')

def main_page_view(request):
    products = Product.objects.all()
    print(products)
    context = {
        'product_list': products
    }
    return render(request, template_name='index.html', context=context)