from django.contrib import admin
from main.models import Product, Review, Size

class ReviewInLine(admin.StackedInline):
    model = Review
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    inlines = [ReviewInLine]
    list_display = ['title', 'description', 'price', 'is_active', 'created', 'updated']
    search_fields = ['title', 'description']
    list_filter = ['sizes', 'price', 'is_active', 'description', 'title']
    list_per_page = 20
    readonly_fields = ['created', 'updated']

class ReviewAdmin(admin.ModelAdmin):
    list_display = 'author text stars product product_id'.split()

admin.site.register(Product, ProductAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Size)

