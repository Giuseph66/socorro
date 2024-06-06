from django.contrib import admin
from django.urls import path
from . import views

app_name='socorro_app'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name='index'),
    path('pergunta/',views.pergunta, name='pegun'),
]
