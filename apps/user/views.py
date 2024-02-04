from django.contrib import messages
from django.contrib.auth.views import LoginView as AuthLoginView
from django.shortcuts import redirect
from django.urls import reverse
from django.views import View


class LoginView(AuthLoginView):
    template_name: str = "pages/login.html"

    def form_invalid(self, form):
        messages.error(self.request, "Invalid username or password. Please try again.")
        return super().form_invalid(form)


class LogoutView(View):

    def get(self, request):
        request.session.flush()
        messages.success(request, "You have been logged out.")
        return redirect(reverse("login"))
