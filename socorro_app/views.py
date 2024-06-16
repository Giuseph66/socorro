from django.shortcuts import render
from .models import *

def index(request):
    return render(request, 'socorro_app/login.html',{"validacao":0})
def cads(request):
    return render(request, 'socorro_app/cadastro.html')
def cadastrar(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        gmail = request.POST.get('email')
        senha = request.POST.get('senha')
        tell = request.POST.get('celular')
        pix = request.POST.get('pix')

        if Usuario.objects.filter(nome=nome).exists() or Usuario.objects.filter(gmail=gmail).exists():
            return render(request, 'socorro_app/cadastro.html',{"validacao":1,"sms":"Usuario já Esta cadastrado"})
        else:
            novo_usuario = Usuario(nome=nome, gmail=gmail, senha=senha,cell=tell,chave_pix=pix,saldo=0)
            novo_usuario.save()
            return render(request,'socorro_app/login.html',{"validacao":1,"sms":"Novo usuario cadastrado com sucesso!"})
        
def man(request):
    if request.method == 'POST':
        gmail = request.POST.get('email')
        senha = request.POST.get('senha')
        usuario = Usuario.objects.filter(gmail=gmail)
        print(usuario)
        if Usuario.objects.filter(gmail=gmail,senha=senha).exists():
            return render(request, 'socorro_app/inicio.html',{"usu":usuario})
        else:
            return render(request,'socorro_app/login.html',{"validacao":1,"sms":"Senha incorreta ou usuário não cadastrado!"})
