from os import name
from typing import Dict

from flask import redirect, render_template, request, url_for


async def index():
    """
    Login View
    """
    return f"Hello There"
