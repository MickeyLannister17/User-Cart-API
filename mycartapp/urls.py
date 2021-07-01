from django.urls import path
from . import views

urlpatterns = [

    path('categories', views.ListCategory.as_view(), name='categories'),
    path('categories/<int:pk>/', views.DetailCategory.as_view(), name='singlecategory'),
    path('product', views.ListProduct.as_view(), name='product'),
    path('product/<int:pk>/', views.DetailProduct.as_view(), name='singleproduct'),
    path('users', views.ListUser.as_view(), name='users'),
    path('users/<int:pk>/', views.DetailUser.as_view(), name='singleuser'),

    path('carts', views.ListCart.as_view(), name='allcarts'),
    path('carts/<int:pk>', views.DetailCart.as_view(), name='cartdetail')

]
