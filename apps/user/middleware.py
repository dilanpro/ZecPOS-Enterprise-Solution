from datetime import datetime

from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse


class Middleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        # Super Admin has access to /sa only
        if request.user.is_superuser and not request.path.startswith("/sa"):
            return redirect("/sa")

        return self.get_response(request)
