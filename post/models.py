from django.db import models

# Create your models here.

class Post (models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    edad = models.IntegerField()

