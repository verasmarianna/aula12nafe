from random import choices
from secrets import choice
from django import forms
from django.forms import Textarea
from tempus_dominus.widgets import DatePicker
from datetime import datetime
from viagens.classe_viagem import tipos_de_classe
from viagens.validar import campo_temNumero, origem_destino_iguais, compara_data_ida_volta, compara_data_ida_pesquisa
from viagens.validar import *

class ViagemForms(forms.Form):
    origem = forms.CharField(label= 'Origem', max_length=100)
    destino = forms.CharField(label= 'Destino', max_length=100)
    data_ida = forms.DateField(label= 'Ida', widget=DatePicker())
    data_volta = forms.DateField(label= 'Volta', widget=DatePicker())
    data_pesquisa = forms.DateField(label='Data da pesquisa', disable=True, initial=datetime.today)
    classe_viagem = forms.CharField(label='Opçáo de voo', choices= tipos_de_classe)
    adicionais = forms.CharField(label='Informacoes adiconais', max_length=200, widget=forms.Textarea(), required= False)
    email= forms.EmailField(label='e-mail', max_length=200)
    
def clean(self):
    origem = self.cleaned_data.get('origem')
    destino = self.cleaned_data.get('destino')
    data_ida = self.cleaned_data.get('data_ida')
    data_volta = self.cleaned_data.get('data_volta')
    data_pesquisa = self.cleaned_data.get('data_pesquisa')
    listaErros = ()
    
    campo_temNumero (origem, 'origem', listaErros)
    campo_temNumero (destino, 'destino', listaErros)
    origem_destino_iguais (origem, destino, listaErros)
    compara_data_ida_volta(data_ida, data_volta, listaErros)
    compara_data_ida_pesquisa(data_ida, data_pesquisa, listaErros)
    
    if listaErros is not None:
        for erro in listaErros:
            mensagem_erro = listaErros[erro]
            self.add_error(erro, mensagem_erro)
        return self.cleaned_data