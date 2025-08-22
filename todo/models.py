from django.db import models

class AppUser(models.Model):
    """
    Simple user table with id, name, email.
    We name the DB table exactly 'users' to match your requirement.
    """
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    class Meta:
        db_table = "users"  # ✅ your requirement: table name is exactly 'users'

    def __str__(self):
        return f"{self.name} <{self.email}>"

class ToDo(models.Model):
    class Status(models.TextChoices):
        PENDING = "PENDING", "Pending"
        IN_PROGRESS = "IN_PROGRESS", "In Progress"
        DONE = "DONE", "Done"

    task = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING,
    )
    due_date = models.DateField(null=True, blank=True)

    # ✅ T-2: Add user in To Do as a foreign key (assignee)
    assignee = models.ForeignKey(
        AppUser,
        on_delete=models.CASCADE,
        related_name="todos"
    )

    created_at = models.DateTimeField(auto_now_add=True)  # auto timestamps
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.task} (assignee={self.assignee_id})"
