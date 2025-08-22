from django.contrib import admin
from .models import AppUser, ToDo

@admin.register(AppUser)
class AppUserAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email")
    search_fields = ("name", "email")

@admin.register(ToDo)
class ToDoAdmin(admin.ModelAdmin):
    list_display = ("id", "task", "status", "assignee", "due_date", "created_at")
    list_filter = ("status",)
    search_fields = ("task", "description", "assignee__name", "assignee__email")
