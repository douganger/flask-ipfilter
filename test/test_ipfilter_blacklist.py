"""Integration tests for IPFilter with Whitelist ruleset."""

import unittest
import flask
from flask_ipfilter import IPFilter, Blacklist


class TestIPFilterWhiteList(unittest.TestCase):
    """Test integration between IPFilter and WhiteList ruleset."""

    def setUp(self):
        """Set up the test case."""
        self.app = flask.Flask(__name__)
        self.app.add_url_rule('/', 'index', lambda: "OK")
        self.client = self.app.test_client()
        self.ruleset = Blacklist()
        self.ipfilter = IPFilter(self.app, ruleset=self.ruleset)
        self.request_env = {"REMOTE_ADDR": "192.168.0.1"}

    def test_request_allowed_by_default(self):
        """All requests should be permitted by default."""
        response = self.client.get("/", environ_base=self.request_env)
        self.assertEqual(response.status_code, 200)

    def test_request_blocked_after_deny(self):
        """A request from a denied IP address should be denied."""
        self.ruleset.deny("192.168.0.1")
        response = self.client.get("/", environ_base=self.request_env)
        self.assertEqual(response.status_code, 403)
