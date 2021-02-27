from django.shortcuts import render
from .models import Event
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import EventsSerializer
# Create your views here.

class EventsViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all().order_by("-start_date")
    serializer_class = EventsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]