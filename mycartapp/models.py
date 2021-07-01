from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=250)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title


class Product(models.Model):
    product_tag = models.CharField(max_length=150)
    name = models.CharField(max_length=150)
    brand_name = models.CharField(max_length=150)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.FloatField()
    picture = models.URLField()
    description = models.TextField()
    status = models.BooleanField(default=True)
    date_created = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return '{} {}'.format(self.product_tag, self.name)


class Cart(models.Model):
    cart_id = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    products = models.ManyToManyField(Product)

    class Meta:
        ordering = ['cart_id', '-created_at']

    def __str__(self):
        return '{}'.format(self.cart_id)
