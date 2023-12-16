from django.urls import path
from . import views

app_name = 'comentarios'

urlpatterns = [
    path('new/<int:pk>', views.new_com, name='new_com'),
    path('edit/<int:pk>', views.edit_com.as_view(), name='edit_com'),
    path('delete/<int:pk>', views.delete_com.as_view(), name='delete_com')
]
