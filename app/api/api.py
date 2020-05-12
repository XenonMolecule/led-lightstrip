import time
import json
import multiprocessing
from flask import Flask
from flask import request

app = Flask('api')
# manager = BaseManager(('', 37844), b'password')
# manager.register('get_setting')
# manager.register('set_setting')
# manager.connect()

@app.route('/time')
def get_current_time():
    return json.dumps({'time': time.time()})

@app.route('/setcolor', methods=['POST'])
def set_color():
    color = request.get_json()
    # manager.set_setting('red', color['red'])
    # manager.set_setting('green', color['green'])
    # manager.set_setting('blue', color['blue'])
    return json.dumps({'success': 'success'})

def run_server(settings, read_lock):
    app.run(host='127.0.0.1', port='5000', debug=True, use_reloader=False)

if __name__ == "__main__":
    run_server(multiprocessing.Manager().Namespace(), multiprocessing.Lock())
