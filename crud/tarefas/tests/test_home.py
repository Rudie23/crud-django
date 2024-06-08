import pytest
from django.test import Client
from django.urls import reverse
from crud.django_assertions import assert_cointains


@pytest.fixture
def response_home(client: Client):
    return client.get(reverse('tarefas:home'))


def test_home(response_home):
    assert response_home.status_code == 200


def test_title(response_home):
    assert_cointains(response_home, 'Salvar</button>')
