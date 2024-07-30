import pytest
from model_bakery import baker
from project.modulos.models import Modulo
from project.modulos import facade


@pytest.fixture
def modulos(db):
    return [baker.make(Modulo, titulo=s) for s in 'Antes Depois'.split()]


def test_listar_modulos_ordenados(modulos):
    assert list(sorted(modulos, key=lambda modulo: modulo.order)) == facade.listar_modulos_ordenados()
