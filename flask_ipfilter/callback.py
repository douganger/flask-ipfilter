"""IPFilter Whitelist."""


class Callback:
    """
    A ruleset that allows requests by default.

    Hosts and networks will be denied only if they have been explicitly
    permitted with the :func:`deny` function.
    """

    def __init__(self, callback):
        """Initialize the ruleset."""
        self.update(callback)

    def update(self, callback):
        """Update the callback function."""
        self.callback = callback

    def evaluate(self, ip_address):
        """
        Determine whether an IP address is allowed.

        :parameter ip_address: The IP address to check. This must be something
                               that :mod:`ipaddress` can convert into an
                               :class:`ip_address`.

        :returns: True if access should be allowed and False otherwise.
        """
        return self.callback(ip_address)
