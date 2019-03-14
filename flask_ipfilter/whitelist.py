"""Code for filtering Flask requests based on an IP address whitelist."""

import ipaddress
from flask import request
from werkzeug.exceptions import Forbidden


class Whitelist:
    """An IP address whitelist filter for Flask."""

    def __init__(self, app=None):
        """Initialize the whitelist filter."""
        self.addresses = set()
        self.networks = set()
        if app:
            self.init_app(app)

    def init_app(self, app):
        """
        Connect the whitelist filter to a Flask application.

        This is called in the :func:`__init__` function if the app
        parameter is passed at that time, but can be called later in order to
        allow a whitelist to be set up before the Flask app is created.
        """
        self.app = app
        self.app.before_request(self.validate_ip)

    def whitelist(self, address):
        """
        Add a new host or network to the whitelist.

        :parameter address: The IP address to allow. The address parameter
                            accepts anything that the :mod:`ipaddress` module
                            can take as a parameter to :class:`ip_address` or
                            :class:`ip_network`.
        """
        try:
            host = ipaddress.ip_address(address)
            self.addresses.add(host)
        except ValueError:
            net = ipaddress.ip_network(address)
            self.networks.add(net)

    def check(self, address):
        """
        Check an IP address against the whitelist.

        :parameter address: The IP address to check.

        :returns: True if access should be allowed and False otherwise.
        """
        ip_addr = ipaddress.ip_address(address)

        if ip_addr in self.addresses:
            return True

        for net in self.networks:
            if ip_addr in net:
                return True

        return False

    def validate_ip(self):
        """
        Validate an IP before processing a request.

        When :func:`init_app` is called, it will be registered to run before
        each request.

        This depends on the Flask request object.

        :returns: A denied message with HTTP status 403 if the IP address
                  associated with the request object is not allowed.
                  Otherwise, nothing.
        """
        x_forwarded_for = request.headers.get('X-Forwarded-For')
        if x_forwarded_for:
            ip_addr = x_forwarded_for.split(',')[-1].strip()
        else:
            ip_addr = request.remote_addr

        if not self.check(ip_addr):
            raise Forbidden()
