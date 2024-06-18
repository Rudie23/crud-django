from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from crud.tarefas.forms import TarefaNovaForm, TarefaForm
from crud.tarefas.models import Tarefa


# Create your views here.
def home(request):
    """
    Mostra as tarefas pendentes e feitas, e também cria novas tarefas.




    """
    if request.method == 'POST':
        form = TarefaNovaForm(request.POST)
        if form.is_valid():
            # Dados válidos
            form.save()
            return HttpResponseRedirect(reverse('tarefas:home'))
        else:
            tarefas_pendentes = Tarefa.objects.filter(feita=False).all()
            tarefas_feitas = Tarefa.objects.filter(feita=True).all()
            # Quando dados inválidos, mostrar os erros no HTML page {{ form.name.erros }} e mostrar as tarefas pendents
            return render(request, 'tarefas/home.html',
                          {
                              'form': form,
                              'tarefas_pendentes': tarefas_pendentes,
                              'tarefas_feitas': tarefas_feitas
                          },
                          status=400)
    # Para mostrar na página inicial as tarefas pendentes
    tarefas_pendentes = Tarefa.objects.filter(feita=False).all()
    tarefas_feitas = Tarefa.objects.filter(feita=True).all()
    return render(request, 'tarefas/home.html',
                  {
                      'tarefas_pendentes': tarefas_pendentes,
                      'tarefas_feitas': tarefas_feitas
                  })


def alterar(request, tarefa_id):
    """
    Função altera o status da tarefa para false ou true.
    """
    if request.method == 'POST':
        tarefa = Tarefa.objects.get(id=tarefa_id)
        # o parametro 'instance' serve para modificar o objeto, neste caso a tarefa pelo id dela mesma
        form = TarefaForm(request.POST, instance=tarefa)
        if form.is_valid():
            form.save()
    return HttpResponseRedirect(reverse('tarefas:home'))


def apagar(request, tarefa_id):
    """
    Deleta uma tarefa feita de acordo com seu id.
    """
    if request.method == 'POST':
        Tarefa.objects.filter(id=tarefa_id).delete()
    return HttpResponseRedirect(reverse('tarefas:home'))
