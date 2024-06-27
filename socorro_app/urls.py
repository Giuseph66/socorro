from django.contrib import admin
from django.urls import path
from . import views

app_name='socorro_app'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('principal_157/', views.man, name='main'),
    path('cads/', views.cads, name='cads'),
    path('castrado/', views.cadastrar, name='cadas'),
    path('<int:id_usu>inicio/', views.inicio, name='inicio'),
    path('<int:id_usu>n157<int:valida>/new/', views.novo_trabalho, name='novo'),
    path('<int:id_usu>/c157/<int:valida>/new/', views.novo_curso, name='novo_curso'),
    path('<int:id_usu>/m157/<int:valida>/new/', views.novo_materia, name='novo_materia'),
    path('<int:id_usu>cmi157<int:valida>/princ/', views.select_ini, name='processar_curso_ini'),
    path('<int:id_usu>cma157<int:valida>/princ/', views.select_add, name='processar_curso'),
    path('<int:id_usu>upload/', views.coletar_arquivo, name='upload_trabalho'),
    path('<int:id_usu>pronto/<int:trabalho>', views.coletar_arquivo_pronto, name='upload_trabalho_pronto'),
    path('<int:id_usu>/<int:trabalho>aceito/', views.aceitar_trabalho, name='aceito'),
    path('<int:id_usu>/<int:trabalho>compra/', views.tela_compra, name='tela_compra'),
    path('<int:id_usu>/<int:trabalho>entrega/', views.recebe_pg, name='entrega'),
    path('<int:id_usu>perfil/', views.perfil_usu, name='perfil'),
]