"""Restrict access to Flask applications by requestor IP address."""

from flask import request
from werkzeug.exceptions import Forbidden


class IPFilter:
    """An IP address filter for Flask applications."""

    def __init__(self, flask_app=None, ruleset=None):
        """
        Initialize the IP filter.

        :parameter app: The Flask application may or may not exist when
                        __init__ is called. If app is passed, the filter will
                        be applied to the Flask application immediately. The
                        filter can be applied to a Flask application later by
                        calling init_app with the app object as the parameter.
        """
        self.app = flask_app
        self.ruleset = ruleset
        if flask_app:
            self.init_app(flask_app)

    def init_app(self, flask_app):
        """
        Connect the whitelist filter to a Flask application.

        This is called in the :func:`__init__` function if the app
        parameter is passed at that time, but can be called later in order to
        allow a whitelist to be set up before the Flask app is created.

        :parameter app: Required reference to the Flask application to which we
                        will apply the filter.
        """
        flask_app.before_request(self)

    def __call__(self):
        """
        Validate an IP before processing a request.

        When :func:`init_app` is called, it will be registered to run before
        each request. This depends on the Flask request object.

        :returns: Nothing, but raises an exception for Flask to catch if the
                  ruleset determines that the IP address should be blocked.
        """
        x_forwarded_for = request.headers.get('X-Forwarded-For')
        if x_forwarded_for:
            ip_address = x_forwarded_for.split(',')[-1].strip()
        else:
            ip_address = request.remote_addr

        if not self.ruleset.evaluate(ip_address):
            raise Forbidden()
