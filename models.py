from django.db import models

# Create your models here.
class Registration(models.Model):
    Username=models.CharField(max_length=50)
    Password=models.CharField(max_length=50)
    Email=models.EmailField(max_length=50)
    phone=models.CharField(max_length=50)


