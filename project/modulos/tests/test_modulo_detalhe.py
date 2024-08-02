from django.urls import reverse
import pytest
from model_bakery import baker
from project.modulos.models import Modulo, Aula
from project.django_assertions import assert_contains


@pytest.fixture
def modulo(db):
    return baker.make(Modulo)


@pytest.fixture
def aulas(modulo):
    return baker.make(Aula, 3, modulo=modulo)


@pytest.fixture
def resp(client, modulo, aulas):
    resp = client.get(reverse('modulos:detalhe', kwargs={'slug': modulo.slug}))
    return resp


def test_status_code(resp):
    assert resp.status_code == 200


def test_titulo(resp, modulo):
    assert_contains(resp, f'<h3>{modulo.titulo}</h3>')


def test_publico(resp, modulo):
    assert_contains(resp, modulo.publico)


def test_descricao(resp, modulo):
    assert_contains(resp, modulo.descricao)


def test_aulas_titulo(resp, aulas):
    for aula in aulas:
        assert_contains(resp, aula.titulo)


def test_aulas_link(resp, aulas):
    for aula in aulas:
        assert_contains(resp, aula.get_absolute_url())
