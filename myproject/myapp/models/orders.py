from django.db import models
from .orders_details import Order_details
from .customers import Customer
# Create your models here.

class Order(models.Model):
    customer_id = models.ForeignKey(Customer,on_delete=models.CASCADE)
    order_details_id = models.ForeignKey(Order_details,on_delete=models.CASCADE)
    order_date = models.DateField()
    required_date = models.DateField()
    shipped_date = models.CharField(max_length=50)
    stetus = models.CharField(max_length=50)
    comment = models.CharField(max_length=50)
    shipping_to = models.CharField(max_length=50)

