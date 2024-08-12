from django.shortcuts import render,redirect,get_object_or_404
from django.http import JsonResponse
from .models import *
from .forms import *
import crcmod
import qrcode

def index(request):
    return render(request, 'socorro_app/login.html',{"validacao":0})

def cads(request):
    return render(request, 'socorro_app/cadastro.html')
def inicio(request,id_usu):
    cursos= Cursos_class.objects.all()
    materias=Materias_class.objects.all()
    trabalhos = Trabalhos_fazer.objects.all()
    usuario = Usuario.objects.filter(id_usuario=id_usu)
    return render(request, 'socorro_app/inicio.html',{"usu":usuario,"curso":cursos,"materias":materias,'trabalhos': trabalhos})

def perfil_usu(request, id_usu):
    usu = Usuario.objects.get(id_usuario=id_usu)
    trabalhos_ids = [int(id.strip()) for id in usu.Trabalhos_aceitos.split(',') if id.strip().isdigit()]
    trabalhos = Trabalhos_fazer.objects.filter(id__in=trabalhos_ids)
    trabalhos_ = [int(id.strip()) for id in usu.Trabalhos_feitos.split(',') if id.strip().isdigit()]
    trabalho_f = Trabalhos_fazer.objects.filter(id__in=trabalhos_)
    return render(request, 'socorro_app/perfil.html',{"usu":usu,"trabalhos":trabalhos,"feitos":trabalho_f})

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
        trabalhos = Trabalhos_fazer.objects.all()
        if Usuario.objects.filter(gmail=gmail,senha=senha).exists():
            return render(request, 'socorro_app/inicio.html',{"usu":usuario,"curso":cursos,"materias":materias,'trabalhos': trabalhos})
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
    
    trabalhos = Trabalhos_fazer.objects.filter(curso_trab=curso_id)
    return render(request, 'socorro_app/inicio.html', {"usu": usuario,"curso": cursos,"materias": materias_cujo,"validacao": valida,'trabalhos': trabalhos})

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
        arquivos = request.FILES.get('arquivos')
        curso = get_object_or_404(Cursos_class, id=curso_id)
        materia = get_object_or_404(Materias_class, id=materia_id)
        trabalho = Trabalhos_fazer.objects.create(
                curso_trab=curso,
                fazer_materia=materia,
                trabalho=title,
                trabalho_cm_pronto='pendente', 
                quem_pediu_fazer=id_usu,
                quem_fez=0,
                data=data,
                valor_afazer=valor,
                pago=0
            )
        TrabalhoArquivo.objects.create(trabalho=trabalho, arquivo=arquivos)
        trabalhos = Trabalhos_fazer.objects.all()
        usuario = Usuario.objects.filter(id_usuario=id_usu)
        cursos= Cursos_class.objects.all()
        materias=Materias_class.objects.all()
        return render(request, 'socorro_app/inicio.html',{"usu":usuario,"curso":cursos,"materias":materias,'trabalhos': trabalhos})

def aceitar_trabalho(request, id_usu,trabalho):
    usu = get_object_or_404(Usuario, id_usuario=id_usu)
    trabalhuuu = get_object_or_404(Trabalhos_fazer, id=trabalho)
    if usu.Trabalhos_aceitos:
        trabalhos_aceitos_list = usu.Trabalhos_aceitos.split(',')
    else:
        trabalhos_aceitos_list = []
    if str(trabalho) not in trabalhos_aceitos_list:
        trabalhos_aceitos_list.append(str(trabalho))
        usu.Trabalhos_aceitos = ','.join(trabalhos_aceitos_list)
        usu.save()
    trabalhuuu.quem_fez=id_usu
    trabalhuuu.save()

    trabalho_ids = [int(id) for id in trabalhos_aceitos_list]
    trabalhos = Trabalhos_fazer.objects.filter(id__in=trabalho_ids)
    
    trabalhos_ = [int(id.strip()) for id in usu.Trabalhos_feitos.split(',') if id.strip().isdigit()]
    trabalho_f = Trabalhos_fazer.objects.filter(id__in=trabalhos_)
    valor=Trabalhos_fazer.objects.get(id=trabalho)
    return render(request, 'socorro_app/perfil.html',{"usu":usu,"trabalhos":trabalhos,"feitos":trabalho_f,"valor":valor.valor_afazer})

