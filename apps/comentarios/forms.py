from django import forms
from .models import Comentario

class EditForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['contenido',]