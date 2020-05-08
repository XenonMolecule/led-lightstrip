#!/usr/bin/env python3
# LED Lightstrip control code for my Raspberry Pi controlled lightstrip
# Author: Michael Ryan
# 
# This was made possible using the port of the
# Arduino Neopixel library by Tony Dicola

import yaml
import time
from lightstrip import Lightstrip
from colors import *
from patterns.colorwipe import ColorWipe
from patterns.theaterchase import TheaterChase
from patterns.colorslide import ColorSlide
from patterns.timer import Timer
from iterable_patterns.icolorwipe import IColorWipe
from iterable_patterns.itheaterchase import ITheaterChase

cfg = {}

# Load settings
with open("config.yaml", "r") as yamlfile:
	cfg = yaml.safe_load(yamlfile)
	
if __name__ == '__main__':
	# Create NeoPixel object with appropriate configuration
	strip = Lightstrip(cfg)
	sequence = []
	sequence.append(ColorWipe(strip, rainbow_cycle(strip.numPixels()), 20))
	sequence.append(TheaterChase(strip, blue, 50))
	sequence.append(ColorSlide(strip, rainbow_cycle(strip.numPixels()), 5, 5))
	sequence.append(ColorWipe(strip, red, 20))
	sequence.append(Timer(strip, red, 10000))
	
	chase = ITheaterChase(strip, rainbow_cycle(strip.numPixels()))
	
	try:
		while True:
			while not chase.isDone():
				chase.runStep()
				time.sleep(50/1000.0)
			chase.reset()
			strip.clear()
			time.sleep(1)
	except KeyboardInterrupt:
		strip.clear()
