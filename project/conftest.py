import pytest
from model_bakery import baker


@pytest.fixture
def usuario_logado(db, django_user_model):
    return baker.make(django_user_model, first_name='Fulano')


@pytest.fixture
def client_usuario_logado(client, usuario_logado):
    client.force_login(usuario_logado)
    return client
