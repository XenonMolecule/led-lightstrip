import sys

sys.path.insert(1, '../../light_control')
sys.path.insert(1, '../../light_control/patterns')
sys.path.insert(1, '../../light_control/iterable_patterns')

from controllights import control_lights
import time
from threading import Thread, Lock
from flask import Flask
from flask import request

app = Flask(__name__)

soloLock = Lock()

@app.route('/time')
def get_current_time():
    return {'time': time.time()}

@app.route('/setcolor', methods=['POST'])
def set_color():
    print(request.get_json())
    return {'success': 'success'}

if __name__ == '__main__':
    defaultSettings = {'red': 0, 'green':255, 'blue': 0}
    t = Thread(target=control_lights, args=(defaultSettings, Lock(), soloLock))
    t.start()
    app.run(host='127.0.0.1', port='5000', debug=True)
    t.join()
