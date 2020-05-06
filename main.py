#!/usr/bin/env python3
# LED Lightstrip control code for my Raspberry Pi controlled lightstrip
# Author: Michael Ryan
# 
# This was made possible using the port of the
# Arduino Neopixel library by Tony Dicola

import time
from lightstrip import *
from patterns.colorwipe import ColorWipe
import yaml

cfg = {}

def red(n):
	return Color(255, 0, 0)
	
def clr(n):
	return Color(0,0,0)

# Load settings
with open("config.yaml", "r") as yamlfile:
	cfg = yaml.safe_load(yamlfile)
	
if __name__ == '__main__':
	# Create NeoPixel object with appropriate configuration
	strip = Lightstrip(cfg)
	red_wipe = ColorWipe(strip, red, 20)
	clr_wipe = ColorWipe(strip, clr, 20)
	
	try:
		while True:
			red_wipe.execute()
			clr_wipe.execute()
	except KeyboardInterrupt:
		strip.clear()
