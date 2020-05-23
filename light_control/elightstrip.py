from light_control.colors import Color
from tkinter import *

class EmulatedLightstrip(object):
    def __init__(self, cfg, estrip):
        self.led_count = cfg['neopixel']['led-count']
        self.reversed = cfg['custom']['reversed']
        self.brightness = cfg['neopixel']['led-brightness']
        self.color_cache = [0] * self.led_count
        self.estrip = estrip

    def show(self):
        for i in range(len(self.color_cache)):
            self.estrip[i] = self.color_cache[i]

    # Sets the pixel without updating the strip
	#  Allows reversal of direction of the strip
	#  Ensures bounded pixel index from [0, numPixels)
    def setPixel(self, n, color):
        pixelNum = self.numPixels() - 1 - n if self.reversed else n
        pixelNum %= self.numPixels()
        self.color_cache[pixelNum] = color

    # Sets the pixel and immediately updates the lightstrip visually
    def setPixelUpdate(self, n, color):
        self.setPixel(n, color)
        self.show()

    def setBrightness(self, n):
        self.brightness = n

    def getBrightness(self):
        return self.brightness

    def setReversed(self, rev):
        self.reversed = rev

    def getReversed(self):
        return self.reversed

    def numPixels(self):
        return self.led_count

    # The only animation I am baking into the lightstrip class because
	#  it has pretty universal importance among other animations and
	#  the runner class too
    def clear(self):
        for i in range(self.numPixels()):
            self.setPixel(i, Color(0,0,0))
        self.show()

    def clearPixel(self, n):
        self.setPixel(n, Color(0, 0, 0))
