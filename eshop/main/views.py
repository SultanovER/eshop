from django.shortcuts import render
from django.http import HttpResponse
from main.models import Product, Review

def product_view(request):
    return render(request, template_name='index.html')

def main_page_view(request):
    products = Product.objects.all()
    print(products)
    context = {
        'product_list': products
    }
    return render(request, template_name='index.html', context=context)

def product_detail_view(request, id):
    product = Product.objects.get(id=id)
    reviews = Review.objects.filter(product=product)
    print(reviews)
    context = {
        'product': product,
        'reviews': reviews
    }
    return render(request, template_name='product.html', context=context)
