from django.urls import reverse
import pytest
from model_bakery import baker
from project.modulos.models import Modulo, Aula
from project.django_assertions import assert_contains


@pytest.fixture
def modulo(db):
    return baker.make(Modulo)


@pytest.fixture
def aula(modulo):
    return baker.make(Aula, modulo=modulo)


@pytest.fixture
def resp(client, modulo, aula):
    resp = client.get(reverse('modulos:aula', kwargs={'slug': aula.slug}))
    return resp


def test_status_code(resp):
    assert resp.status_code == 200


def test_titulo(resp, aula: Aula):
    assert_contains(resp, aula.titulo)


def test_descricao(resp, aula: Aula):
    assert_contains(resp, aula.descricao)


def test_embed(resp, aula: Aula):
    assert_contains(resp, aula.embed)


def test_breadcrumb(resp, modulo: Modulo):
    assert_contains(resp, f'<li class="breadcrumb-item"><a href="{modulo.get_absolute_url()}">{modulo.titulo}</a></li>')
