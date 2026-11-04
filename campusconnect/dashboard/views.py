from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.views.generic import TemplateView

from accounts.models import CustomUser


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "dashboard/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["member_count"] = CustomUser.objects.count()
        context["is_admin"] = self.request.user.role == CustomUser.Role.ADMIN
        return context


class AdminPanelView(LoginRequiredMixin, TemplateView):
    template_name = "dashboard/admin_panel.html"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user.role != CustomUser.Role.ADMIN:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)