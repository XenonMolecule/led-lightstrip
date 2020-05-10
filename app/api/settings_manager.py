from multiprocessing import Lock
from multiprocessing.managers import BaseManager
from threading import Thread

settings = {
	'red':0,
	'green':0,
	'blue': 255
}

lock = Lock()

manager = BaseManager(('', 37844), b'password')
updator = BaseManager(('', 37845), b'password')

def get_setting(setting):
	return settings[setting]
		
def set_setting(setting, value):
	with lock:
		updator.update_setting(setting, value)
		settings[setting] = value
		
manager.register('get_setting', get_setting)
manager.register('set_setting', set_setting)
updator.register('update_setting')
server = manager.get_server()
t = Thread(target=server.serve_forever, args=())
t.start()
updator.connect()
t.join()
