import time

class Pattern(object):
	
	def __init__(self, strip, colorFunc, updateRate):
		self.strip = strip
		self.color = colorFunc
		self.delay = updateRate
		
	def setColorFunc(self, colorFunc):
		self.color = colorFunc
		
	def setUpdateRate(self, updateRate):
		self.delay = updateRate 
		
	def pause(self):
		time.sleep(self.delay/1000.0)
		
	def execute(self):
		pass
