from django.urls import reverse
import pytest
# from project.django_assertions import assert_contains


@pytest.fixture
def resp(client, db):
    resp = client.get(reverse('modulos:detalhe', kwargs={'slug': 'introducao'}))
    return resp


def test_status_code(resp):
    assert resp.status_code == 200
