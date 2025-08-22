from rest_framework import serializers
from .models import AppUser, ToDo

class AppUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUser
        fields = ["id", "name", "email"]

class ToDoSerializer(serializers.ModelSerializer):

    assignee_detail = AppUserSerializer(source="assignee", read_only=True)

    class Meta:
        model = ToDo
        fields = [
            "id",
            "task",
            "description",
            "status",
            "due_date",
            "assignee",         # write with user id
            "assignee_detail",  # read-only nested info
            "created_at",
            "updated_at",
        ]
