import logging

# import gpiozero
from flask import Flask, request
from flask_socketio import SocketIO

from settings import settings
from wpa import connect, scan_for_networks

logger = logging.getLogger(__name__)

app = Flask(__name__)
socketio = SocketIO(app)


@app.route("/health")
def health():
    return {"status": "ok"}


@app.route("/wpa/ssids")
def ssids():
    return {"ssids": scan_for_networks()}


@app.route("/wpa/connect", methods=["POST"])
def connect_to_network():
    data = request.json
    ssid = data["ssid"]
    password = data["password"]
    network_id = connect(ssid, password)
    return {"network_id": network_id}


if __name__ == "__main__":
    socketio.run(app, host=settings.host, port=settings.port)
