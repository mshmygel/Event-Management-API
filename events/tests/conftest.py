import pytest
from django.contrib.auth.models import User
from events.models import Event
from datetime import timedelta
from django.utils import timezone


@pytest.fixture
def user(db):
    return User.objects.create_user(
        username="testuser", password="testpass", email="test@example.com"
    )


@pytest.fixture
def event(user):
    return Event.objects.create(
        title="Sample Event",
        description="Description",
        date=timezone.now() + timedelta(days=1),
        location="Kyiv",
        organizer=user,
    )
