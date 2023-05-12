from django.db import models
from .orders import Order
# Create your models here.

class Track_order(models.Model):
    STATUS_CHOICES = (
        ('processing', 'Processing'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    )
    order_id = models.ForeignKey(Order,on_delete=models.CASCADE)
    stetus = models.CharField(max_length=50, choices=STATUS_CHOICES)
    stetus_date = models.DateTimeField()
