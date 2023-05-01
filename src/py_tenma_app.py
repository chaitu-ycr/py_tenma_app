"""python 🐍 flask application for tenma power supply."""

__version__ = "0.0.1"

# Import Python Libraries here
from flask import Flask
from socket import getfqdn
from datetime import datetime

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return f"""<meta http-equiv="refresh" content="1"/>
    Hello World!<br>The current time is {format(datetime.strftime(datetime.now(), "%d %B %Y %X"))}."""


if __name__ == '__main__':
    app.run(host=getfqdn(), debug=True)
