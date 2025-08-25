from django.urls import path
from django.conf.urls.static import static
from .views import ProductListView, ProductDetailView, ProductsByCategoryView


urlpatterns = [
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'), 
]

