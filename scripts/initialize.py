import os
from typing import List

from django.contrib.auth import get_user_model


def run():
    print("Initializing Application")

    # Superuser
    User = get_user_model()
    if not User.objects.filter(is_superuser=True).exists():
        username = os.environ["DJANGO_SUPERUSER_USERNAME"]
        email = os.environ["DJANGO_SUPERUSER_EMAIL"]
        password = os.environ["DJANGO_SUPERUSER_PASSWORD"]
        User.objects.create_superuser(username=username, email=email, password=password)  # type: ignore
        print(" - Superuser Created.")
    else:
        print(" - Superuser Already Exists.")


