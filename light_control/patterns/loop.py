from pattern import Pattern

class Loop(Pattern):
	def __init__(self, pattern, iterations):
		self.pattern = pattern
		self.iterations = iterations
		self.delay = 0
		
	def execute(self):
		for i in range(self.iterations):
			self.pattern.execute()
