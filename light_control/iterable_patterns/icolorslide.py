from iterable_pattern import IterablePattern

class IColorSlide(IterablePattern):
	
	def __init__(self, strip, colorFunc, delay = 20, iterations = 1):
		super(IColorSlide, self).__init__(strip, colorFunc, strip.numPixels() * iterations, delay)
		self.iterations = iterations
		
	def runStep(self):
		j = (self.totalSteps - self.step) % self.totalSteps
		for i in range(self.strip.numPixels()):
			self.strip.setPixel(i, self.color(i + j))
		self.strip.show()
		self.incrementStep()
