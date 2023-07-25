
from flask import Blueprint
from .views import views

base: Blueprint = Blueprint(name='base', import_name=__name__)

base.add_url_rule(rule='/', view_func=views.index, methods=['GET'])
