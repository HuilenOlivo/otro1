from django.db import models



class TodoListItem(models.Model):
    nota = models.TextField()
    pendiente = models.BooleanField(default=True)
   
   
 
class Contact(models.Model):
    nombre = models.CharField(max_length=40)
    telefono = models.IntegerField()
    correo = models.EmailField()
    
class Proyecto(models.Model):
    nombre = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=500)
    