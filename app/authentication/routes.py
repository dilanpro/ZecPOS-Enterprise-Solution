
from flask import Blueprint
from .views import authentication

base: Blueprint = Blueprint(name='authentication', import_name=__name__)

base.add_url_rule(rule='/', view_func=authentication.login, methods=['GET'])
