import multiprocessing
from light_control.main import run_lights
from app.api.api import run_server

from multiprocessing import Process
from multiprocessing.sharedctypes import Value
from ctypes import Structure, c_int

class Settings(Structure):
	_fields_ = [
		('red', c_int),
		('green', c_int),
		('blue', c_int)
	]

if __name__ == "__main__":
	settings = Value(Settings, 0, 0, 0)
	read_lock = multiprocessing.Lock()
	
	server = Process(target=run_server, args=(settings, read_lock))
	lights = Process(target=run_lights, args=(settings, read_lock))
	
	server.start()
	lights.start()
	
	server.join()
	lights.join()
