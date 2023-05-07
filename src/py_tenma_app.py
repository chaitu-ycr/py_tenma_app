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
    return render_template('home.html')

@app.route("/live_ps_info", methods=["GET"])
def live_ps_info():
    return render_template('live_ps_info.html')

@app.route("/control_ps", methods=["GET"])
def control_ps():
    return render_template('control_ps.html')

@app.route("/get_live_info", methods=["GET", "POST"])
def get_live_info():
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
