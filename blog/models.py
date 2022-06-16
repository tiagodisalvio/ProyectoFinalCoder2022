from sqlite3 import Timestamp
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from ckeditor.fields import RichTextField


# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    usuario= models.CharField(max_length=10)

    def __str__(self):
        return f'{self.usuario} {self.email}'

class Post(models.Model):
    titulo=models.CharField(max_length=120)
    subtitulo=models.CharField(max_length=120, default=None)
    contenido=RichTextField(blank=True, null=True)
    fecha=models.DateTimeField(default=timezone.now)
    actualizado=models.DateTimeField(auto_now=True)
    autor=models.CharField(max_length=50, default=None)
    imagen= models.ImageField(upload_to='imagen',blank=True, null=True)

    # autor=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

class Recomendaciones(models.Model):
    asunto = models.CharField(max_length=20)
    email = models.EmailField()
    contenido=RichTextField(blank=True, null=True)

    def __str__(self) -> str:
        return self.asunto 