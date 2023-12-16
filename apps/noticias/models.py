from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre

# Esta herencia es la que va a ocupar el ORM
class Noticia(models.Model):
    publicado = models.DateTimeField('creado', auto_now_add=True)
    modificado = models.DateTimeField('modificado', auto_now= True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length= 250)
    contenido = models.TextField()
    imagen = models.ImageField(upload_to= 'noticias')

    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    # models.CASCADE cuando se borra la categoría, se borra todas las publicaciones relacionadas a esa categoría.

    def __str__(self):
        return self.titulo