from flask import render_template
from typing import Dict


async def login():
	"""
	Login View
	"""
	return render_template('pages/index.html')
