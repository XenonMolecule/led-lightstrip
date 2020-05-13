from iterable_pattern import IterablePattern

class EmptyIPatt(IterablePattern):
	
	def __init__(self):
		super(EmptyIPatt, self).__init__(None, None, 1, 10)
		
	def runStep(self):
		self.incrementStep()

class IMacro(IterablePattern):
	
	def __init__(self, *ipatterns):
		self.sequence = [ipattern for ipattern in ipatterns]
		self.curr_patt = EmptyIPatt()
		self.isEmpty = False
		if len(self.sequence) > 0:
			self.curr_patt = self.sequence[0]
		else:
			self.isEmpty = True
			self.sequence.append(self.curr_patt)
		self.curr_index = 0
		self.end_steps = []
		totalSteps = 0
		for pattern in self.sequence:
			totalSteps += pattern.getTotalSteps()
			self.end_steps.append(totalSteps)
		super(IMacro, self).__init__(None, None, totalSteps, 0)
		
	def reset(self):
		super(IMacro, self).reset()
		self.curr_index = 0
		self.curr_patt = self.sequence[0]
		for pattern in self.sequence:
			pattern.reset()
		
	def pause(self):
		self.curr_patt.pause()
		
	def runStep(self):
		if (self.curr_patt.isDone()):
			self.curr_index += 1
			self.curr_patt = self.sequence[self.curr_index]
		self.curr_patt.runStep()
		self.incrementStep()
	
	# Helper method to replace the empty pattern that prevents the macro
	# from being completely empty
	def addToEmpty(self, pattern):
		self.sequence[0] = pattern
		self.end_steps[0] = pattern.getTotalSteps()
		self.setTotalSteps(pattern.getTotalSteps())
		self.reset()
		self.isEmpty = False
		
	# append a pattern to the macro
	#  Macro can continue running even if pattern was appended midway
	#  through running it
	def append(self, pattern):
		if (self.isEmpty):
			self.addToEmpty(pattern)
			return
		self.sequence.append(pattern)
		self.setTotalSteps(self.getTotalSteps() + pattern.getTotalSteps())
		self.end_steps.append(self.getTotalSteps())
	
	# insert a pattern into the macro at the specified index
	#  Contains all logic for keeping the sequence going even though
	#  the pattern could've been inserted midway through running it
	def insert(self, index, pattern):
		if (self.isEmpty):
			self.addToEmpty(pattern)
			return
		if (index == -1):
			index = len(self.sequence) - 1
		self.setTotalSteps(self.getTotalSteps() + pattern.getTotalSteps())
		self.sequence.insert(index, pattern)
		# shift all the end steps by the total steps of the inserted pattern
		for i in range(index, len(self.end_steps)):
			self.end_steps[i] += pattern.getTotalSteps()
		last_stop = 0 if index == 0 else self.end_steps[index - 1]
		self.end_steps.insert(index, pattern.getTotalSteps() + last_stop)
		# if this pattern was already supposed to have started
		if self.getStep() > last_stop:
			# push progress past this pattern
			self.setStep(self.getStep() + pattern.getTotalSteps())
			self.curr_index += 1
		if self.getStep() == last_stop:
			self.curr_patt = self.sequence[self.curr_index]
	
	# pop a pattern out of the macro at specified index
	#  Contains all logic for keeping the sequence going even though
	#  the pattern could've been popped midway through running it
	def pop(self, index = -1):
		if (self.isEmpty):
			return
		if (len(self.sequence) == 1):
			rem = self.sequence[0]
			self.sequence[0] = EmptyIPatt()
			self.end_steps[0] = self.sequence[0].getTotalSteps()
			self.setTotalSteps(self.sequence[0].getTotalSteps())
			self.isEmpty = True
			self.reset()
			return rem
		if (index == -1):
			index = len(self.sequence) - 1
		rem = self.sequence.pop(index)
		self.end_steps.pop(index)
		self.setTotalSteps(self.getTotalSteps() - rem.getTotalSteps())
		# shift all the end steps by the total steps of the removed pattern
		for i in range(index, len(self.end_steps)):
			self.end_steps[index] -= rem.getTotalSteps()
		last_stop = 0 if index == 0 else self.end_steps[index - 1]
		rem_stop = last_stop + rem.getTotalSteps()
		# if this pattern was happening or already happened
		if (self.getStep() > last_stop):
			# it was happening or literally was just finishing up
			if (self.getStep() <= rem_stop):
				self.setStep(self.getStep() - rem.getStep())
				self.curr_patt = self.sequence[self.curr_index]
			# it was already done
			else:
				self.setStep(self.getStep() - rem.getTotalSteps())
				self.curr_index -= 1
		return rem
				
