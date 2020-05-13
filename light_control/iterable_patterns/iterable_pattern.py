import time

class IterablePattern(object):
	
	def __init__(self, strip, colorFunc, totalSteps, delay):
		self.strip = strip
		self.color = colorFunc
		self.step = 0
		self.totalSteps = totalSteps
		self.delay = delay
	
	def setColorFunc(self, colorFunc):
		self.color = colorFunc
		
	def setTotalSteps(self, totalSteps):
		self.totalSteps = totalSteps
		
	def getTotalSteps(self):
		return self.totalSteps
		
	def setStep(self, step):
		self.step = step
		
	def getStep(self):
		return self.step
		
	def reset(self):
		self.step = 0
		
	def incrementStep(self):
		self.step += 1
		
	def pause(self):
		time.sleep(self.delay/1000.0)
		
	def isDone(self):
		return self.step >= self.totalSteps
	
	def runStep(self):
		pass
