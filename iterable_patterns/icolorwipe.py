from iterable_pattern import IterablePattern

class IColorWipe(IterablePattern):
	
	def __init__(self, strip, colorFunc):
		super(IColorWipe, self).__init__(strip, colorFunc, strip.numPixels())
	
	def runStep(self):
		step = min(self.step, self.strip.numPixels())
		for i in range(step):
			self.strip.setPixel(i, self.color(i))
		for i in range(step, self.strip.numPixels()):
			self.strip.clearPixel(i)
		self.strip.show()
		self.incrementStep()
