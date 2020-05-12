#!/usr/bin/env python3
# LED Lightstrip control code for my Raspberry Pi controlled lightstrip
# Author: Michael Ryan
# 
# This was made possible using the port of the
# Arduino Neopixel library by Tony Dicola

import yaml
import time
import multiprocessing
from lightstrip import Lightstrip
from colors import *
from onlineconn import OnlineConn
from iterable_patterns.icolorslide import IColorSlide
	
def run_lights(settings, read_lock):
	cfg = {}

	# Load settings
	with open("../config.yaml", "r") as yamlfile:
		cfg = yaml.safe_load(yamlfile)
	
	# Create NeoPixel object with appropriate configuration
	strip = Lightstrip(cfg)
	
	conn = OnlineConn(settings, read_lock)
	
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

if __name__ == '__main__':
	settings = multiprocessing.Manager().Namespace()
	settings.red = 0
	settings.green = 0
	settings.blue = 255
	run_lights(settings, multiprocessing.Lock())
