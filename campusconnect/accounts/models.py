from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    class Role(models.TextChoices):
        STUDENT = "STUDENT", "Student"
        ADMIN = "ADMIN", "Admin"

    course = models.CharField(max_length=100, blank=True)
    role = models.CharField(max_length=10, choices=Role.choices, default=Role.STUDENT)