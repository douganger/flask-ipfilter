from flask import Flask
from flask_ipfilter import Whitelist

app = Flask(__name__)
ip_filter = Whitelist(app)

ip_filter.whitelist("127.0.0.1")

@app.route("/")
def route_test():
    return "Allowed."
