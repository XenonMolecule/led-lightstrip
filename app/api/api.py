import time
import json
from multiprocessing.managers import BaseManager
from flask import Flask
from flask import request

app = Flask(__name__)
manager = BaseManager(('', 37844), b'password')
manager.register('get_setting')
manager.register('set_setting')
manager.connect()

@app.route('/time')
def get_current_time():
    return json.dumps({'time': time.time()})

@app.route('/setcolor', methods=['POST'])
def set_color():
    color = request.get_json()
    manager.set_setting('red', color['red'])
    manager.set_setting('green', color['green'])
    manager.set_setting('blue', color['blue'])
    return json.dumps({'success': 'success'})

if __name__ == '__main__':
    app.run(host='127.0.0.1', port='5000', debug=True)
