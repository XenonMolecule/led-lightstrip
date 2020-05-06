from pattern import Pattern

class ColorWipe(Pattern):
	
	def execute(self):
		for i in range(self.strip.numPixels()):
			self.strip.setPixelUpdate(i, self.color(i))
			self.pause()
