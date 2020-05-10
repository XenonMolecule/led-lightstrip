from multiprocessing.managers import BaseManager
from multiprocessing import Lock
from threading import Thread
import time

class OnlineConn(object):
	
	def __init__(self):
		manager = BaseManager(('', 37844), b'password')
		manager.register('get_setting')
		manager.connect()
		self.manager = manager
		self.settings = {}
		self.updateLock = Lock()
		self.updator = BaseManager(('', 37845), b'password')
		self.updator.register('update_setting', self.update_setting)
		server = self.updator.get_server()
		t = Thread(target=server.serve_forever, args=())
		t.start()
		self.init_settings()
		
	
	def init_settings(self):
		self.settings['red'] = int(str(self.manager.get_setting('red')))
		self.settings['green'] = int(str(self.manager.get_setting('green')))
		self.settings['blue'] = int(str(self.manager.get_setting('blue')))
		
	def update_setting(self, setting, value):
		with self.updateLock:
			self.settings[setting] = value
		
	def getColor(self):
		color = {'red':0, 'green':0, 'blue':0}
		with self.updateLock:
			color['red'] = self.settings['red']
			color['green'] = self.settings['green']
			color['blue'] = self.settings['blue']
			return color
