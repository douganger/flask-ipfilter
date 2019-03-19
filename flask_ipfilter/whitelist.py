"""IPFilter Whitelist."""

import ipaddress


class Whitelist:
    """
    A ruleset that denies requests by default.

    Hosts and networks will be allowed only if they have been explicitly
    permitted with the :func:`permit` function.
    """

    def __init__(self):
        """Initialize the ruleset."""
        self.permitted_hosts = set()
        self.permitted_networks = set()

    def evaluate(self, ip_address):
        """
        Determine whether an IP address is allowed.

        :parameter ip_address: The IP address to check. This must be something
                               that :mod:`ipaddress` can convert into an
                               :class:`ip_address`.

        :returns: True if access should be allowed and False otherwise.
        """
        ip_addr = ipaddress.ip_address(ip_address)

        if ip_addr in self.permitted_hosts:
            return True

        for net in self.permitted_networks:
            if ip_addr in net:
                return True

        return False

    def permit(self, ip_address):
        """
        Add a new host or network to the whitelist.

        :parameter ip_address: The IP address to allow. The address parameter
                            accepts anything that the :mod:`ipaddress` module
                            can take as a parameter to :class:`ip_address` or
                            :class:`ip_network`.
        """
        try:
            host = ipaddress.ip_address(ip_address)
            self.permitted_hosts.add(host)
        except ValueError:
            net = ipaddress.ip_network(ip_address)
            self.permitted_networks.add(net)
