from django.contrib import admin
from .models import Usuario, Post, Recomendaciones
# Register your models here.

admin.site.register(Usuario)
admin.site.register(Post)
admin.site.register(Recomendaciones)