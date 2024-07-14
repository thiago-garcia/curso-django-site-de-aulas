from django.test import Client
from django.urls import reverse


def test_status_code():
    client = Client()
    resp = client.get(reverse('base:home'))
    assert resp.status_code == 200
