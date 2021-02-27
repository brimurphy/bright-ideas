from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>/', views.product_item, name='product_item'),
    path('add/', views.add_products, name='add_products'),
    path(
        'update/<int:product_id>/',
        views.update_products, name='update_products'),
    path(
        'delete/<int:product_id>/',
        views.delete_product, name='delete_product'),
]
