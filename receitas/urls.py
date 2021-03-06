from unicodedata import name
from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('receita/<int:receita_id>', receita, name='receita'),
    path('buscar', buscar, name='buscar'),
    path('cria/receita', cria_receita, name='cria_receita'),
    path('deleta/<int:receita_id>', deleta_receita, name='deleta_receita'),
    path('edita/<int:edita_id>', edita_receita, name='edita_receita'),    
    path('atualiza_receita', atualiza_receita, name='atualiza_receita')
]