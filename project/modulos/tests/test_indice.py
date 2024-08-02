from django.urls import reverse
import pytest
from project.django_assertions import assert_contains
from model_bakery import baker
from project.modulos.models import Modulo, Aula
from typing import List


@pytest.fixture
def modulos(db):
    return baker.make(Modulo, 2)


@pytest.fixture
def aulas(modulos):
    aulas = []
    for modulo in modulos:
        aulas.extend(baker.make(Aula, 3, modulo=modulo))
    return aulas


@pytest.fixture
def resp(client, modulos, aulas):
    resp = client.get(reverse('modulos:indice'))
    return resp


def test_status_code(resp):
    assert resp.status_code == 200


def test_titulos_modulos(resp, modulos: List[Modulo]):
    for modulo in modulos:
        assert_contains(resp, f'<h3>{modulo.titulo}</h3>')


def test_publicos_modulos(resp, modulos: List[Modulo]):
    for modulo in modulos:
        assert_contains(resp, modulo.publico)


def test_descricao_modulos(resp, modulos: List[Modulo]):
    for modulo in modulos:
        assert_contains(resp, modulo.descricao)


def test_titulos_aulas(resp, aulas: List[Aula]):
    for aula in aulas:
        assert_contains(resp, aula.titulo)


def test_links_aulas(resp, aulas: List[Aula]):
    for aula in aulas:
        assert_contains(resp, aula.get_absolute_url())
