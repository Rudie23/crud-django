from django.contrib import admin

from crud.tarefas.models import Tarefa


# Register your models here.
@admin.register(Tarefa)
class TarefaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'feita')
    list_filter = ('feita',)
    ordering = ('-id',)
    search_fields = ('name',)
