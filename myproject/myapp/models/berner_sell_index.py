from django.db import models


class Berner_sell(models.Model):
    title = models.CharField(max_length=50)
    sell_offer = models.CharField(max_length=50)
    image = models.ImageField(upload_to='berner_sel_index/images')
    active = models.BooleanField()
