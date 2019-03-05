from flask import Flask
from flask_ipfilter import Whitelist

app = Flask(__name__)
filter = Whitelist(app)

filter.whitelist("127.0.0.1")

@app.route("/")
def route_test():
    return "Allowed."
