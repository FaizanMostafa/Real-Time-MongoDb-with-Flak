from flask_socketio import SocketIO, join_room, leave_room, emit, disconnect
import json

def init(socketio):
    @socketio.on('connect')
    def connectIO():
        print("a user connected")

    @socketio.on('disconnect')
    def disconnectIO():
        print('a client disconnected')

    # def on_new_insert(data):
    #     emit('new_document_inserted', data)