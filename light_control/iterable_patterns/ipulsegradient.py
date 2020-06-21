from light_control.iterable_patterns.iterable_pattern import IterablePattern
from light_control.colors import calcGradient
import math

class IPulseGradient(IterablePattern):
	
    def __init__(self, strip, colorBase, colorPulse, duration):
        super(IPulseGradient, self).__init__(strip, colorBase, 20, duration/20.0)
        self.colorPulse = colorPulse
		
    def calc_progress(self, i):
        return (math.sin(((math.pi/10) * i) - (math.pi/2)) + 1) * 0.5
	
    def runStep(self):
        j = (self.step % self.totalSteps) + 1
        prog = (self.calc_progress(j))
        for i in range(self.strip.numPixels()):
            self.strip.setPixel(i, calcGradient(self.color(0), self.colorPulse(0), prog))
        self.strip.show()
        self.incrementStep()
