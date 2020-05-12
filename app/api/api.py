import time
import json
import multiprocessing
from flask import Flask
from flask import request

app = Flask('api')
settings = None
lock = None

@app.route('/time')
def get_current_time():
    return json.dumps({'time': time.time()})

@app.route('/setcolor', methods=['POST'])
def set_color():
    color = request.get_json()
    with lock:
        settings.red = color['red']
        settings.green = color['green']
        settings.blue = color['blue']
    return json.dumps({'success': 'success'})

def run_server(settings_link, read_lock):
    global settings
    global lock
    settings = settings_link
    lock = read_lock
    app.run(host='127.0.0.1', port='5000', debug=True, use_reloader=False)

if __name__ == "__main__":
    run_server(multiprocessing.Manager().Namespace(), multiprocessing.Lock())
