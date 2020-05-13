from iterable_pattern import IterablePattern

class ILoop(IterablePattern):
	
	def __init__(self, pattern, iterations = 1):
		self.pattern = pattern
		self.iterations = iterations
		super(ILoop, self).__init__(None, None, pattern.getTotalSteps() * iterations, 0)
	
	def reset(self):
		super(ILoop, self).reset()
		self.pattern.reset()
		
	def pause(self):
		self.pattern.pause()
	
	def runStep(self):
		if self.pattern.isDone():
			self.pattern.reset()
		self.pattern.runStep()
		self.incrementStep()
