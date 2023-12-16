from django.db import models
from django.contrib.auth.models import User
from apps.noticias.models import Noticia

# Create your models here.
class Comentario(models.Model):
    publicado = models.DateTimeField('creado', auto_now_add=True)
    modificado = models.DateTimeField('modificado', auto_now= True)
    contenido = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    noticia = models.ForeignKey(Noticia, on_delete=models.CASCADE)

    def __str__(self):
        return self.contenido
