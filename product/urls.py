from django.urls import path
from .views import (
    ProductListView,
    ProductDetailView,
    ProductDetailWithImagesView
)

urlpatterns = [
    path('products/', ProductListView.as_view(), name='product_list'),
    path('products/<slug:category_slug>/', ProductListView.as_view(), name='product_list_by_category'),
    path('product/<slug:product_slug>/', ProductDetailView.as_view(), name='product_detail'),
    path('product_with_images/<slug:product_slug>/', ProductDetailWithImagesView.as_view(), name='product_detail_with_images'),
]
