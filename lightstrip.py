from neopixel import Adafruit_NeoPixel
from colors import Color

# Creates an "interface" (not using programming definition) between
# my code and the neopixel library to set each of the pixels
# 
# This creates a level of abstraction that will let my change how I
# set each pixel in the future should the need for change arise
class Lightstrip(object):
	def __init__(self, cfg):
		nps = cfg['neopixel']
		self.strip = Adafruit_NeoPixel(nps['led-count'], \
			nps['led-pin'], nps['led-freq-hz'], nps['led-dma'], \
			nps['led-invert'], nps['led-brightness'], nps['led-channel'])
		
		self.reversed = cfg['custom']['reversed']
		
		self.strip.begin()
	
	def _cleanup(self):
		self.strip._cleanup()
		
	def show(self):
		self.strip.show()
		
	# Sets the pixel without updating the strip
	#  Allows reversal of direction of the strip
	#  Ensures bounded pixel index from [0, numPixels)
	def setPixel(self, n, color):
		pixelNum = self.strip.numPixels() - 1 - n if self.reversed else n
		pixelNum %= self.strip.numPixels()
		self.strip.setPixelColor(pixelNum, color)
	
	# Sets the pixel and immediately updates the lightstrip visually
	def setPixelUpdate(self, n, color):
		self.setPixel(n, color)
		self.show()
		
	def setBrightness(self, n):
		self.strip.setBrightness(n)
		
	def getBrightness(self):
		self.strip.getBrightness()
		
	def setReversed(self, rev):
		self.reversed = rev
		
	def getReversed(self):
		return self.reversed
		
	def numPixels(self):
		return self.strip.numPixels()
		
	# The only animation I am baking into the lightstrip class because
	#  it has pretty universal importance among other animations and
	#  the runner class too
	def clear(self):
		for i in range(self.strip.numPixels()):
			self.setPixel(i, Color(0,0,0))
		self.show()
