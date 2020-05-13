#!/usr/bin/env python3
# LED Lightstrip control code for my Raspberry Pi controlled lightstrip
# Author: Michael Ryan
#
# This was made possible using the port of the
# Arduino Neopixel library by Tony Dicola

import yaml
import time
import multiprocessing
#from lightstrip import Lightstrip
from elightstrip import EmulatedLightstrip
from colors import *
from onlineconn import OnlineConn
from iterable_patterns.icolorslide import IColorSlide

def run_lights(settings, read_lock, estrip):
	cfg = {}

	# Load settings
	with open("config.yaml", "r") as yamlfile:
		cfg = yaml.safe_load(yamlfile)

	# Create NeoPixel object with appropriate configuration
	strip = None
	if cfg['custom']['emulator']:
		strip = EmulatedLightstrip(cfg, estrip)
	else:
		strip = Lightstrip(cfg)

	conn = OnlineConn(settings, read_lock)

	slide = IColorSlide(strip, rainbow_cycle(strip.numPixels()))

	try:
		while True:
			while not slide.isDone():
				slide.runStep()
				slide.pause()
			slide.reset()
	except KeyboardInterrupt:
		strip.clear()

if __name__ == '__main__':
	settings = multiprocessing.Manager().Namespace()
	settings.red = 0
	settings.green = 0
	settings.blue = 255
	run_lights(settings, multiprocessing.Lock(), None)
