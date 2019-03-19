"""Unit tests for :mod:`flask_ipfilter`."""

import unittest
from flask_ipfilter import Whitelist


class TestWhitelist(unittest.TestCase):
    """
    Test the Whitelist ruleset.

    The following definitions will apply to documentation for this class.

    permit
      Configuring the ruleset to allow an IP address or network.

    allow
       The ruleset's decision to allow a request to continue because the
       source IP address is on the permitted list or is part of a network that
       is on the permitted list.

    deny
      The ruleset's decision to prevent a request from continuing because the
      source IP address is not on the permitted list.
    """

    def setUp(self):
        """Set up unit under test before each test."""
        self.uut = Whitelist()

    def test_evaluate_ip_address(self):
        """
        Default behavior should be to deny an IP address.

        Ask whether an IP address is allowed. We expect it will not be allowed
        because this filter denies access by default.
        """
        self.assertEqual(self.uut.evaluate("127.0.0.1"), False)

    def test_permit_ip_address(self):
        """
        Permitting an IP address should allow that IP address.

        Permit an IP address and then ask whether access is allowed. We expect
        access to be allowed for the permitted IP address.
        """
        self.uut.permit("127.0.0.1")
        self.assertEqual(self.uut.evaluate("127.0.0.1"), True)

    def test_deny_after_permitting_other_address(self):
        """
        Permitting an IP address should not allow another IP address.

        Permit an IP address and then ask whether access is allowed for a
        different address. We expect access will not be allowed because we did
        not permit the address we are asking about.
        """
        self.uut.permit("127.0.0.1")
        self.assertEqual(self.uut.evaluate("192.168.0.1"), False)

    def test_permit_ip_network(self):
        """
        Permitting a network should allow an IP address in that network.

        Permit an entire IP network and ask whether access is allowed to an
        address on that network. We expect access to be allowed because the IP
        address is included in the network range.
        """
        self.uut.permit("192.168.0.0/16")
        self.assertEqual(self.uut.evaluate("192.168.1.1"), True)

    def test_deny_after_permitting_other_network(self):
        """
        Permitting a network should not allow an unrelated IP address.

        Permit an entire IP network and ask whether access is allowed to an
        address not on that network. We expect access to be denied because the
        IP address is not part of the network that has been permitted.
        """
        self.uut.permit("192.168.0.0/16")
        self.assertEqual(self.uut.evaluate("10.0.0.1"), False)

    def test_deny_address_just_off_edge_of_permitted_network(self):
        """
        An IP address just outside the permitted range should be denied.

        Permit an entire IP network and ask whether access is allowed to an
        address just past the edge of the network. We expect access to be
        denied because the address is not part of the network that has been
        permitted.
        """
        self.uut.permit("172.16.0.0/12")
        self.assertEqual(self.uut.evaluate("172.32.0.0"), False)

    def test_error_permitting_invalid_ip(self):
        """
        Attempting to permit an invalid address should raise an error.

        Try to permit an invalid IP address (not a host or a network). We
        expect to get an exception.
        """
        with self.assertRaises(ValueError):
            self.uut.permit("192.168.0.0.0")


if __name__ == "__main__":
    unittest.main()
