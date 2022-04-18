"""Integration tests for IPFilter with Whitelist ruleset."""

import unittest
import flask
from flask_ipfilter import IPFilter, Callback


class TestIPFilterWhiteList(unittest.TestCase):
    """Test integration between IPFilter and WhiteList ruleset."""

    def setUp(self):
        self.app = flask.Flask(__name__)
        self.app.add_url_rule('/', 'index', lambda: "OK")
        self.client = self.app.test_client()
        self.request_env = {"REMOTE_ADDR": "192.168.0.1"}

    def test_request_allowed(self):
        """A request should be allowed when the callback function permits it."""

        # Arrange
        self.ruleset = Callback(lambda ip : True)
        self.ipfilter = IPFilter(self.app, ruleset=self.ruleset)

        # Act
        response = self.client.get("/", environ_base=self.request_env)

        # Assert
        self.assertEqual(response.status_code, 200)

    def test_request_blocked(self):
        """A request should be denied when the callback function denies it."""

        # Arrange
        self.ruleset = Callback(lambda ip : False)
        self.ipfilter = IPFilter(self.app, ruleset=self.ruleset)

        # Act
        response = self.client.get("/", environ_base=self.request_env)

        # Assert
        self.assertEqual(response.status_code, 403)
