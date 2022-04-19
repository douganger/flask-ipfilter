Flask-IPFilter
==============

Flask-IPFilter is a simple Flask extension to limit access to a site by based
on the source IP address. The current implementation has one very important
limitation:

 - The current implementation trusts the X-Forwarded-For header and uses the
   last IP address in that header if multiple IP addresses are listed.

Flask-IPFilter uses rulesets to decide whether a request will be allowed or
denied. Three rulesets are provided with Flask-IPFilter:

 - The Whitelist ruleset blockes all access except from IP addresses that have
   been explicitly permitted.

 - The Blacklist ruleset allows all access except from IP addresses thar have
   been explicitly denied.

 - The Callback ruleset passes the originating IP address to a user-defined
   function, which can return True to allow access or False to deny access.
 
Users can also register functions to be called by Flask-IPFilter in the event
of either an allowed or denied request. This can be useful for integrating
Flask-IPFilter with a centralized logging service or intrusion detection
system.

Quickstart
----------

Install Flask-IPFilter with the command, :command:`pip install flask-ipfilter`.

The following minimal Flask application demonstrates how to use Flask-IPFilter
with a Whitelist ruleset in your application.

.. code-block:: python

    from flask import Flask
    from flask_ipfilter import IPFilter, Whitelist

    app = Flask(__name__)
    ip_filter = IPFilter(app, ruleset=Whitelist())

    ip_filter.ruleset.permit("127.0.0.1")

    @app.route("/")
    def route_test():
        return "Allowed."


More Information
----------------

.. toctree::
   :maxdepth: 2

   modules


Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
