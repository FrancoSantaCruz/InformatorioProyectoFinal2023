from django.db import models

# Create your models here.
# Esta herencia es la que va a ocupar el ORM
class Noticia(models.Model):
    titulo = models.CharField(max_length= 250)
    contenido = models.TextField()

    def __str__(self):
        return self.titulo