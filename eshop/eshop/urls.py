from django.contrib import admin
from django.urls import path
from main import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', views.main_page_view, name='product_list'),
    path('', views.main_page_view),
    path('products/<int:id>/', views.product_detail_view, name='product_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
