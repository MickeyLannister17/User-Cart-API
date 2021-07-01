
from rest_framework import generics
from django.contrib.auth.models import User
from .models import Category, Product, Cart
from.serializers import CategorySerializer, ProductSerializer, CartUserSerializer, CartSerializer


# Create your views here.

class ListCategory(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class DetailCategory(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ListProduct(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class DetailProduct(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ListUser(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = CartUserSerializer


class DetailUser(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = CartUserSerializer


class ListCart(generics.ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class DetailCart(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
