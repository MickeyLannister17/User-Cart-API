from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Category, Product, Cart



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id',
                  'title')
        model = Category


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

    def create(self, validated_data):
        return Product.objects.create(**validated_data)

class UserSerializer(serializers.ModelSerializer):
    products = serializers.PrimaryKeyRelatedField(many=True, queryset=Product.objects.all())

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
            'products',
        )


class CartUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')


class CartSerializer(serializers.ModelSerializer):
    cart_id = CartUserSerializer(read_only=True, many=False)
    products = ProductSerializer(read_only=True, many=True)

    class Meta:
        model = Cart
        fields = ('cart_id', 'created_at', 'products')
