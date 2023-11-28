from django.shortcuts import render
from .models import Noticia
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy

from .forms import form_noticia
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
    template_name = 'noticias/new_noticia.html'
    form_class = form_noticia
    success_url = reverse_lazy('noticias:h_noticias')

