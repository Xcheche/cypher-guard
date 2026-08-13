from unittest.mock import patch

import pytest
from django.urls import reverse

from contacts.models import Contact
from conftest import client


pytestmark = pytest.mark.django_db


@pytest.mark.django_db
@patch("contacts.views.send_contact_email")
def test_authenticated_user_can_create_contact(
    mock_send_contact_email,
    client: client,
    user_instance,
    contact_create,
):
    client.force_login(user_instance)

    contact_url = reverse("contact")
    response = client.post(contact_url, data=contact_create)

    assert response.status_code == 302
    assert response.url == reverse("home")
    mock_send_contact_email.assert_called_once()

    contact = Contact.objects.get(email=contact_create["email"])
    assert contact.name == contact_create["name"]
    assert contact.message == contact_create["message"]
    assert contact.phone == contact_create["phone"]
    assert contact.purpose == contact_create["purpose"]


# Test for unauthenticated user
@pytest.mark.django_db
@patch("contacts.views.send_contact_email")
def test_unauthenticated_user_can_create_contact(
    mock_send_contact_email,
    client: client,
    contact_create,
):
    contact_url = reverse("contact")
    response = client.post(contact_url, data=contact_create)

    assert response.status_code == 302
    assert response.url == reverse("home")
    mock_send_contact_email.assert_called_once()

    contact = Contact.objects.get(email=contact_create["email"])
    assert contact.name == contact_create["name"]
    assert contact.message == contact_create["message"]
    assert contact.phone == contact_create["phone"]
    assert contact.purpose == contact_create["purpose"]


# To run: python -m pytest contacts/test/test_contact_view.py -v    