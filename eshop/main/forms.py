from typing import Any
from django.forms import ModelForm, Form
from main.models import Product
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class UserLoginForm(Form):
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите имя'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Введите пароль'}))

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if not user:
            raise forms.ValidationError('Ошибка')
        return self.cleaned_data

class UserRegistrationForm(Form):
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите имя'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Введите пароль'}))
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Подтвердите пароль'}))

    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 != password2:
            raise forms.ValidationError('Пароли не совпадают!')
        return password2



    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError('Такой пользователь уже существует!')
    
class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = 'title price sizes description'.split()
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'sizes': forms.CheckboxSelectMultiple()
        }