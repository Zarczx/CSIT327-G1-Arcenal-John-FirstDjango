from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    # Edit page: shows Role and Course under a "CampusConnect" section
    fieldsets = UserAdmin.fieldsets + (
        ("CampusConnect", {"fields": ("role", "course")}),
    )
    # "Add user" page: includes Role and Course
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("CampusConnect", {"fields": ("email", "first_name", "last_name", "course", "role")}),
    )
    # The list you see in /admin/ > Users
    list_display = ("username", "first_name", "last_name", "email", "course", "role", "is_staff")
    list_filter = ("role", "is_staff")
    search_fields = ("username", "email", "course")