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

def control_lights(onlineSettings, onlineLock, soloThreadLock):
	print(soloThreadLock.locked())
	if(soloThreadLock.locked()):
		return
	else:
		soloThreadLock.acquire()
	
	cfg = {}

	# Load settings
	with open("../../config.yaml", "r") as yamlfile:
		cfg = yaml.safe_load(yamlfile)
	
	# Create NeoPixel object with appropriate configuration
	strip = Lightstrip(cfg)
	
	conn = OnlineConn(onlineSettings, onlineLock)
	
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
	defaultSettings = {
		'red': 255,
		'green': 0,
		'blue': 0
	}
	control_lights(defaultSettings, Lock(), Lock())
