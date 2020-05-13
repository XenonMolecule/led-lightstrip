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
from iterable_patterns.icolorwipe import IColorWipe
from iterable_patterns.imacro import IMacro
from iterable_patterns.iloop import ILoop
from patterns.colorwipe import ColorWipe
from patterns.macro import Macro
from patterns.loop import Loop
	
def run_lights(settings, read_lock):
	cfg = {}

	# Load settings
	with open("config.yaml", "r") as yamlfile:
		cfg = yaml.safe_load(yamlfile)
	
	# Create NeoPixel object with appropriate configuration
	strip = Lightstrip(cfg)
	
	conn = OnlineConn(settings, read_lock)
	
	slide = IColorSlide(strip, rainbow_cycle(strip.numPixels()))
	rwipe = IColorWipe(strip, red)
	bwipe = IColorWipe(strip, blue)
	iloop = ILoop(rwipe, 2)
	imacro = IMacro(slide, iloop, bwipe)
	
	redwipe = ColorWipe(strip, red, 20)
	bluewipe = ColorWipe(strip, blue, 20)
	macro = Macro(redwipe, bluewipe)
	loop = Loop(macro, 3)
	
	try:
		while True:
			while not imacro.isDone():
				imacro.runStep()
				imacro.pause()
			imacro.reset()
	except KeyboardInterrupt:
		strip.clear()

if __name__ == '__main__':
	settings = multiprocessing.Manager().Namespace()
	settings.red = 0
	settings.green = 0
	settings.blue = 255
	run_lights(settings, multiprocessing.Lock())
