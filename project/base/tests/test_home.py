from django.urls import reverse
import pytest

from project.django_assertions import assert_contains


@pytest.fixture
def resp(client, db):
    resp = client.get(reverse('base:home'))
    return resp


def test_status_code(resp):
    assert resp.status_code == 200


def test_title(resp):
    assert_contains(resp, '<title>Site de aulas - Comece agora mesmo!</title>')


def test_bloco_comece_agora(resp):
    assert_contains(resp, '<h2>Comece agora mesmo!</h2>')


def test_bloco_nossa_historia(resp):
    assert_contains(resp, '<h2>Conheça nossa história</h2>')


def test_email_link(resp):
    assert_contains(resp, 'href="mailto:email@email.com"')
