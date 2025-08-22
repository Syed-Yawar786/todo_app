from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import AppUser, ToDo
from .serializers import AppUserSerializer, ToDoSerializer

class AppUserViewSet(viewsets.ModelViewSet):

    queryset = AppUser.objects.all().order_by("id")
    serializer_class = AppUserSerializer

class ToDoViewSet(viewsets.ModelViewSet):

    queryset = ToDo.objects.select_related("assignee").order_by("-created_at")
    serializer_class = ToDoSerializer

    filter_backends = [SearchFilter, DjangoFilterBackend]

    search_fields = ["task", "description", "assignee__name", "assignee__email"]

    filterset_fields = ["assignee"]
