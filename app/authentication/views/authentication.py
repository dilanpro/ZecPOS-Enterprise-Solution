from flask import render_template, request, redirect, url_for
from htmx_flask import make_response
from typing import Dict
from app import models
import flask_login


async def login():
	"""
	Login View
	"""
	if request.method == 'GET':
		if flask_login.current_user.is_authenticated:
			flask_login.logout_user()
		return render_template('pages/authentication/login.html')

	username: str = request.form.get('username')
	password: str = request.form.get('password')

	user: models.User = models.User.query.filter_by(username=username).first()
	if user and user.check_password(password):
		flask_login.login_user(user)
		return redirect(url_for('dashboard.index'))
	else:
		return render_template(
			'pages/authentication/login.html',
			error='Invalid Username or Password',
			username=username,
			password=password
		)


async def logout():
	"""
	Logout View
	"""
	flask_login.logout_user()
	return redirect(url_for('authentication.login'))
