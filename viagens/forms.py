from django import forms
from tempus_dominus.widgets import DatePicker
from datetime import datetime
from viagens.classe_viagem import tipos_de_classe

class ViagemForms(forms.Form):
    origem = forms.CharField(label= 'Origem', max_length=100)
    destino = forms.CharField(label= 'Destino', max_length=100)
    data_ida = forms.DateField(label= 'Ida', widget=DatePicker())
    data_volta = forms.DateField(label= 'Volta', widget=DatePicker())
    data_pesquisa = forms.DateField(label='Data da pesquisa', disable=True, initial=datetime.today)
    classe_viagem = forms.CharField(label='Opçáo de voo', choices= tipos_de_classe)