from dataclasses import field
from django import forms
from .models import Mercadoria, Entrada, Saida, Local

class DateInput(forms.DateInput):
    input_type = 'date'

class LocalForm(forms.ModelForm):
    class Meta:
        model = Local
        fields = ['nome']


class MercadoriaForm(forms.ModelForm):
    class Meta:
        model = Mercadoria
        fields = ['registro','nome', 'fabricante', 'tipo', 'descricao']


class EntradaForm(forms.ModelForm):
    class Meta:
        model = Entrada
        widgets = {'data': DateInput()}
        fields = ['quantidade', 'data', 'local', 'mercadoria']


class SaidaForm(forms.ModelForm):
    class Meta:
        model = Saida
        widgets = {'data': DateInput()}
        fields = ['quantidade', 'data', 'local', 'mercadoria']
