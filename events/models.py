from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):
    """
    Model representing an event that users can organize and register for.

    Attributes:
        title (str): The title of the event.
        description (str): A brief description of the event.
        date (datetime): The date and time when the event will take place.
        location (str): The location where the event is held.
        organizer (User): The user who organizes the event.
    """

    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=255)
    organizer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="organized_events"
    )

    def __str__(self) -> str:
        return f"{self.title} - {self.date.strftime('%Y-%m-%d %H:%M')}"


class EventRegistration(models.Model):
    """
    Model representing a user's registration to a specific event.

    Attributes:
        user (User): The user who registers for the event.
        event (Event): The event the user is registering for.
        registered_at (datetime): The date and time of registration.
    """

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="registrations"
    )
    event = models.ForeignKey(
        Event, on_delete=models.CASCADE, related_name="registrations"
    )
    registered_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "event")

    def __str__(self) -> str:
        return f"{self.user.username} → {self.event.title}"
