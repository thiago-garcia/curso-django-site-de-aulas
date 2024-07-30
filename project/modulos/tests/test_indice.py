from django.urls import reverse
import pytest
from project.django_assertions import assert_contains


@pytest.fixture
def resp(client, db):
    resp = client.get(reverse('modulos:indice'))
    return resp


def test_status_code(resp):
    assert resp.status_code == 200


@pytest.mark.parametrize(
    'titulo',
    [
        'Introdução',
        'Primeiro programa',
    ]
)
def test_titulos_modulos(resp, titulo):
    assert_contains(resp, titulo)


@pytest.mark.parametrize(
    'publico',
    [
        'Iniciantes',
        'Intermediário',
    ]
)
def test_publicos_modulos(resp, publico):
    assert_contains(resp, publico)


@pytest.mark.parametrize(
    'descricao',
    [
        'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed viverra purus ipsum. Nulla facilisi.',
        'Sed viverra purus ipsum. Nulla facilisi. Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
    ]
)
def test_descricao_modulos(resp, descricao):
    assert_contains(resp, descricao)


@pytest.mark.parametrize(
    'titulo',
    [
        'Aula inicial',
        'História do computador',
        'Instalação do ambiente',
        'Escrevendo primeiro programa'
    ]
)
def test_titulos_aulas(resp, titulo):
    assert_contains(resp, titulo)


@pytest.mark.parametrize(
    'link',
    [
        '/modulos/aulas/aula-inicial',
        '/modulos/aulas/historia-do-computador',
        '/modulos/aulas/instalacao-do-ambiente',
        '/modulos/aulas/escrevendo-primeiro-programa'
    ]
)
def test_links_aulas(resp, link):
    assert_contains(resp, link)
