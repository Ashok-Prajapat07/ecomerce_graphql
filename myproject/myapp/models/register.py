from django.db import models

# Create your models here.


class Register(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.CharField(max_length=50)
    Password = models.CharField(max_length=50)
    Confirm_password = models.CharField(max_length=50)

