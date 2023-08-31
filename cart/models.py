import datetime
from django.db import models
from user.models import CustomUser
from product.models import Product

class Cart(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=datetime.now)

class CartItem(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)