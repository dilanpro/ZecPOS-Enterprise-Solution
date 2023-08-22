
from flask import Blueprint
from .views import super_admin

sa: Blueprint = Blueprint(
    name='super_admin',
    import_name=__name__,
    url_prefix="/sa"
)

sa.add_url_rule(rule='/', view_func=super_admin.index, methods=['GET'])
