from django.urls import path

from crud.tarefas import views

app_name = 'tarefas'

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:tarefa_id>', views.alterar, name='alterar'),
    path('apagar/<int:tarefa_id>', views.apagar, name='apagar'),
]
