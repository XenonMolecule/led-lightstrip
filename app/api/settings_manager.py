from multiprocessing import Lock
from multiprocessing.managers import BaseManager

settings = {
	'red':0,
	'green':0,
	'blue': 255
}

lock = Lock()

manager = BaseManager(('', 37844), b'password')

def get_setting(setting):
	return settings[setting]
		
def set_setting(setting, value):
	with lock:
		manager.update_setting(setting, value)
		settings[setting] = value
		
manager.register('get_setting', get_setting)
manager.register('set_setting', set_setting)
manager.register('update_setting')
server = manager.get_server()
server.serve_forever()


