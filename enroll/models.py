from django.db import models

# Create your models here.

class User(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=70)
    email = models.EmailField(max_length=100)
    course = models.CharField(max_length=125)
    password = models.CharField(max_length=100)
 