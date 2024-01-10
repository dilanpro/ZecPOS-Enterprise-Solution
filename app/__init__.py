import logging
from typing import NoReturn

from flask import Flask, Response, redirect, render_template, request, url_for

from .dashboard.routes import dash


def create_app() -> Flask:
    """
    Create and return the Flask App
    :return: Flask App
    """
    app: Flask = Flask(__name__)

    # Registering Blueprints
    app.register_blueprint(dash)

    # Registering Page Not Found Handler
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template("pages/404.html"), 404

    # Registering Interceptors
    @app.before_request
    def pre_interceptor() -> None:
        """
        Pre-Interceptor for logging the request url
        """
        logging.info(f"{request.method}: {request.url}")

    @app.after_request
    def post_interceptor(response) -> Response:
        """
        Post Interceptor
        :param response: Response object form the chain
        :return: Response object should send
        """
        return response

    @app.teardown_request  # type: ignore
    def teardown(exc: Exception) -> None:
        """
        Teardown function
        :param exc: Exception occurred
        """
        pass

    return app
