from multiprocessing.managers import BaseManager

class OnlineConn(object):
	
	def __init__(self):
		manager = BaseManager(('', 37844), b'password')
		manager.register('get_setting')
		manager.connect()
		self.manager = manager
		
	def getColor(self):
		color = {'red':0, 'green':0, 'blue':0}
		color['red'] = int(str(self.manager.get_setting('red')))
		color['green'] = int(str(self.manager.get_setting('green')))
		color['blue'] = int(str(self.manager.get_setting('blue')))
		return color
