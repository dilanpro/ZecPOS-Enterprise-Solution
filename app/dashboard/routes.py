
from flask import Blueprint
from .views import dashboard
from flask_login import login_required

dash: Blueprint = Blueprint(
    name='dashboard',
    import_name=__name__,
    url_prefix="/"
)

dash.add_url_rule(rule='/', view_func=dashboard.index, methods=['GET', 'POST'])
dash.add_url_rule(rule='/test', view_func=dashboard.create_all_db_stuffs, methods=['GET'])
