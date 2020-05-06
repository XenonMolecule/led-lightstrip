from pattern import Pattern

class TheaterChase(Pattern):
	
	def __init__(self, strip, colorFunc, updateRate, iterations = 10):
		super(TheaterChase, self).__init__(strip, colorFunc, updateRate)
		self.iterations = iterations
		
	def setIterations(self, iterations):
		self.iterations = iterations
	
	def execute(self):
		for j in range(self.iterations):
			for q in range(3):
				for i in range(0, self.strip.numPixels(), 3):
					self.strip.setPixel(i + q, self.color(i + q))
				self.strip.show()
				self.pause()
				for i in range(0, self.strip.numPixels(), 3):
					self.strip.clearPixel(i + q)
