from django.db import models

# Create your models here.
class Quimico(models.Model):
    nombre=models.CharField(max_length=50)
    proveedor=models.CharField(max_length=50)
    prodxbulto=models.IntegerField() #cantidad de productos por bulto

    def __str__(self):
        return self.nombre



class Descartable(models.Model):
    nombre= models.CharField(max_length=50)
    proveedor=models.CharField(max_length=50)
    prodxbulto=models.IntegerField() #cantidad de productos por bulto

    def __str__(self):
        return self.nombre
        

class Cepillo(models.Model):
    nombre= models.CharField(max_length=50)
    proveedor=models.CharField(max_length=50)
    prodxbulto=models.IntegerField() #cantidad de productos por bulto

    def __str__(self):
        return self.nombre
