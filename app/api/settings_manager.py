from multiprocessing import Lock
from multiprocessing.managers import BaseManager

settings = {
	'red':0,
	'green':0,
	'blue': 255
}
readLock = Lock()

lock = Lock()

def get_settings():
	with lock:
		return settings
		
def get_read_lock():
	with lock:
		return readLock
		
manager = BaseManager(('', 37844), b'password')
manager.register('get_settings', get_settings)
manager.register('get_read_lock', get_read_lock)
server = manager.get_server()
server.serve_forever()


