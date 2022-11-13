from django.db import models

# Create your models here.

# Se definen modelos BD
class BajistasDB(models.Model):

    nombre =  models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.IntegerField()
    email = models.EmailField()


class BateristasDB(models.Model):

    nombre =  models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.IntegerField()
    email = models.EmailField()

class GuitarristasDB(models.Model):

    nombre =  models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.IntegerField()
    email = models.EmailField()