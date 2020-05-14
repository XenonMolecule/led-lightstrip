from pattern import Pattern
from light_control.colors import calcGradient
import random

class Sparkle(Pattern):
	
	def __init__(self, strip, backgroundColor, sparkleColor, updateRate, looping = False, iterations=256, sparkleDensity=0.0075, sparkleDuration=64):
		super(Sparkle, self).__init__(strip, backgroundColor, updateRate)
		self.sparkle = sparkleColor
		self.iterations = iterations
		self.sparkleDensity = sparkleDensity
		self.sparkleDuration = sparkleDuration
		self.looping = looping
		self.sparkles = {}

	def execute(self):
		if not self.looping:
			self.sparkles = {}
		for i in range(self.iterations):
			for n in range(self.strip.numPixels()):
				if ((self.looping or self.iterations - i > self.sparkleDuration) and random.random() < self.sparkleDensity):
					sparkle_time = self.sparkles.get(n, 0)
					if sparkle_time == 0:
						self.sparkles[n] = self.sparkleDuration
				self.strip.setPixel(n, self.color(n))
			for n in self.sparkles:
				mid = (self.sparkleDuration // 2) * 1.0
				progress = (mid - ((mid + self.sparkles[n]) % self.sparkleDuration)) / mid
				progress = min(abs(progress), 1)
				self.strip.setPixel(n, calcGradient(self.color(n), self.sparkle(n), progress))
				if(self.sparkles[n] > 0):
					self.sparkles[n] -= 1
			self.strip.show()
			self.pause()
