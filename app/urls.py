from django.urls import path
from .views import ProductList,ProductDetail
from django.contrib.auth import views as auth_views

urlpatterns = [
     path('products/',ProductList.as_view(),name='product-list'),
    path('products/<int:pk>/',ProductDetail.as_view(),name='product-detail')
]
