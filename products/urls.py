from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
    path('list', views.categorize_products, name='list'),  # http://127.0.0.1:8000/products/list
    path('list/<str:category_name>', views.categorize_products, name='list'),  # http://127.0.0.1:8000/products/list/laptop
]