from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from .forms import CustomUserCreationForm, ProfileForm
from .models import CustomUser


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Account created! Please log in.")
        return response


class ProfileView(LoginRequiredMixin, UpdateView):
    form_class = ProfileForm
    template_name = "accounts/profile.html"
    success_url = reverse_lazy("profile")

    def get_object(self):
        return self.request.user

    def form_valid(self, form):
        messages.success(self.request, "Profile updated.")
        return super().form_valid(form)