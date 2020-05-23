#!/usr/bin/env python3
# LED Lightstrip control code for my Raspberry Pi controlled lightstrip
# Author: Michael Ryan
#
# This was made possible using the port of the
# Arduino Neopixel library by Tony Dicola

import yaml
import time
import multiprocessing
from light_control.lightstrip import Lightstrip
# from light_control.elightstrip import EmulatedLightstrip
from light_control.colors import *
from light_control.onlineconn import OnlineConn
from light_control.iterable_patterns.isparkle import ISparkle

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

	# slide = IColorSlide(strip, online(conn))

	# Birthday Cake Mode (Funfetti)
	isparkle = ISparkle(strip, color(255, 255, 255), rainbow_cycle(strip.numPixels()), 20, True)

	try:
		while True:
			while not isparkle.isDone():
				isparkle.runStep()
				isparkle.pause()
			isparkle.reset()
	except KeyboardInterrupt:
		strip.clear()

if __name__ == '__main__':
	settings = multiprocessing.Manager().Namespace()
	settings.red = 0
	settings.green = 0
	settings.blue = 255
	run_lights(settings, multiprocessing.Lock(), None)
