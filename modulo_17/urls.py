from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_produtos, name='listar_produtos'),
    path('novo/', views.cadastrar_produto, name='cadastrar_produto'),
    path('editar/<int:pk>/', views.atualizar_produto, name='atualizar_produto'),
    path('deletar/<int:pk>/', views.excluir_produto, name='excluir_produto'),
]
