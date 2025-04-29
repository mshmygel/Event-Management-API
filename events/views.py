from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Event, EventRegistration
from .serializers import EventSerializer
from django.core.mail import send_mail
from django.conf import settings


class EventViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing event instances.
    """
    queryset = Event.objects.select_related("organizer").all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["date", "location"]

    def perform_create(self, serializer):
        """
        Set the organizer field to the current user on creation.
        """
        serializer.save(organizer=self.request.user)

    @action(detail=True, methods=["post"], permission_classes=[permissions.IsAuthenticated])
    def register(self, request, pk=None):
        """
        Register the authenticated user for the specified event
        and send confirmation email.
        """
        event = self.get_object()
        user = request.user

        if EventRegistration.objects.filter(user=user, event=event).exists():
            return Response({"detail": "You are already registered for this event."},
                            status=status.HTTP_400_BAD_REQUEST)

        EventRegistration.objects.create(user=user, event=event)

        if user.email:
            send_mail(
                subject="Registration Confirmation",
                message=f"You have successfully registered for the event {event.title}.",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[user.email],
                fail_silently=False,
            )

        return Response({"detail": "Successfully registered for the event."},
                        status=status.HTTP_201_CREATED)