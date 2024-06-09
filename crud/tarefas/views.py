from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from crud.tarefas.forms import TarefaNovaForm, TarefaForm
from crud.tarefas.models import Tarefa


# Create your views here.
def home(request):
    if request.method == 'POST':
        form = TarefaNovaForm(request.POST)
        if form.is_valid():
            # Dados válidos
            form.save()
            return HttpResponseRedirect(reverse('tarefas:home'))
        else:
            tarefas_pendentes = Tarefa.objects.filter(feita=False)
            # Quando dados inválidos, mostrar os erros no HTML page {{ form.name.erros }} e mostrar as tarefas pendents
            return render(request, 'tarefas/home.html', {'form': form, 'tarefas_pendentes': tarefas_pendentes},
                          status=400)
    # Para mostrar na página inicial as tarefas pendentes
    tarefas_pendentes = Tarefa.objects.filter(feita=False)
    return render(request, 'tarefas/home.html', {'tarefas_pendentes': tarefas_pendentes})


def detalhe(request, tarefa_id):
    if request.method == 'POST':
        tarefa = Tarefa.objects.get(id=tarefa_id)
        # o parametro 'instance' serve para modificar o objeto, neste caso a tarefa pelo id dela mesma
        form = TarefaForm(request.POST, instance=tarefa)
        if form.is_valid():
            form.save()
    return HttpResponseRedirect(reverse('tarefas:home'))
