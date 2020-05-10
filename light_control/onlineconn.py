from multiprocessing.managers import BaseManager

class OnlineConn(object):
	
	def __init__(self):
		manager = BaseManager(('', 37844), b'password')
		manager.register('get_setting')
		manager.register('update_setting', self.update_setting)
		manager.connect()
		self.manager = manager
		self.settings = {}
		self.init_settings()
	
	def init_settings(self):
		self.settings['red'] = int(str(self.manager.get_setting('red')))
		self.settings['green'] = int(str(self.manager.get_setting('green')))
		self.settings['blue'] = int(str(self.manager.get_setting('blue')))
		
	def update_setting(self, setting, value):
		self.settings[setting] = value
		
	def getColor(self):
		color = {'red':0, 'green':0, 'blue':0}
		color['red'] = self.settings['red']
		color['green'] = self.settings['green']
		color['blue'] = self.settings['blue']
		return color
