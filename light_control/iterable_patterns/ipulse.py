from light_control.iterable_patterns.iterable_pattern import IterablePattern
import math

class IPulse(IterablePattern):
	
	def __init__(self, strip, colorFunc, duration):
		super(IPulse, self).__init__(strip, colorFunc, 20, duration/20.0)
		
	def calc_progress(self, i):
		return 64 * (math.sin(((math.pi/10) * i) - (math.pi/2)) + 1)
	
	def runStep(self):
		j = (self.step % self.totalSteps) + 1
		prog = int(round(self.calc_progress(j)))
		for i in range(self.strip.numPixels()):
			self.strip.setPixel(i, self.color(prog))
		self.strip.show()
		self.incrementStep()
