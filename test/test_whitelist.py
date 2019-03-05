"""Unit tests for :mod:`flask_ipfilter`."""

import unittest
from flask_ipfilter import Whitelist


class TestWhitelist(unittest.TestCase):
    """Unit tests for :class:`Whitelist`."""

    def setUp(self):
        """Set up unit under test before each test."""
        self.uut = Whitelist()

    def test_request_blocked_by_default(self):
        """
        Test whether an IP address is allowed with no configuration.

        All IP addresses should be blocked until specific hosts and/or
        networks have been added to the whitelist.
        """
        self.assertEqual(self.uut.check("127.0.0.1"), False)

    def test_request_allowed_by_host(self):
        """Test whether an IP address is allowed after whitelisting."""
        self.uut.whitelist("127.0.0.1")
        self.assertEqual(self.uut.check("127.0.0.1"), True)

    def test_request_allowed_by_network(self):
        """
        Test whether addresses are allowed after whitelisting a network.

        We expect an address in the allowed network to be allowed, but an
        address just outside the allowed network should be denied.
        """
        self.uut.whitelist("172.16.0.0/12")
        self.assertEqual(self.uut.check("172.31.255.255"), True)
        self.assertEqual(self.uut.check("172.32.0.0"), False)


if __name__ == "__main__":
    unittest.main()
