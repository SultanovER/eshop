from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', views.product_view, name='product_list'),
    path('', views.main_page_view),
    path('products/<int:id>', views.product_detail_view, name='product_detail')
]
