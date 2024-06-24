from django.shortcuts import render,redirect,get_object_or_404
from django.http import JsonResponse
from django.forms import modelformset_factory
from .models import *
from .forms import *

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
        cursos= Cursos_class.objects.all()
        materias=Materias_class.objects.all()
        if Usuario.objects.filter(gmail=gmail,senha=senha).exists():
            return render(request, 'socorro_app/inicio.html',{"usu":usuario,"curso":cursos,"materias":materias})
        else:
            return render(request,'socorro_app/login.html',{"validacao":1,"sms":"Senha incorreta ou usuário não cadastrado!"})
        
def novo_trabalho(request,id_usu,valida):
    usuario = Usuario.objects.get(id_usuario=id_usu)
    cursos= Cursos_class.objects.all()
    materias=Materias_class.objects.all()
    return render(request, 'socorro_app/novo_trabalho.html',{"usu":usuario,"curso":cursos,"materias":materias,"validacao":valida})

def novo_curso(request, id_usu, valida):
    usuario = Usuario.objects.get(id_usuario=id_usu)
    cursos = Cursos_class.objects.all()
    materias = Materias_class.objects.all()
    
    if request.method == 'POST':
        curso_nome = request.POST.get('curso')
        if not Cursos_class.objects.filter(cursos=curso_nome).exists():
            novo_curso = Cursos_class(cursos=curso_nome)
            novo_curso.save()
        return redirect('socorro_app:novo_curso', id_usu=id_usu, valida=9)
    
    return render(request, 'socorro_app/novo_trabalho.html', {"usu": usuario, "curso": cursos, "materias": materias, "validacao": valida})

def novo_materia(request, id_usu, valida):
    usuario = Usuario.objects.get(id_usuario=id_usu)
    cursos = Cursos_class.objects.all()
    materias = Materias_class.objects.all()
    
    if request.method == "POST":
        curso_id = request.POST.get('curso')
        materia_nome = request.POST.get('mate')
        curso = Cursos_class.objects.get(id=curso_id)
        
        if not Materias_class.objects.filter(pai=curso, materias=materia_nome).exists():
            nova_materia = Materias_class(pai=curso, materias=materia_nome)
            nova_materia.save()
        return redirect('socorro_app:novo_materia', id_usu=id_usu, valida=9)
    
    return render(request, 'socorro_app/novo_trabalho.html', {"usu": usuario, "curso": cursos, "materias": materias, "validacao": valida})


def select_ini(request, id_usu, valida):
    usuario = Usuario.objects.filter(id_usuario=id_usu)
    cursos = list(Cursos_class.objects.all())
    materias_cujo = []
    pai = None
    if request.method == 'POST':
        curso_id = request.POST.get('curso_id')
        if curso_id:
            pai = get_object_or_404(Cursos_class, id=curso_id)
            materias_cujo = Materias_class.objects.filter(pai=pai)
            cursos.remove(pai)
            cursos.insert(0, pai)
            for materia in materias_cujo:
                print(materia.materias)
    return render(request, 'socorro_app/inicio.html', {"usu": usuario,"curso": cursos,"materias": materias_cujo,"validacao": valida})

def select_add(request, id_usu, valida):
    usuario = Usuario.objects.get(id_usuario=id_usu)
    cursos = list(Cursos_class.objects.all())
    materias_cujo = []
    pai = None
    if request.method == 'POST':
        curso_id = request.POST.get('curso_id')
        if curso_id:
            pai = get_object_or_404(Cursos_class, id=curso_id)
            materias_cujo = Materias_class.objects.filter(pai=pai)
            cursos.remove(pai)
            cursos.insert(0, pai)
            for materia in materias_cujo:
                print(materia.materias)
    return render(request, 'socorro_app/novo_trabalho.html', {"usu": usuario,"curso": cursos,"materias": materias_cujo,"validacao": valida})



def coletar_arquivo(request, id_usu):
    if request.method == 'POST':
        curso_id = request.POST.get('curso_trab')
        materia_id = request.POST.get('Materia_traba')
        data = request.POST.get('data')
        title = request.POST.get('trabalho')
        valor = request.POST.get('valor_afazer')
        arquivos = request.FILES.getlist('arquivos')

        curso = get_object_or_404(Cursos_class, id=curso_id)
        materia = get_object_or_404(Materias_class, id=materia_id)

        trabalho_data = {
            'curso_trab': curso.id,
            'fazer_materia': materia.id,
            'trabalho': title,
            'trabalho_cm_pronto': 'pendente', 
            'quem_pediu_fazer': id_usu,
            'data': data,
            'valor_afazer': valor,
            'pago': '00' 
        }

        trabalho_form = TrabalhoForm(trabalho_data)

        if trabalho_form.is_valid():
            trabalho = trabalho_form.save()

            for arquivo in arquivos:
                TrabalhoArquivo.objects.create(trabalho=trabalho, arquivo=arquivo)

            return JsonResponse({'message': 'Arquivos coletados com sucesso.'}, status=200)
        else:
            return JsonResponse({'errors': trabalho_form.errors}, status=400)

    trabalho_form = TrabalhoForm()
    return render(request, 'socorro_app/tst.html', {'trabalho_form': trabalho_form})