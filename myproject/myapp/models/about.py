from  django.db import models


class About(models.Model):
    about_images = models.ImageField(upload_to='about/images/')
    about_video = models.FileField(upload_to='about/video')