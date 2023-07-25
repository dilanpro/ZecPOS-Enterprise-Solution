from flask import render_template
from typing import Dict


async def index() -> Dict:
	"""
	Health View
	:return: Health Status
	"""
	return render_template('index.html')