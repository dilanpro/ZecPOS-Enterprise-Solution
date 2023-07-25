
CONFIG = {
	# Debug Mode
	'DEBUG': False,  # Do Not Change
	
	# Request / Response
	'TRAP_BAD_REQUEST_ERRORS': True,
}


def _configure_app(app):
	for config, config_value in CONFIG.items():
		app.config[config] = config_value
	return app
