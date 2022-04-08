"""IPFilter Whitelist."""

import ipaddress


class Blacklist:
    """
    A ruleset that allows requests by default.

    Hosts and networks will be denied only if they have been explicitly
    permitted with the :func:`deny` function.
    """

    def __init__(self):
        """Initialize the ruleset."""
        self.denied_hosts = set()
        self.denied_networks = set()

    def evaluate(self, ip_address):
        """
        Determine whether an IP address is allowed.

        :parameter ip_address: The IP address to check. This must be something
                               that :mod:`ipaddress` can convert into an
                               :class:`ip_address`.

        :returns: True if access should be allowed and False otherwise.
        """
        ip_addr = ipaddress.ip_address(u''.__class__(ip_address))

        if ip_addr in self.denied_hosts:
            return False

        for net in self.denied_networks:
            if ip_addr in net:
                return False

        return True

    def deny(self, ip_address):
        """
        Add a new host or network to the blacklist.

        :parameter ip_address: The IP address to deny. The address parameter
                            accepts anything that the :mod:`ipaddress` module
                            can take as a parameter to :class:`ip_address` or
                            :class:`ip_network`.
        """
        try:
            host = ipaddress.ip_address(u''.__class__(ip_address))
            self.denied_hosts.add(host)
        except (ValueError, ipaddress.AddressValueError):
            net = ipaddress.ip_network(u''.__class__(ip_address))
            self.denied_networks.add(net)
