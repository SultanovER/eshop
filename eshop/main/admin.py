from django.contrib import admin
from main.models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'price', 'is_active', 'created', 'updated']
    search_fields = ['title', 'description']
    list_filter = ['price', 'is_active', 'description', 'title']
    list_per_page = 20
    readonly_fields = ['created', 'updated']
admin.site.register(Product, ProductAdmin)