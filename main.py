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

cfg = {}

# Load settings
with open("config.yaml", "r") as yamlfile:
	cfg = yaml.safe_load(yamlfile)
	
if __name__ == '__main__':
	# Create NeoPixel object with appropriate configuration
	strip = Lightstrip(cfg)
	red_wipe = ColorWipe(strip, red, 20)
	clr_wipe = ColorWipe(strip, clear, 20)
	
	try:
		while True:
			red_wipe.execute()
			clr_wipe.execute()
	except KeyboardInterrupt:
		strip.clear()
