from django.db import models

# Create your models here.

class Persona(models.Model):
    nombre = models.CharField(max_length = 50)
    apellidos = models.CharField(max_length = 50)
    edad = models.IntegerField()
    edad = models.CharField(max_length = 12)
    email = models.EmailField()
    domicilio = models.TextField()    