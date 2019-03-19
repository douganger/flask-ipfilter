"""Tests for the IPFilter class."""

import unittest
from unittest.mock import Mock
import flask
from flask_ipfilter import IPFilter


class TestFlaskIPFilter(unittest.TestCase):
    """
    Test the IPFilter class.

    The :class:`IPFilter` binds to a Flask application and blocks requests from
    unauthorized IP addresses.
    """

    def setUp(self):
        """
        Set up the test case.

        For these tests, we will use a minimal application with a single route.
        """
        self.app = flask.Flask(__name__)
        self.app.add_url_rule('/', 'index', lambda: "OK")
        self.client = self.app.test_client()

    def test_canary(self):
        """
        Make sure Flask and the test framework are working.

        This doesn't test any code in the project itself.
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_bind_to_flask_application(self):
        """
        Test binding to a Flask application on initialization.

        The IPFilter should know what app it's connected to and the Flask
        application should call the filter before processing each request.
        """
        uut = IPFilter(self.app)

        self.assertEqual(uut.app, self.app)
        self.assertIn(uut, self.app.before_request_funcs[None])

    def test_bind_to_flask_application_after_initialization(self):
        """
        Test binding to Flask application after initialization.

        Bind an instance of IPFilter to a Flask application. Per the Flask
        documentation, extensions bound in this way should not be restricted to
        this single app. We still expect the filter to be called before every
        request to the Flask application.
        """
        uut = IPFilter()
        uut.init_app(self.app)

        self.assertEqual(uut.app, None)
        self.assertIn(uut, self.app.before_request_funcs[None])

    def test_deny_request(self):
        """
        Test denying a request.

        Set up an IPFilter that will block all requests and verify that a
        request is actually denied. We expect the response to have an HTTP
        status of 403.
        """
        ruleset = Mock()
        ruleset.evaluate = Mock(return_value=False)
        IPFilter(self.app, ruleset=ruleset)

        response = self.client.get("/")
        self.assertEqual(response.status_code, 403)
        ruleset.evaluate.assert_called()

    def test_allow_request(self):
        """
        Test allowing a request.

        Set up an IPFilter that will allow all requests and verify that a
        request is actually allowed. We expect the response to have an HTTP
        status of 200.
        """
        ruleset = Mock()
        ruleset.evaluate = Mock(return_value=True)
        IPFilter(self.app, ruleset=ruleset)

        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        ruleset.evaluate.assert_called()

    def test_ruleset_evaluates_request_ip_address(self):
        """
        The IPFilter should take the IP address rom the Flask request context.

        We can test this by checking whether the IP address passed to the
        ruleset matches the remote_addr from the request object.
        """
        ruleset = Mock()
        IPFilter(self.app, ruleset=ruleset)
        self.client.get("/", environ_base={"REMOTE_ADDR": "192.168.0.1"})
        ruleset.evaluate.assert_called_with("192.168.0.1")

    def test_ruleset_evaluates_x_forwarded_for_ip_address(self):
        """
        Filter should trust the last address in the X-Forwarded-For header.

        If the X-Forwareded-For header exists in the request, we should trust
        it. We can test this by checking whther the IP address passed to the
        ruleset matches this address.
        """
        ruleset = Mock()
        IPFilter(self.app, ruleset=ruleset)
        self.client.get("/",
                        environ_base={"REMOTE_ADDR": "192.168.0.1"},
                        headers={"X-FORWARDED-FOR": "10.0.0.1,172.16.0.1"})
        ruleset.evaluate.assert_called_with("172.16.0.1")


if __name__ == "__main__":
    unittest.main()
