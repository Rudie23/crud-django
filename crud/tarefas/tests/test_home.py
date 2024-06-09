import pytest
from django.test import Client
from django.urls import reverse
from crud.django_assertions import assert_cointains
from crud.tarefas.models import Tarefa


@pytest.fixture
def response_home(client: Client, db):
    # Ao inves do client.get, use o client.post porque o método utilizado para criar dados e envia-los
    return client.post(reverse('tarefas:home'), data={'nome': 'Tarefa'})


def test_tarefa_existe_in_db(response_home):
    assert Tarefa.objects.exists()


def test_redirecionar_apos_salvar_no_db(response_home):
    assert response_home.status_code == 302


# def test_title(response_home):
#     assert_cointains(response_home, 'Salvar</button>')


@pytest.fixture
def dado_invalido(client: Client, db):
    return client.post(reverse('tarefas:home'), data={'name': ''})


def test_tarefa_nao_existe(dado_invalido):
    assert not Tarefa.objects.exists()


def test_pagina_com_dados_invalidos(dado_invalido):
    assert dado_invalido.status_code == 400
