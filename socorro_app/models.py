from django.db import models

class Usuario(models.Model):    
    id_usuario = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    cell = models.IntegerField()
    saldo = models.IntegerField()
    chave_pix = models.CharField(max_length=200)
    gmail = models.EmailField(max_length=500)
    senha = models.CharField(max_length=100)
    Trabalhos_aceitos = models.CharField(max_length=100)
    Trabalhos_feitos = models.CharField(max_length=100)

class Cursos_class(models.Model):
    cursos = models.CharField(max_length=200)

    def __str__(self):
        return self.cursos

class Materias_class(models.Model):
    pai = models.ForeignKey(Cursos_class, on_delete=models.CASCADE)
    materias = models.CharField(max_length=200)

    def __str__(self):
        return self.materias

class Trabalhos_fazer(models.Model):
    curso_trab = models.ForeignKey(Cursos_class, on_delete=models.CASCADE)
    fazer_materia = models.ForeignKey(Materias_class, on_delete=models.CASCADE)
    trabalho = models.CharField(max_length=200)
    trabalho_cm_pronto = models.FileField(upload_to='pronto/')
    quem_pediu_fazer = models.CharField(max_length=200)
    quem_fez = models.FloatField()
    quem_pago=models.CharField(max_length=1000)
    data = models.CharField(max_length=100)
    valor_afazer = models.FloatField()
    pago = models.FloatField()

class TrabalhoArquivo(models.Model):
    trabalho = models.ForeignKey(Trabalhos_fazer, related_name='arquivos', on_delete=models.CASCADE)
    arquivo = models.FileField(upload_to='uploads/')

class Transacao(models.Model):
    qual_trabalho = models.ForeignKey(Trabalhos_fazer, on_delete=models.CASCADE)
    quem_compro = models.CharField(max_length=200)
    quem_vendeu = models.CharField(max_length=200)
    valor_pago = models.FloatField()
