from django.db import models
from .sub_cat import Sub_cat
from .suppliers import Suppliers
# Create your models here.

class Product(models.Model):
    sub_cat_id = models.ForeignKey(Sub_cat, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=50)
    product_description = models.CharField(max_length=50)
    unit_price = models.IntegerField()
    units_in_stock =models.IntegerField()
    reorder_level = models.IntegerField()
    Image_url = models.CharField(max_length=50)
    suppliers_id = models.ForeignKey(Suppliers,on_delete=models.CASCADE)
