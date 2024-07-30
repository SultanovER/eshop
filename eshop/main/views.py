from django.shortcuts import render, redirect
from django.http import HttpResponse
from main.models import Product, Review
from main.forms import ProductForm, UserRegistrationForm, UserLoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required


def logout_view(request):
    logout(request)
    return redirect('/')

def authorization_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/authorization/')
    else:
        form = UserLoginForm
    return render(request, template_name='authorization.html', context={'form': form})


def registration_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            User.objects.create_user(username=username, password=password)
            return redirect('/')
    else:
        form = UserRegistrationForm()
    return render(request, template_name='registration.html', context={'form': form})

@login_required(login_url='/authorization')
def create_product_view(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    
    context = {
        'form': ProductForm()
    }
    return render(request, template_name='add.html', context=context)

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
