from iterable_pattern import IterablePattern
from light_control.colors import calcGradient
import random

class ISparkle(IterablePattern):
	
	def __init__(self, strip, backgroundColor, sparkleColor, delay = 20, looping = False, iterations=256, sparkleDensity=0.0075, sparkleDuration=64):
		super(ISparkle, self).__init__(strip, backgroundColor, iterations, delay)
		self.sparkle = sparkleColor
		self.sparkleDensity = sparkleDensity
		self.sparkleDuration = sparkleDuration
		self.looping = looping
		self.sparkles = {}

	def runStep(self):
		for n in range(self.strip.numPixels()):
			if ((self.looping or self.getTotalSteps() - self.getStep() > self.sparkleDuration) and random.random() < self.sparkleDensity):
				sparkle_time = self.sparkles.get(n, 0)
				if sparkle_time == 0:
					self.sparkles[n] = self.sparkleDuration
			self.strip.setPixel(n, self.color(n))
		for n in self.sparkles:
			mid = (self.sparkleDuration // 2) * 1.0
			progress = (mid - ((mid + self.sparkles[n]) % self.sparkleDuration)) / mid
			progress = min(abs(progress), 1)
			self.strip.setPixel(n, calcGradient(self.color(n), self.sparkle(n), progress))
			if self.sparkles[n] > 0:
				self.sparkles[n] -= 1
		self.strip.show()
		self.incrementStep()
		
	def reset(self):
		super(ISparkle, self).reset()
		if not self.looping:
			self.sparkles = {}
