from django.db import models

# Create your models here.

class Main_cat(models.Model):
    main_cat_name = models.CharField(max_length=50)
