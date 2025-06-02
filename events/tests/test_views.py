import pytest
from rest_framework.test import APIClient
from events.models import EventRegistration
from unittest.mock import patch
from django.urls import reverse


def get_jwt_token(client, username="testuser", password="testpass"):
    """
    Helper function to obtain JWT token for the test user.
    """
    response = client.post(
        reverse("token_obtain_pair"),  # or hardcoded: "/api/token/"
        {"username": username, "password": password},
        format="json",
    )
    return response.data["access"]


@pytest.mark.django_db
def test_event_list_view():
    client = APIClient()
    response = client.get("/api/events/events/")
    assert response.status_code == 200


@pytest.mark.django_db
def test_authenticated_event_registration(user, event):
    client = APIClient()
    token = get_jwt_token(client)
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")

    response = client.post(f"/api/events/events/{event.id}/register/")
    assert response.status_code == 201
    assert EventRegistration.objects.filter(user=user, event=event).exists()


@pytest.mark.django_db
def test_duplicate_registration_not_allowed(user, event):
    EventRegistration.objects.create(user=user, event=event)

    client = APIClient()
    token = get_jwt_token(client)
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")

    response = client.post(f"/api/events/events/{event.id}/register/")
    assert response.status_code == 400
    assert response.data["detail"] == "You are already registered for this event."


@pytest.mark.django_db
@patch("events.views.send_mail")
def test_email_sent_on_registration(mock_send_mail, user, event):
    client = APIClient()
    token = get_jwt_token(client)
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")

    client.post(f"/api/events/events/{event.id}/register/")
    assert mock_send_mail.called
    assert mock_send_mail.call_args[1]["subject"] == "Registration Confirmation"
    assert user.email in mock_send_mail.call_args[1]["recipient_list"]
