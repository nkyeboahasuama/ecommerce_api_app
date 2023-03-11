from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview),
    path('product-list/', views.apiProducts, name="products-list"),
    path('product-list/<str:pk>/', views.ProductDetail.as_view(), name="product-detail"),
    path('category-list/', views.CategoryList.as_view(), name="category-list"),
    path('category-list/<str:pk>/', views.CategoryDetail.as_view(), name="category-detail"),
    path('order-items/', views.order_items, name="order-items"),
]


