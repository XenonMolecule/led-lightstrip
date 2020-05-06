#!/usr/bin/env python3
# LED Lightstrip control code for my Raspberry Pi controlled lightstrip
# Author: Michael Ryan
# 
# This was made possible using the port of the
# Arduino Neopixel library by Tony Dicola

import yaml
from lightstrip import Lightstrip
from colors import *
from patterns.colorwipe import ColorWipe
from patterns.theaterchase import TheaterChase

cfg = {}

# Load settings
with open("config.yaml", "r") as yamlfile:
	cfg = yaml.safe_load(yamlfile)
	
if __name__ == '__main__':
	# Create NeoPixel object with appropriate configuration
	strip = Lightstrip(cfg)
	sequence = []
	sequence.append(ColorWipe(strip, red, 20))
	sequence.append(TheaterChase(strip, red, 50))
	sequence.append(TheaterChase(strip, green, 50))
	sequence.append(TheaterChase(strip, blue, 50))
	
	try:
		while True:
			for pattern in sequence:
				pattern.execute()
	except KeyboardInterrupt:
		strip.clear()
