import multiprocessing

# settings:
# {
# 	back_red: 0,
#	back_green: 0,
#	back_blue: 0,
#	fore_red: 0,
#	fore_green: 0,
#	fore_blue: 0,
#	queue_patt: "",  MAX LENGTH 10
#	hold_patt: false
# }

class OnlineConn(object):
	
	def __init__(self, settings, lock):
		self.settings = settings
		self.lock = lock
		
	def getBackgroundColor(self):
		color = {'red':0, 'green':0, 'blue':0}
		with self.lock:
			color['red'] = self.settings.back_red
			color['green'] = self.settings.back_green
			color['blue'] = self.settings.back_blue
			return color

	def getForegroundColor(self):
		color = {'red':0, 'green':0, 'blue':0}
		with self.lock:
			color['red'] = self.settings.fore_red
			color['green'] = self.settings.fore_green
			color['blue'] = self.settings.fore_blue
			return color

	def getNextPattern(self):
		with self.lock:
			return self.settings.queue_patt

	def setNextPattern(self, patt_string):
		with self.lock:
			self.settings.queue_patt = patt_string

	def shouldHoldPattern(self):
		with self.lock:
			return self.settings.hold_patt