def recebe_pg(request, id_usu,trabalho):
    usu = Usuario.objects.get(id_usuario=id_usu)
    trabalhos_ids = [int(id.strip()) for id in usu.Trabalhos_aceitos.split(',') if id.strip().isdigit()]
    trabalhos = Trabalhos_fazer.objects.filter(id__in=trabalhos_ids)
    trabalhos_ = [int(id.strip()) for id in usu.Trabalhos_feitos.split(',') if id.strip().isdigit()]
    trabalho_f = Trabalhos_fazer.objects.filter(id__in=trabalhos_)
    valor=Trabalhos_fazer.objects.get(id=trabalho)
    return render(request, 'socorro_app/perfil.html',{"usu":usu,"trabalhos":trabalhos,"validacao":trabalho,"feitos":trabalho_f,"valor":valor.valor_afazer})

def coletar_arquivo_pronto(request, id_usu,trabalho):
    if request.method == 'POST':
        valor = request.POST.get('valor_novo')
        arquivos = request.FILES.get('arquivos')
        tra_fazer=Trabalhos_fazer.objects.get(id=trabalho)
        tra_fazer.pago=valor
        tra_fazer.trabalho_cm_pronto=arquivos
        tra_fazer.save()
        usuario = Usuario.objects.get(id_usuario=id_usu)
        trabalhos_a = usuario.Trabalhos_aceitos.split(',')
        trabalhos_a.remove(str(trabalho))
        usuario.Trabalhos_aceitos = ','.join(trabalhos_a)
        feitos = usuario.Trabalhos_feitos.split(',')
        feitos.append(str(trabalho)) 
        usuario.Trabalhos_feitos = ','.join(feitos)
        usuario.save()
        usuario = Usuario.objects.filter(id_usuario=id_usu)
        cursos = Cursos_class.objects.all()
        materias = Materias_class.objects.all()
        trabalhos = Trabalhos_fazer.objects.all()
        return render(request, 'socorro_app/inicio.html',{"usu":usuario,"curso":cursos,"materias":materias,'trabalhos': trabalhos})

def tela_compra(request, id_usu,trabalho):
    trabalhos=Trabalhos_fazer.objects.filter(id=trabalho)
    usuario = Usuario.objects.get(id_usuario=id_usu)
    nome="Socorro"
    chave="+5566999086599"
    valor= "{:.2f}".format(float(trabalhos[0].pago))
    cidade="SINOP_MT"
    txt="LOJA01"
    payloadFormato= "000201"
    merchantCategoria="52040000"
    transationCurrect="5303986"
    contraCode="5802BR"
    nome_tamanho=len(nome)
    chave_tamanho=len(chave)
    valor_tamanho=len(valor)
    cidade_tamanho=len(cidade)
    txt_tamanho=len(txt)
    merchantAccont_tam=f"0014BR.GOV.BCB.PIX01{chave_tamanho}{chave}"
    merchantAccont=f"26{len(merchantAccont_tam)}{merchantAccont_tam}"
    transationAmount_valor_tam=f"0{valor_tamanho}{valor}"
    if txt_tamanho<=9:
        Data_tam=f"050{txt_tamanho}{txt}"
    else:
        Data_tam=f"05{txt_tamanho}{txt}"
    if nome_tamanho<=9:
        nome_tamanho=f"0{nome_tamanho}"
    if cidade_tamanho<=9:
        cidade_tamanho=f"0{cidade_tamanho}"
    transationAmount_valor=f"54{transationAmount_valor_tam}"
    merchant_Nome=f"59{nome_tamanho}{nome}"
    city=f"60{cidade_tamanho}{cidade}"
    Data=f"62{len(Data_tam)}{Data_tam}"
    crc16="6304"
    payload=f"{payloadFormato}{merchantAccont}{merchantCategoria}{transationCurrect}{transationAmount_valor}{contraCode}{merchant_Nome}{city}{Data}{crc16}"
    crc16=crcmod.mkCrcFun(poly=0x11021,initCrc=0xFFFF,rev=False,xorOut=0x0000)
    crc16codigo=hex(crc16(str(payload).encode("utf-8")))
    crc16codigo_formatado=str(crc16codigo).replace("0x","").upper()
    payload_pronta=f"{payload}{crc16codigo_formatado}"
    qrcode_=qrcode.make(payload_pronta)
    qrcode_.save("socorro_app/static/imgs/qr_code_principal.png")
    return render(request, 'socorro_app/pag.html',{"usu":usuario,'trabalhos': trabalhos,'copia_cola':payload_pronta})