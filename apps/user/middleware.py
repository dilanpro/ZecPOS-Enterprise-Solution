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
            return redirect(reverse("businesses"))

        return self.get_response(request)
