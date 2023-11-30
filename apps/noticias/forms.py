from django import forms
from .models import Noticia

class create_form(forms.ModelForm):
     class Meta:
        model = Noticia
        fields = ['titulo', 'contenido', 'categoria', 'imagen']


class update_form(forms.ModelForm):
     class Meta:
        model = Noticia
        fields = ['titulo', 'contenido', 'imagen']
          
          