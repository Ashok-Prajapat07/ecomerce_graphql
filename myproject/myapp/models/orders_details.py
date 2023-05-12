from django.db import models
from .products import Product
class Order_details(models.Model):
    product_id = models.ForeignKey(Product,on_delete=models.CASCADE)
    unit_price = models.IntegerField()
    quantity = models.IntegerField()
    discount = models.IntegerField()
