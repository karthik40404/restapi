from django.db import models

# Create your models here.
class pro_user(models.Model):
    name=models.TextField()
    age=models.IntegerField()
    email=models.EmailField()
    place=models.TextField()