from django import forms
from .models import Noticia

class form_noticia(forms.ModelForm):
     class Meta:
        model = Noticia
        fields = ['titulo', 'contenido', 'categoria', 'imagen']
          
          