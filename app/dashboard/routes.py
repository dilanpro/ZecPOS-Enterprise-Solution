from flask import Blueprint

from .views import dashboard

dash: Blueprint = Blueprint(name="dashboard", import_name=__name__, url_prefix="/")

dash.add_url_rule(rule="/", view_func=dashboard.index, methods=["GET", "POST"])
