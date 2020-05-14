import time
import json
import multiprocessing
from flask import Flask
from flask import request
from flask_socketio import SocketIO, emit

app = Flask('api')
socketio = SocketIO(app)
settings = None
lock = None

@app.route('/api/time')
def get_current_time():
    return json.dumps({'time': time.time()})

@socketio.on('setcolor')
def set_color(message):
    with lock:
        settings.red = int(message['red'])
        settings.green = int(message['green'])
        settings.blue = int(message['blue'])

@socketio.on('connect')
def connect():
    print("New Connection")
    
@socketio.on('disconnect')
def disconnect():
    print("Client disconnected")

def run_server(settings_link, read_lock):
    global settings
    global lock
    settings = settings_link
    lock = read_lock
    socketio.run(app, host='127.0.0.1', port='5000', debug=False, use_reloader=False)

if __name__ == "__main__":
    run_server(multiprocessing.Manager().Namespace(), multiprocessing.Lock())
