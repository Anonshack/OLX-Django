from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Product, ProductImages, Category
from .serializers import ProductSerializer, ProductImagesSerializer, CategorySerializer
from django.db.models import Count, Q
from django.shortcuts import get_object_or_404


class ProductListView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        category_slug = self.kwargs.get('category_slug')
        search_query = self.request.query_params.get('q', None)

        queryset = Product.objects.all()

        if category_slug:
            category = get_object_or_404(Category, slug=category_slug)
            queryset = queryset.filter(category=category)

        if search_query:
            queryset = queryset.filter(
                Q(name__icontains=search_query) |
                Q(description__icontains=search_query) |
                Q(condition__icontains=search_query) |
                Q(brand__brand_name__icontains=search_query) |
                Q(category__category_name__icontains=search_query)
            )

        return queryset


class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailWithImagesView(APIView):
    def get(self, request, product_slug):
        product = get_object_or_404(Product, slug=product_slug)
        serializer = ProductSerializer(product)
        product_images = ProductImages.objects.filter(product=product)
        images_serializer = ProductImagesSerializer(product_images, many=True)

        return Response({
            'product_detail': serializer.data,
            'product_images': images_serializer.data
        })
