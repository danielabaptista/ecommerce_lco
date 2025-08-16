from django.urls import path
from .views import ProductListView, ProductDetailView, ProductsByCategoryView

urlpatterns = [
    path('products/', ProductListView.as_view(), name='product-list'),
    path('categories/<int:category_id>/products/', ProductsByCategoryView.as_view(), name='products-by-category'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'), 
]