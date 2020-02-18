from flask import Flask, request
from flask_socketio import SocketIO
from socket_events import init
from flask_cors import CORS

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")
init(socketio)

if __name__ == "__main__":
    socketio.run(app)
    import change_streams