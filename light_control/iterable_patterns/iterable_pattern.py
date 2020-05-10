class IterablePattern(object):
	
	def __init__(self, strip, colorFunc, totalSteps):
		self.strip = strip
		self.color = colorFunc
		self.step = 0
		self.totalSteps = totalSteps
		
	def setColorFunc(self, colorFunc):
		self.color = colorFunc
	
	def getStep(self):
		return self.step
		
	def reset(self):
		self.step = 0
		
	def incrementStep(self):
		self.step += 1
		
	def isDone(self):
		return self.step >= self.totalSteps
	
	def runStep(self):
		pass
