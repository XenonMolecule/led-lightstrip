from pattern import Pattern

class ColorSlide(Pattern):
	
	def __init__(self, strip, colorFunc, updateRate, iterations = 1):
		super(ColorSlide, self).__init__(strip, colorFunc, updateRate)
		self.iterations = iterations
	
	def execute(self):
		for j in range(self.strip.numPixels() * self.iterations - 1, -1, -1):
			for i in range(self.strip.numPixels()):
				self.strip.setPixel(i, self.color(i + j))
			self.strip.show()
			self.pause()
