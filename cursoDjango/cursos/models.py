from tabnanny import verbose
from django.forms import IntegerField
from django.utils import timezone
from django.db import models



# Create your models here.
class Cursos(models.Model):
    i = models.AutoField(primary_key=True)
    nombre = models.TextField(max_length=20,verbose_name="Nombre completo")
    #edad = models.IntegerField()
    curso = models.TextField(max_length=20,verbose_name="Nombre del curso")
    email = models.EmailField(max_length=200,verbose_name="Correo Electrónico")
    tiempo = models.BooleanField(
        default=False,verbose_name="Deseas obtener el curso intensivo")
    fecha = models.DateField(
        default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)#Fecha y tiempo
    update = models.DateField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"
        ordering = ["created"]
    
    def __str__(self):
        return self.nombre