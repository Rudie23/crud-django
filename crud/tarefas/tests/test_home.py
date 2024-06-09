import pytest
from django.test import Client
from django.urls import reverse
from crud.django_assertions import assert_cointains
from crud.tarefas.models import Tarefa


@pytest.fixture
def response_home(client: Client, db):
    return client.get(reverse('tarefas:home'), db)


def test_title(response_home):
    assert_cointains(response_home, '<title>Página Inicial</title>')


def test_form_present(response_home):
    assert_cointains(response_home, '<form')


@pytest.fixture
def response_redirect_home(client: Client, db):
    # Ao invés do client.get, use o client.post porque o método utilizado para criar dados e envia-los
    return client.post(reverse('tarefas:home'), data={'nome': 'Tarefa'})


def test_tarefa_existe_in_db(response_redirect_home):
    assert Tarefa.objects.exists()


def test_redirecionar_apos_salvar_no_db(response_redirect_home):
    assert response_redirect_home.status_code == 302


@pytest.fixture
def dado_invalido(client: Client, db):
    return client.post(reverse('tarefas:home'), data={'name': ''})


def test_tarefa_nao_existe(dado_invalido):
    assert not Tarefa.objects.exists()


def test_pagina_com_dados_invalidos(dado_invalido):
    assert dado_invalido.status_code == 400


@pytest.fixture
def lista_de_tarefas_pendentes(db):
    tarefas = [
        Tarefa(nome='Primeira tarefa', feita=False),
        Tarefa(nome='Segunda tarefa', feita=False),
    ]
    # Para criar um banco de dados
    Tarefa.objects.bulk_create(tarefas)
    return tarefas


@pytest.fixture
def response_com_lista_de_tarefas(client: Client, lista_de_tarefas_pendentes):
    return client.get(reverse('tarefas:home'))


def test_lista_de_tarefas_presentes(response_com_lista_de_tarefas, lista_de_tarefas_pendentes):
    for tarefa in lista_de_tarefas_pendentes:
        assert_cointains(response_com_lista_de_tarefas, tarefa.nome)
