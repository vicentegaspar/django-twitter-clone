import pytest
from django.urls import reverse, resolve
from django.test import Client
from ..factories import UserFactory


@pytest.mark.django_db
def test_home_view(client):
    url = reverse("home")
    response = client.get(url)
    assert response.status_code == 200
    assert resolve("/").view_name == "home"
