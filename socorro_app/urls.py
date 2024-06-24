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
    path('<int:id_usu>n157<int:valida>/new/', views.novo_trabalho, name='novo'),
    path('<int:id_usu>/c157/<int:valida>/new/', views.novo_curso, name='novo_curso'),
    path('<int:id_usu>/m157/<int:valida>/new/', views.novo_materia, name='novo_materia'),
    path('<int:id_usu>cmi157<int:valida>/princ/', views.select_ini, name='processar_curso_ini'),
    path('<int:id_usu>cma157<int:valida>/princ/', views.select_add, name='processar_curso'),
    path('<int:id_usu>upload/', views.coletar_arquivo, name='upload_trabalho'),
]