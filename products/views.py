from django.shortcuts import render
from .models import (
    Category,
    Product,
    ProductOrder,
    OrderStatus,
    UserOrder
)

# Create your views here.
def categorize_products(request, category_name=None):  # category_name이 있으면 받고 없으면 None

    if request.method == 'GET':

        categories = Category.objects.all()
        products = Product.objects.all()


        return render(request, 'list.html', {'categories':categories, 'products':products})