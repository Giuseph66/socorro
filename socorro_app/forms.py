from django import forms
from .models import *

class TrabalhoForm(forms.ModelForm):
    class Meta:
        model = Trabalhos_fazer
        fields = ['curso_trab', 'fazer_materia', 'trabalho', 'trabalho_cm_pronto', 'quem_pediu_fazer', 'data', 'valor_afazer', 'pago']

class TrabalhoArquivoForm(forms.ModelForm):
    class Meta:
        model = TrabalhoArquivo
        fields = ['arquivo']