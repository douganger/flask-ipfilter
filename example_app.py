from flask import Flask
from flask_ipfilter import IPFilter, Whitelist

app = Flask(__name__)
ip_filter = IPFilter(app, ruleset=Whitelist())

ip_filter.ruleset.permit("127.0.0.1")

@app.route("/")
def route_test():
    return "Allowed."
