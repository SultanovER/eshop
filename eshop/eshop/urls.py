from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', views.product_view),
    path('', views.main_page_view)
]
