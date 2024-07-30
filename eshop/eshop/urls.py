from django.contrib import admin
from django.urls import path
from main import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', views.ProductListView.as_view(), name='product_list'),
    path('', views.ProductListView.as_view()),
    path('add_product/', views.create_product_view),
    path('products/<int:id>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('registration/', views.registration_view),
    path('authorization/', views.AuthorizationView.as_view()),
    path('logout/', views.logout_view),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
