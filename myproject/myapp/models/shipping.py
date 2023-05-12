from django.db import models
from .orders import Order
# Create your models here.

class Shipping(models.Model):
    order_id = models.ForeignKey(Order,on_delete=models.CASCADE)
    shipment_date = models.DateTimeField()
    tracking_number = models.CharField(max_length=50)
    estimated_delivery_date = models.DateTimeField()
