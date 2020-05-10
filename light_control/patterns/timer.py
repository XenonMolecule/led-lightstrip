from pattern import Pattern

class Timer(Pattern):
	
	def __init__(self, strip, colorFunc, time):
		super(Timer, self).__init__(strip, colorFunc, time * 1.0 / strip.numPixels())
		
	def execute(self):
		for i in range(self.strip.numPixels()):
			self.strip.setPixel(i, self.color(i))
		self.strip.show()
		for i in range(self.strip.numPixels() - 1, -1, -1):
			self.strip.clearPixel(i)
			self.strip.show()
			self.pause()
