import multiprocessing

class OnlineConn(object):
	
	def __init__(self, settings, lock):
		self.settings = settings
		self.lock = lock
		print(settings['red'])
		
	def getColor(self):
		color = {'red':0, 'green':0, 'blue':0}
		with self.lock:
			color['red'] = self.settings.red
			color['green'] = self.settings.green
			color['blue'] = self.settings.blue
			return color
