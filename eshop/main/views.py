from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.http import HttpResponse
from main.models import Product, Review
from main.forms import ProductForm, UserRegistrationForm, UserLoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from main.constans import PAGE_SIZE
from django.views import View
from django.views.generic import ListView, DetailView

def logout_view(request):
    logout(request)
    return redirect('/')

class AuthorizationView(View):
    def get(self, request, *args, **kwargs):
        form = UserLoginForm()
        return render(request, template_name='authorization.html', context={'form': form})

    def post(self, request, *args, **kwargs):
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/authorization/')
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

class ProductListView(ListView):
    model = Product
    template_name = 'index.html'
    paginate_by = PAGE_SIZE
    

    def get_queryset(self):
        search_word = self.request.GET.get('search', '')
        queryset = super().get_queryset()
        queryset = queryset.filter(title__icontains=search_word)
        try:
            price_from = int(self.request.GET.get('price_from', 0))
        except:
            price_from = 0
        try:
            price_to = int(self.request.GET.get('price_to'))
        except:
            price_to = None
        if price_from:
            queryset = queryset.filter(price__gte=price_from)
        if price_to:
            queryset = queryset.filter(price__lte=price_to)
        return queryset
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        total_amount = Product.objects.all().count()
        buttons = total_amount // PAGE_SIZE
        if total_amount % PAGE_SIZE > 0:
            buttons+=1
        price_from = self.request.GET.get('price_from', '')
        price_to = self.request.GET.get('price_to', '')
        search_word = self.request.GET.get('search', '')
        context['price_from'] = price_from
        context['price_to'] = price_to
        context['search_word'] = search_word
        context['button_list'] = [str(i) for i in range(1, buttons+1)]
        context['page'] = self.request.GET.get('page', '1')
        return context
        

class ProductDetailView(DetailView):
    model = Product
    pk_url_kwarg = "id"
    template_name='product_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product_id = kwargs['object'].id
        context['rewies'] = Review.objects.filter(product_id=product_id)
        return context
