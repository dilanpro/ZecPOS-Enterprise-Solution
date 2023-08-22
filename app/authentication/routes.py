
from flask import Blueprint
from .views import authentication

auth: Blueprint = Blueprint(
    name='authentication',
    import_name=__name__,
    url_prefix="/auth"
)

auth.add_url_rule(rule='/login', view_func=authentication.login, methods=['GET', 'POST'])
auth.add_url_rule(rule='/logout', view_func=authentication.logout, methods=['GET'])
