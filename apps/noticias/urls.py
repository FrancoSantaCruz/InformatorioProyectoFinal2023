"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

app_name = 'noticias'

urlpatterns = [
    # url para una view basada en funciones
    path('', views.home_noticia, name="h_noticias"),

    # url para una view basada en clases
    # 127.0.0.1:8000/noticias/
    # path('', views.home_noticias_clase.as_view(), name="h_noticias"),

    # 127.0.0.1:8000/noticias/new/
    path('new/', views.new_noticia.as_view(), name='new_noticia'),
    # 127.0.0.1:8000/noticias/detail/18293813
    path('detail/<int:pk>', views.detail_noticia, name='detail_noticia'),
    # 127.0.0.1:8000/noticias/update/12838123
    path('update/<int:pk>', views.update_noticia.as_view(), name='update_noticia'),
    # 127.0.0.1:8000/noticias/delete/19283812
    path('delete/<int:pk>', views.delete_noticia.as_view(), name='delete_noticia'),
]
