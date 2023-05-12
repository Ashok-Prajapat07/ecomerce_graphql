from django.db import models

# Create your models here.

class Customer(models.Model):
    customer_name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=50)
    phone_no = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
