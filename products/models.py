from django.db import models
from django.urls import reverse
from users import models as user_models

# 상품 카테고리 - one-to-many
class Category(models.Model): # 상품 카테고리
    name = models.CharField(max_length=100)

    class Meta:
        db_table = "categories"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product:list', args=[self.name])  # product/list/laptop

# 상품
class Product(models.Model): # 복수형을 쓰면 안됨. admin page 저절로 복수형으로 표기해줌.
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True) # 상품 카테고리
    name = models.CharField(max_length=100) # 상품 이름
    image = models.ImageField(upload_to='product/%Y/%m/%d', blank=True) # 상품 이미지, pip isntall Pillow
    description = models.TextField(blank=True) # 상품 설명

    price = models.DecimalField(max_digits=10, decimal_places=2, ) # 상품 가격. 소숫점 두자리까지
    stack = models.IntegerField() # 상품 재고량

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'products'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product:product_detail', args=[self.id, self.name]) # 주문상세페이지로 넘어갈 때 정보를 넘겨주기 위해서

# 주문 상태 - one-to-many
class OrderStatus(models.Model):
    status_name = models.CharField(max_length=100) # 주문완료, 결제완료, 취소, 배송출발, 배송완료

    class Meta:
        db_table = 'order_status'

    def __str__(self):
        return self.status_name

# 주문 상품 갯수
class ProductOrder(models.Model):
    product = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True, blank=True) # 'Product'
    product_count = models.IntegerField()

    class Meta:
        db_table = 'product_orders'

    def __str__(self):
        return self.product

# 유저의 주문
class UserOrder(models.Model):
    user = models.ForeignKey(user_models.User, on_delete=models.SET_NULL, null=True)
    product_order = models.ForeignKey('ProductOrder', on_delete=models.SET_NULL, null=True)
    order_status = models.ForeignKey('OrderStatus', on_delete=models.SET_NULL, null=True)

    delivery_address = models.CharField(max_length=1000) # 주소 API 사용해야 하는데 일단 이렇게 작성.
    order_time = models.DateTimeField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=10, decimal_places=2)

    final_price = models.DecimalField(max_digits=10, decimal_places=2)

    active = models.BooleanField()

    class Meta:
        db_table = 'user_order'

    def __str__(self):
        return self.user