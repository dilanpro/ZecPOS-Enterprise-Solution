from django.contrib import messages
from django.http import Http404
from django.shortcuts import redirect
from django.urls import reverse


class Middleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        # Everyone has to be logged
        if not request.user.is_authenticated and not request.path == reverse("login"):
            return redirect(reverse("login"))

        return self.get_response(request)
