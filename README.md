# Flask-IPFilter

[![Build Status](https://travis-ci.org/douganger/flask-ipfilter.svg?branch=master)](https://travis-ci.org/douganger/flask-ipfilter)
[![Documentation Status](https://readthedocs.org/projects/flask-ipfilter/badge/?version=latest)](https://flask-ipfilter.readthedocs.io/en/latest/?badge=latest)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/fbff22f2f804412790ee10601e8b6949)](https://www.codacy.com/app/douganger/flask-ipfilter)

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
