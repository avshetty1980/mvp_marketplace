from django.shortcuts import render

from .models import Product, Seller
from .serializers import ProductSerializer
# from rest_framework.decorators import api_view
# from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status
# from rest_framework.views import APIView
# from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import BasePermission, SAFE_METHODS, IsAuthenticated, DjangoModelPermissionsOrAnonReadOnly
# from rest_framework import mixins
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from django.shortcuts import get_object_or_404

# class ProductList(viewsets.ViewSet):

#     def list(self, request):
#         products = Product.objects.all()
#         serializer = ProductSerializer(products, many=True)
#         return Response(serializer.data)

#     def create(self, request):
#         serializer = ProductSerializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def retrieve(self, request, pk=None):
#         queryset = Product.objects.all()
#         product = get_object_or_404(queryset, pk=pk)
#         serializer = ProductSerializer(product)
#         return Response(serializer.data)

#     def update(self, request, pk=None):
#         product = Product.objects.get(pk=pk)
#         serializer = ProductSerializer(product, data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def destroy(self, request, pk=None):
#         product = Product.objects.get(pk=pk)
#         product.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


class ProductList(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
