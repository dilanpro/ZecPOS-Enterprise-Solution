
from flask import Blueprint
from .views import sample

sample: Blueprint = Blueprint(
    name='sample',
    import_name=__name__,
    url_prefix="/sample"
)

sample.add_url_rule(rule='/', view_func=sample.index, methods=['GET'])