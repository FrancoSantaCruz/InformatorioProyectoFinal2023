from django.contrib import admin
from .models import Noticia, Categoria
# Register your models here.

admin.site.register(Categoria)
admin.site.register(Noticia)
