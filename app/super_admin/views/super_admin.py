from flask import render_template


async def index():
	"""
	Sample View
	"""
	return render_template('pages/super_admin/base.html')