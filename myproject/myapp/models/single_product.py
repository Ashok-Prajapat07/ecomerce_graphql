from django.db import models

class Single_product(models.Model):
    image1 = models.ImageField(upload_to='single_product/images')
    image2 = models.ImageField(upload_to='single_product/images')
    image3 = models.ImageField(upload_to='single_product/images')
    title = models.CharField(max_length=50)
    rating = models.CharField(max_length=50)
    totle_price = models.IntegerField()
    offer_price = models.IntegerField()
    delevery_price = models.IntegerField()
    descripstion = models.CharField(max_length=50)
