from django.db import models

class Usuario(models.Model):    
    id_usuario= models.AutoField(primary_key=True)
    nome=models.TextField(max_length=255)
    cell=models.IntegerField()
    saldo=models.IntegerField()
    chave_pix=models.CharField(max_length=200)
    gmail=models.EmailField(max_length=500)
    senha=models.CharField(max_length=100)
    Trabalhos_aceitos=models.CharField(max_length=100)
    Trabalhos_feitos=models.CharField(max_length=100)

class Materias_class(models.Model):
    materias=models.CharField(max_length=200)

class Trabalhos_fazer(models.Model):
    fazer_materia = models.ForeignKey(Materias_class, on_delete=models.CASCADE)
    quem_pediu_fazer=models.CharField(max_length=200)
    data=models.CharField(max_length=100)
    valor_afazer=models.IntegerField()
    pago=models.CharField(max_length=200)

class Transacao(models.Model):
    qual_trabalho=models.ForeignKey(Trabalhos_fazer, on_delete=models.CASCADE)
    quem_compro=models.CharField(max_length=200)
    quem_pago=models.CharField(max_length=200)
    valor_pago=models.IntegerField()
    