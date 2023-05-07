"""python 🐍 flask application for tenma power supply."""

__version__ = "0.0.2"

# Import Python Libraries here
import random
from flask import Flask, render_template
from flask import jsonify
from socket import getfqdn

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return render_template('index.html')

@app.route("/get_info", methods=["GET", "POST"])
def get_info():
    power_supply_info = {
        'make': 'tenma power supply',
        'com_port': 'COM4',
        'state': 'ON/OFF',
        'set_voltage': random.randint(0, 30),
        'set_current': random.randint(0, 5),
        'live_voltage': random.randint(0, 30),
        'live_current': random.randint(0, 5)
    }
    return jsonify(power_supply_info)


if __name__ == '__main__':
    app.run(host=getfqdn(), debug=True)
