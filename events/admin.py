from django.contrib import admin
from .models import Event, EventRegistration


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Event model.

    Displays a list view with title, date, location, and organizer.
    Provides search functionality by title and location.
    Enables filtering by event date.
    """
    list_display = ("title", "date", "location", "organizer")
    search_fields = ("title", "location")
    list_filter = ("date",)


@admin.register(EventRegistration)
class EventRegistrationAdmin(admin.ModelAdmin):
    """
    Admin configuration for the EventRegistration model.

    Displays a list view with the related event, user, and registration time.
    Enables filtering by registration date.
    """
    list_display = ("event", "user", "registered_at")
    list_filter = ("registered_at",)
