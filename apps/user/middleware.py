from datetime import datetime

from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse


class Middleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        # Everyone has to be logged
        if not request.user.is_authenticated and not request.path == reverse("login"):
            return redirect(reverse("login"))

        # Everyone can logged out
        if request.user.is_authenticated and request.path == reverse("logout"):
            pass

        # Super Admin has access to /sa only
        elif request.user.is_superuser and not request.path.startswith("/sa"):
            return redirect(reverse("sa-businesses"))

        # Super Admin Dashboard Access
        elif request.path.startswith("/sa") and not request.user.is_superuser:
            messages.error(request, "You don't have access")
            return redirect(request.user.get_default_dashboard_url())

        # Team Access
        elif request.path.startswith("/team") and not request.user.has_admin_access():
            messages.error(request, "You don't have access to Teams")
            return redirect(request.user.get_default_dashboard_url())

        # POS Access
        elif request.path.startswith("/pos") and not request.user.has_pos_access():
            messages.error(request, "You don't have access to POS")
            return redirect(request.user.get_default_dashboard_url())

        return self.get_response(request)
