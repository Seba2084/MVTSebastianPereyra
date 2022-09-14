from django.db import models

# Create your models here.

class datos(models.Model):
    nombre=models.CharField(max_length=40)
    relacion=models.CharField(max_length=20)
    edad=models.CharField(max_length=3)
    fechaNacimiento=models.DateField()
    email=models.EmailField()

