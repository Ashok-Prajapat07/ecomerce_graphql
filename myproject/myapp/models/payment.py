from django.db import models
from .customers import Customer


class Payment(models.Model):
    PAYMENT_CHOICE = (
        ('CC', 'Credit Card'),
        ('PP', 'PayPal'),
        ('BT', 'Bank Transfer'),
    )
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    payment_date = models.DateTimeField()
    payment_amount = models.IntegerField()
    payment_type = models.CharField(max_length=2, choices=PAYMENT_CHOICE)
