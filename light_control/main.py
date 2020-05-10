#!/usr/bin/env python3
# LED Lightstrip control code for my Raspberry Pi controlled lightstrip
# Author: Michael Ryan
# 
# This was made possible using the port of the
# Arduino Neopixel library by Tony Dicola

import yaml
import time
from threading import Lock
from lightstrip import Lightstrip
from colors import *
from onlineconn import OnlineConn
from iterable_patterns.icolorslide import IColorSlide

cfg = {}

# Load settings
with open("../config.yaml", "r") as yamlfile:
	cfg = yaml.safe_load(yamlfile)
	
if __name__ == '__main__':
	
	# Create NeoPixel object with appropriate configuration
	strip = Lightstrip(cfg)
	
	conn = OnlineConn()
	
	slide = IColorSlide(strip, online(conn))
	
	try:
		while True:
			while not slide.isDone():
				slide.runStep()
				time.sleep(20/1000.0)
			slide.reset()
			strip.clear()
			time.sleep(1)
	except KeyboardInterrupt:
		strip.clear()
