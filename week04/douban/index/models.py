from django.db import models

# Create your models here.
class Movie(models.Model):
    # id 自动创建
    name = models.CharField(max_length=50)
    stars = models.IntegerField()
    comments = models.CharField(max_length=1000)
