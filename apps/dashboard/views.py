from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View


class DashboardView(LoginRequiredMixin, View):
    template_name: str = "pages/dashboard/dashboard.html"

    def get(self, request):

        return render(
            request,
            template_name=self.template_name,
        )
