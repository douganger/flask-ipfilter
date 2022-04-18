"""
Filter access to Flask web applications based on originating IP address.

This package contains a minimum viable implementation of a whitelist filter
appropriate for restricting access to Heroku-hosted application based on the
requestor's IP address.

This package trusts the last IP address in the X-Forwarded-For header and is
therefore appropriate only for applications that are running behind a trusted
load balancer.
"""

from flask_ipfilter.ipfilter import IPFilter
from flask_ipfilter.whitelist import Whitelist
from flask_ipfilter.blacklist import Blacklist
from flask_ipfilter.callback import Callback
