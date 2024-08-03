import pytest
from django.urls import reverse
from project.django_assertions import assert_contains, assert_not_contains
from model_bakery import baker


@pytest.fixture
def resp(client, db):
    return client.get(reverse('login'))


def test_login_form_page(resp):
    assert resp.status_code == 200


@pytest.fixture
def usuario(db, django_user_model):
    usuario_modelo = baker.make(django_user_model)
    senha_plana = 'senha'
    usuario_modelo.set_password(senha_plana)
    usuario_modelo.save()
    usuario_modelo.senha_plana = senha_plana
    return usuario_modelo


@pytest.fixture
def resp_post(client, usuario):
    return client.post(reverse('login'), {'username': usuario.email, 'password': usuario.senha_plana})


def test_login_redirect(resp_post):
    assert resp_post.status_code == 302
    assert resp_post.url == reverse('modulos:indice')


@pytest.fixture
def resp_home(client, db):
    return client.get(reverse('base:home'))


def test_botao_login_home(resp_home):
    assert_contains(resp_home, 'Entrar')


def test_link_login_disponivel(resp_home):
    assert_contains(resp_home, reverse('login'))


@pytest.fixture
def resp_logado(client_usuario_logado, db):
    return client_usuario_logado.get(reverse('base:home'))


def test_botao_login_indisponivel(resp_logado):
    assert_not_contains(resp_logado, 'Entrar')


def test_link_login_indisponivel(resp_logado):
    assert_not_contains(resp_logado, reverse('login'))


def test_nome_usuario_disponivel(resp_logado, usuario_logado):
    assert_contains(resp_logado, usuario_logado.first_name)


def test_link_logout(resp_logado):
    assert_contains(resp_logado, reverse('logout'))


def test_botao_logout_disponivel(resp_logado):
    assert_contains(resp_logado, 'Sair')
