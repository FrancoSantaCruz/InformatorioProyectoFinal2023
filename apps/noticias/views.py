from django.shortcuts import render
from .models import Noticia
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .forms import create_form, update_form
# Create your views here.

# VISTA BASADA EN FUNCIONES
# def home_noticias(request):
#     # ORM
#     noticias = Noticia.objects.all()
#     # contexto
#     ctx = {}
#     ctx['noticias'] = noticias
#     return render(request, 'noticias/home.html', ctx)

# VISTA BASADA EN CLASES
# ListView -> findAll
# DetailView -> findOne
# CreateView -> createOne
# DeleteView -> deleteOne
# CRUD -> Create Read Update Delete

class home_noticias_clase(ListView):
    model = Noticia
    template_name = 'noticias/home.html'
    context_object_name = 'noticias'

class new_noticia(CreateView):
    model = Noticia
    template_name = 'noticias/create.html'
    form_class = create_form
    success_url = reverse_lazy('noticias:h_noticias')

def detail_noticia(request, pk):
    ctx = {}
    n = Noticia.objects.get(pk = pk)
    ctx['noticia'] = n
    return render(request, 'noticias/detail.html', ctx)

class update_noticia(UpdateView):
    model = Noticia
    template_name = 'noticias/update.html'
    form_class = update_form
    success_url = reverse_lazy('noticias:h_noticias')

class delete_noticia(DeleteView):
    model = Noticia
    success_url = reverse_lazy('noticias:h_noticias')