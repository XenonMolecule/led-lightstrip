from pattern import Pattern

class Macro(Pattern):
	def __init__(self, *patterns):
		self.delay = 0
		self.sequence = [pattern for pattern in patterns]
		
	def append(self, pattern):
		self.sequence.append(patten)
		
	def pop(self, index = -1):
		return self.sequence.pop(index)
		
	def insert(self, index, element):
		self.sequence.insert(index, element)
		
	def execute(self):
		for pattern in self.sequence:
			pattern.execute()
