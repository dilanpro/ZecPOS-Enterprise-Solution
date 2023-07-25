
import logging
from typing import NoReturn
from flask import Flask, request, Response
from .config import _configure_app
from . import errors
# noinspection PyPackageRequirements
from werkzeug.exceptions import BadRequestKeyError, Unauthorized, Forbidden, NotFound, MethodNotAllowed, \
	InternalServerError
from .base.routes import base

logging.basicConfig(level=logging.INFO)


def create_app() -> Flask:
	"""
	Create and return the Flask App
	:return: Flask App
	"""
	app: Flask = Flask(__name__)
	app = _configure_app(app)
	app.register_blueprint(base)

	# Registering Error Handlers
	# 4XX Status Codes
	app.register_error_handler(BadRequestKeyError, errors.bad_request_key_error_400)
	app.register_error_handler(Unauthorized, errors.unauthorized_401)
	app.register_error_handler(Forbidden, errors.forbidden_403)
	app.register_error_handler(NotFound, errors.page_not_found_404)
	app.register_error_handler(MethodNotAllowed, errors.method_not_allowed_405)
	# 5XX Status Codes
	app.register_error_handler(InternalServerError, errors.internal_server_error_500)
	# Fallback
	app.register_error_handler(Exception, errors.all_other_exception_200)

	@app.before_request
	def pre_interceptor() -> NoReturn:
		"""
		Pre-Interceptor for logging the request url
		"""
		logging.info(f'{request.method}: {request.url}')

	@app.after_request
	def post_interceptor(response) -> Response:
		"""
		Post Interceptor
		:param response: Response object form the chain
		:return: Response object should send
		"""
		return response

	@app.teardown_request
	def teardown(exc: Exception) -> NoReturn:
		"""
		Teardown function
		:param exc: Exception occured
		"""
		pass

	return app
