from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from crud.tarefas.forms import TarefaForm
from crud.tarefas.models import Tarefa


# Create your views here.
def home(request):

    if request.method == 'POST':
        form = TarefaForm(request.POST)
        if form.is_valid():
            # Dados válidos
            form.save()
            return HttpResponseRedirect(reverse('tarefas:home'))
        else:
            tarefas_pendentes = Tarefa.objects.filter(feita=False)
            # Dados inválidos, e mostrar os erros no HTML page {{ form.name.erros }}
            return render(request, 'tarefas/home.html', {'form': form, 'tarefas_pendentes': tarefas_pendentes}, status=400)
    tarefas_pendentes = Tarefa.objects.filter(feita=False)
    return render(request, 'tarefas/home.html', {'tarefas_pendentes': tarefas_pendentes})
