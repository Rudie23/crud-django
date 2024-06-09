from django import forms

from crud.tarefas.models import Tarefa


class TarefaNovaForm(forms.ModelForm):
    class Meta:
        model = Tarefa
        fields = ['nome']


class TarefaForm(forms.ModelForm):
    class Meta:
        model = Tarefa
        fields = ('nome', 'feita')
