from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser


class BootstrapFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"


class CustomUserCreationForm(BootstrapFormMixin, UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ("username", "email", "first_name", "last_name", "course")


class ProfileForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ("first_name", "last_name", "email", "course")