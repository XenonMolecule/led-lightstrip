from pattern import Pattern
from light_control.colors import calcGradient
import math

class PulseGradient(Pattern):
	
    def __init__(self, strip, colorBase, colorPulse, duration):
        super(PulseGradient, self).__init__(strip, colorBase, duration / 20.0)
        self.colorPulse = colorPulse

    def progress(self, i):
        return (math.sin(((math.pi/10) * i) - (math.pi/2)) + 1) * 0.5
	
    def execute(self):
        for j in range(20):
            prog = self.progress(j)
            for i in range(self.strip.numPixels()):
                self.strip.setPixel(i, calcGradient(self.color(0), self.colorPulse(0), prog))
            self.strip.show()
            self.pause()
        for i in range(self.strip.numPixels()):
            self.strip.setPixel(i, self.color(0))
        self.strip.show()
