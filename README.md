# README

Flask-IPFilter is a simple Flask extension to limit access to a site to certain
IP addresses. The current implementation is a minimal proof of concept with some
important limitations:

-   IP addresses and networks must be whitelisted. All hosts are blocked by
    default. There is currently no blacklist mode to allow hosts by default.

-   The current implementation trusts the X-Forwarded-For header and uses the
    last IP address in that header if multiple IP addresses are listed.

## Quickstart

Install Flask-IPFilter with the command, `pip install flask-ipfilter`.

The following minimal Flask application demonstrates how to use Flask-IPFilter
in your application.

```python
from flask import Flask
from flask_ipfilter import Whitelist

app = Flask(__name__)
ip_filter = Whitelist(app)

ip_filter.whitelist("127.0.0.1")

@app.route("/")
def route_test():
    return "Allowed."
```
