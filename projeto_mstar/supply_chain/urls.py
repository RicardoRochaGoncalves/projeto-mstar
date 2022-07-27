from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('cadastro_local/', views.cadastro_local, name='cadastro-local'),
    path('cadastro_mercadoria/', views.cadastro_mercadoria, name='cadastro-mercadoria'),
    path('cadastro_entrada/', views.cadastro_entrada, name='cadastro-entrada'),
    path('cadastro_saida/', views.cadastro_saida, name='cadastro-saida'),
    path('delete_local/<int:id>', views.delete_local, name='delete-local'),
    path('delete_mercadoria/<int:id>', views.delete_mercadoria, name='delete-mercadoria'),
    path('delete_entrada/<int:id>', views.delete_entrada, name='delete-entrada'),
    path('delete_saida/<int:id>', views.delete_saida, name='delete-saida'),
    path('edita_local/<int:id>', views.edita_local, name='edita-local'),
    path('edita_mercadoria/<int:id>', views.edita_mercadoria, name='edita-mercadoria'),
    path('edita_entrada/<int:id>', views.edita_entrada, name='edita-entrada'),
    path('edita_saida/<int:id>', views.edita_saida, name='edita-saida'),
    path('relatorio_mercadoria/<int:id>', views.relatorio_mercadoria, name='relatorio-mercadoria'),
    path('gerarpdf/', views.gerar_pdf, name='gerar-pdf'),



]
