from django.contrib import admin
from django.urls import path
from . import views

app_name='socorro_app'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name='index'),
    path('principal_157/',views.man, name='main'),
    path('cads/',views.cads, name='cads'),
    path('castrado/',views.cadastrar, name='cadas'),
]
