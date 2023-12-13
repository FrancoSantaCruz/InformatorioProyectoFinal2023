from django.shortcuts import render
from .models import Noticia, Categoria
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .forms import create_form, update_form
# Create your views here.

# VISTA BASADA EN FUNCIONES
def home_noticia(request):
    ctx = {}
    
    categorias = Categoria.objects.all()
    ctx['categorias'] = categorias

    # Obtener el req.query. Si existe el filtro, me lo devuelve, si no, None
    filtro = request.GET.get('cat', None)
    orden = request.GET.get('order', None)

    if not filtro or filtro == '0':
        noticias = Noticia.objects.all()
    else:
        cat_selec = Categoria.objects.get(pk = filtro)
        noticias = Noticia.objects.filter(categoria = cat_selec)

    if orden == 'asc':
        noticias = noticias.order_by('publicado')
    elif orden == 'dsc':
        noticias = noticias.order_by('-publicado')

    ctx['noticias'] = noticias
    return render(request, 'noticias/home.html', ctx)

# VISTA BASADA EN CLASES
# ListView -> findAll
# DetailView -> findOne
# CreateView -> createOne
# DeleteView -> deleteOne
# CRUD -> Create Read Update Delete

# class home_noticias_clase(ListView):
#     model = Noticia
#     template_name = 'noticias/home.html'
#     context_object_name = 'noticias'

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