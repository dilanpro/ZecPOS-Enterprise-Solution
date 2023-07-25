
import logging
from typing import Dict
# noinspection PyPackageRequirements
from werkzeug.exceptions import BadRequestKeyError, Unauthorized, Forbidden, NotFound, MethodNotAllowed, \
	InternalServerError


def bad_request_key_error_400(e: BadRequestKeyError) -> (Dict[str, str], int):
	"""
	Bad Request
	:param e: Exception
	:return: Error Response
	"""
	logging.error(e)
	custom_error_description: str = e.description
	if "\n" in custom_error_description:
		missing_parameter: str = custom_error_description.split('\n')[1].replace('KeyError: ', '')
		custom_error_description = f"{missing_parameter} query parameter not found"
	else:
		custom_error_description = "Bad request without required query parameters"
	return {
			"error": f"{e.code} {e.name}".upper(),
			"message": custom_error_description
		}, e.code


def unauthorized_401(e: Unauthorized) -> (Dict[str, str], int):
	"""
	Unauthorized
	:param e: Exception
	:return: Error Response
	"""
	logging.error(e)
	custom_error_description: str = "You are authorized to access the URL requested"
	return {
			"error": f"{e.code} {e.name}".upper(),
			"message": custom_error_description
		}, e.code


def forbidden_403(e: Forbidden) -> (Dict[str, str], int):
	"""
	Forbidden
	:param e: Exception
	:return: Error Response
	"""
	logging.error(e)
	custom_error_description: str = "You don't have the permission to access the requested resource"
	return {
			"error": f"{e.code} {e.name}".upper(),
			"message": custom_error_description
		}, e.code


def page_not_found_404(e: NotFound) -> (Dict[str, str], int):
	"""
	Page Not Found
	:param e: Exception
	:return: Error Response
	"""
	logging.error(e)
	custom_error_description: str = "The requested resource was not found"
	return {
			"error": f"{e.code} {e.name}".upper(),
			"message": custom_error_description
		}, e.code


def method_not_allowed_405(e: MethodNotAllowed) -> (Dict[str, str], int):
	"""
	Method Not Allowed
	:param e: Exception
	:return: Error Response
	"""
	logging.error(e)
	custom_error_description: str = "The HTTP method is not allowed"
	return {
			"error": f"{e.code} {e.name}".upper(),
			"message": custom_error_description
		}, e.code


def internal_server_error_500(e: InternalServerError) -> (Dict[str, str], int):
	"""
	Internal Server Error
	:param e: Exception
	:return: Error Response
	"""
	logging.error(e)
	custom_error_description: str = "Internal server error occurred"
	return {
			"error": f"{e.code} {e.name}".upper(),
			"message": custom_error_description
		}, e.code


# TODO: Change as the Requirements
def all_other_exception_200(e: Exception) -> (Dict[str, int | Dict], int):
	"""
	Unhandled Exceptions
	:param e: Exception
	:return: Error Response
	"""
	logging.error(e)
	return {
			"score": -4,
			"details": {}
		}, 200
