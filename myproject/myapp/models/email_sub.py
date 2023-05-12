from django.db import models

# Create your models here.

class Email_sub(models.Model):
    email = models.EmailField()
    date_subscribed = models.DateField()
