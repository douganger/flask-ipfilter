# Flask-IPFilter

[![Build Status](https://travis-ci.org/douganger/flask-ipfilter.svg?branch=master)](https://travis-ci.org/douganger/flask-ipfilter)
[![Coverage Status](https://coveralls.io/repos/github/douganger/flask-ipfilter/badge.svg?branch=master)](https://coveralls.io/github/douganger/flask-ipfilter?branch=master)
[![Documentation Status](https://readthedocs.org/projects/flask-ipfilter/badge/?version=latest)](https://flask-ipfilter.readthedocs.io/en/latest/?badge=latest)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/545d4bfe0bee4a47a7235b4f2205bae1)](https://www.codacy.com/gh/douganger/flask-ipfilter/dashboard)

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
from flask_ipfilter import IPFilter, Whitelist

app = Flask(__name__)
ip_filter = IPFilter(app, ruleset=Whitelist())

ip_filter.ruleset.permit("127.0.0.1")

@app.route("/")
def route_test():
    return "Allowed."
```
