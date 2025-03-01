import logging

# import gpiozero
from flask import Flask
from flask_socketio import SocketIO

from settings import settings

logger = logging.getLogger(__name__)

app = Flask(__name__)
socketio = SocketIO(app)


if __name__ == "__main__":
    socketio.run(app, host=settings.host, port=settings.port)
