#!/usr/bin/env python3
# LED Lightstrip control code for my Raspberry Pi controlled lightstrip
# Author: Michael Ryan
# 
# This was made possible using the port of the
# Arduino Neopixel library by Tony Dicola

import time
from lightstrip import *
import yaml

cfg = {}

# Load settings
with open("config.yaml", "r") as yamlfile:
	cfg = yaml.safe_load(yamlfile)
	
if __name__ == '__main__':
	# Create NeoPixel object with appropriate configuration
	strip = Lightstrip(cfg)
	
	try:
		while True:
			for i in range(strip.numPixels()):
				strip.setPixelUpdate(i, Color(255,0,0))
				time.sleep(20/1000.0)
			for i in range(strip.numPixels()):
				strip.setPixelUpdate(i, Color(0,0,0))
				time.sleep(20/1000.0)
	except KeyboardInterrupt:
		strip.clear()
