from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("produtos/", views.lista_produtos, name="lista_produtos"),
    path("produtos/novo/", views.criar_produto, name="criar_produto"),
    path("produtos/<int:pk>/editar/", views.editar_produto, name="editar_produto"),
    # path("produtos/<int:pk>/deletar/", views.deletar_produto, name="deletar_produto"),
]
