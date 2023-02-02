from django.contrib import admin
from . import models


admin.site.register(models.Category)
admin.site.register(models.Product)
admin.site.register(models.ProductOrder)
admin.site.register(models.UserOrder)
admin.site.register(models.OrderStatus)