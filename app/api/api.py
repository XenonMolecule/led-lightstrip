from controllights import control_lights
import time
from threading import Thread, Lock
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/time')
def get_current_time():
    return {'time': time.time()}

@app.route('/setcolor', methods=['POST'])
def set_color():
    print(request.get_json())
    return {'success': 'success'}
