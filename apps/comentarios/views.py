from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView

from apps.noticias.models import Noticia

from .models import Comentario
from .forms import EditForm

# Create your views here.

def new_com(request, pk):
    comentario = request.POST.get('comentario', None)
    noticia = Noticia.objects.get(pk = pk)
    # Una vez que se logeo, el usuario siempre se encuentra en el request.user
    autor = request.user
    Comentario.objects.create(contenido=comentario, autor = autor, noticia = noticia)
    return HttpResponseRedirect(reverse_lazy('noticias:detail_noticia', kwargs= {'pk':pk}))

class delete_com(DeleteView):
    model = Comentario
    def get_success_url(self):
        return reverse_lazy('noticias:detail_noticia', kwargs={'pk': self.object.noticia.pk})

class edit_com(UpdateView):
    model = Comentario
    form_class = EditForm
    template_name = 'comentarios/update.html'
    def get_success_url(self): 
        return reverse_lazy('noticias:detail_noticia', kwargs= {'pk': self.object.noticia.pk})

