from django.contrib.auth.views import LoginView as AuthLoginView
from django.shortcuts import render


class LoginView(AuthLoginView):
    template_name: str = "pages/login.html"

    def form_invalid(self, form):
        messages.error(self.request, "Invalid username or password. Please try again.")
        return super().form_invalid(form)