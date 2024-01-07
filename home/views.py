from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from product.models import Product, Category
from product.serializers import ProductSerializer, CategorySerializer


class HomeView(APIView):
    def get(self, request):
        all_category = Category.objects.all()
        products = Product.objects.all()

        category_serializer = CategorySerializer(all_category, many=True)
        product_serializer = ProductSerializer(products, many=True)

        return Response({
            'all_category': category_serializer.data,
            'products': product_serializer.data
        })
