from iterable_pattern import IterablePattern

class ITheaterChase(IterablePattern):
	
	def __init__(self, strip, colorFunc, delay = 50, iterations = 10):
		super(ITheaterChase, self).__init__(strip, colorFunc, 3 * iterations, delay)
		
		
	def runStep(self):
		for i in range(self.strip.numPixels()):
			if ((i - self.step) % 3) == 0:
				self.strip.setPixel(i, self.color(i))
			else:
				self.strip.clearPixel(i)
		self.strip.show()
		self.incrementStep()
