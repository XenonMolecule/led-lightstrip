#!/usr/bin/env python3
# LED Lightstrip control code for my Raspberry Pi controlled lightstrip
# Author: Michael Ryan
# 
# This was made possible using the port of the
# Arduino Neopixel library by Tony Dicola

import time
from neopixel import *
import yaml

cfg = {}

# Load settings
with open("config.yaml", "r") as yamlfile:
	cfg = yaml.safe_load(yamlfile)

# Create alias for Neopixel specific settings
nps = cfg["neopixel"]

if __name__ == '__main__':
	# Create NeoPixel object with appropriate configuration
	strip = Adafruit_NeoPixel(nps['led-count'], nps['led-pin'], \
		nps['led-freq-hz'], nps['led-dma'], nps['led-invert'], \
		nps['led-brightness'], nps['led-channel'])
	
	# Initialize the library
	strip.begin()
	
	try:
		while True:
			for i in range(strip.numPixels()):
				strip.setPixelColor(i, Color(255,0,0))
				strip.show()
				time.sleep(20/1000.0)
			for i in range(strip.numPixels()):
				strip.setPixelColor(i, Color(0,0,0))
				strip.show()
				time.sleep(20/1000.0)
	except KeyboardInterrupt:
		for i in range(strip.numPixels()):
			strip.setPixelColor(i, Color(0,0,0))
		strip.show()
