from django.db import models

# Create your models here.

class News(models.Model):
    news_name = models.CharField(max_length=50)
    news_url = models.URLField()
