
import logging
import flask_login
from . import models
from typing import NoReturn
from flask import Flask, redirect, request, Response, url_for, render_template
from htmx_flask import Htmx
from .extensions.sql import db
from .authentication.routes import auth
from .super_admin.routes import sa
from .dashboard.routes import dash


def create_app() -> Flask:
	"""
	Create and return the Flask App
	:return: Flask App
	"""
	app: Flask = Flask(__name__)

	# Set Configs
	app.secret_key = 'MySuperSecret'  # TODO: Change this to a random string
	app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/zecpos'  # TODO: Change this to a database url

	# SQL SetUp
	db.init_app(app)

	# Login Manager SetUp
	login_manager: flask_login.LoginManager = flask_login.LoginManager()
	login_manager.init_app(app)

	# Htmx SetUp
	htmx = Htmx()
	htmx.init_app(app)

	# Registering Blueprints
	app.register_blueprint(auth)
	app.register_blueprint(sa)
	app.register_blueprint(dash)

	# Registering Page Not Found Handler
	@app.errorhandler(404)
	def page_not_found(e):
		return render_template('pages/404.html'), 404

	# Registering Interceptors
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

	# Registering Login Manager Callbacks
	@login_manager.user_loader
	def user_loader(user_id):
		"""
		:param usr_id: ID of the user
		"""
		user: models.User = models.User.query.filter_by(id=user_id).first()
		return user

	@login_manager.request_loader
	def request_loader(request):
		"""
		:param request: Request object
		"""
		pass

	@login_manager.unauthorized_handler
	def unauthorized_handler():
		"""
		Redirect to login page if the user is not logged in
		"""
		return redirect(url_for('authentication.login'))

	return app
