import multiprocessing
from light_control.main import run_lights
from app.api.api import run_server

def init_settings(settings, lock):
	with lock:
		settings.red = 255
		settings.green = 0
		settings.blue = 0

if __name__ == "__main__":
	print("TEST")
	mgr = multiprocessing.Manager()
	settings = mgr.Namespace()
	read_lock = multiprocessing.Lock()
	
	init_settings(settings, read_lock)
	
	server = multiprocessing.Process(target=run_server, args=(settings, read_lock))
	lights = multiprocessing.Process(target=run_lights, args=(settings, read_lock))
	
	server.start()
	lights.start()
	
	server.join()
	lights.join()
