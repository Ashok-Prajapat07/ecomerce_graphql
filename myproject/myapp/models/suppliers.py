from django.db import models

# Create your models here.

class Suppliers(models.Model):
    supplier_name = models.CharField(max_length=50)
    adderss = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    postal_code = models.IntegerField()
    phone_no = models.IntegerField()
    email = models.EmailField()
