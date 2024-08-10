import pytest
from django.urls import reverse
from model_bakery import baker
from project.turmas.models import Turma
from project.django_assertions import assert_contains


@pytest.fixture
def turmas(db):
    return baker.make(Turma, 2)


@pytest.fixture
def resp(client, turmas):
    return client.get(reverse('turmas:indice'))


def test_status_code(resp):
    assert resp.status_code == 200


def test_nomes_turmas(resp, turmas):
    for turma in turmas:
        assert_contains(resp, turma.nome)


def test_inicio_turmas(resp, turmas):
    for turma in turmas:
        assert_contains(resp, turma.inicio.strftime("%d/%m/%Y"))


def test_fim_turmas(resp, turmas):
    for turma in turmas:
        assert_contains(resp, turma.fim.strftime("%d/%m/%Y"))
