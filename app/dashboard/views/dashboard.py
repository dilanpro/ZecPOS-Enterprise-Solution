from os import name
from flask import render_template, request, redirect, url_for
from typing import Dict
import flask_login


@flask_login.login_required
async def index():
	"""
	Login View
	"""
	return f"Hello {flask_login.current_user.name}"


# TODO: Remove this Endpoint
async def create_all_db_stuffs():
	"""
	Login View
	"""
	from app.extensions.sql import db
	from app.models import User

	# Drop and then Create All Tables
	db.drop_all()
	db.create_all()

	# Create Admin User
	user = User(
		username="admin",
		name="Admin",
		access_super_admin=True
	)
	user.set_password("admin")
	db.session.add(user)
	db.session.commit()

	# Create Test User
	user = User(
		username="test",
		name="Test"
	)
	user.set_password("test")
	db.session.add(user)
	db.session.commit()

	return "Created All DB Stuffs"
