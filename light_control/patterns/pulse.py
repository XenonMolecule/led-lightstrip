from pattern import Pattern
import math

class Pulse(Pattern):
	
	def __init__(self, strip, colorFunc, duration):
		super(Pulse, self).__init__(strip, colorFunc, duration / 20.0)
		
	def progress(self, i):
		return 64 * (math.sin(((math.pi/10) * i) - (math.pi/2)) + 1)
	
	def execute(self):
		for j in range(20):
			prog = self.progress(j)
			for i in range(self.strip.numPixels()):
				self.strip.setPixel(i, self.color(int(round(prog))))
			self.strip.show()
			self.pause()
		for i in range(self.strip.numPixels()):
			self.strip.setPixel(i, self.color(256))
		self.strip.show()
