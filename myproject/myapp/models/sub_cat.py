from django.db import models
from .main_cat import Main_cat

class Sub_cat(models.Model):
    main_cat_id = models.ForeignKey(Main_cat,on_delete=models.CASCADE)
    sub_cat_name = models.CharField(max_length=50)
