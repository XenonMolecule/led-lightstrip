import multiprocessing
from light_control.main import run_lights
from app.api.api import run_server

from multiprocessing import Process
from multiprocessing.sharedctypes import Value, Array
from ctypes import Structure, c_int, c_wchar, c_bool

# TODO: stop being lazy and just read the config file here too
EMULATOR = False

if EMULATOR:
	import tkinter as tk
	from tkinter import *



def hex_from_int(color):
	red = 0b11111111 & (color >> 8)
	green = 0b11111111 & (color >> 16)
	blue = 0b11111111 & color
	redstr = hex(red)[2:] if red >=16 else "0" + hex(red)[2:]
	greenstr = hex(green)[2:] if green >=16 else "0" + hex(green)[2:]
	bluestr = hex(blue)[2:] if blue >=16 else "0" + hex(blue)[2:]
	return "#" + redstr + greenstr + bluestr

class Settings(Structure):
	_fields_ = [
		('back_red', c_int),
		('back_green', c_int),
		('back_blue', c_int),
		('fore_red', c_int),
		('fore_green', c_int),
		('fore_blue', c_int),
		('queue_patt', c_wchar * 10), # Can't be longer than 10 characters
		('hold_patt', c_bool)
	]

if __name__ == "__main__":
	settings = Value(Settings, 0, 0, 0, 0, 0, 0, 'base', False)
	read_lock = multiprocessing.Lock()

	emulator_colors = None
	if EMULATOR:
		window = tk.Tk()
		canvas = Canvas(window, width=1600, height=100, bg='black')
		pixels = [None] * 150

		x = 53
		for i in range(150):
			pixels[i] = canvas.create_rectangle(x, 48, x + 5, 53, fill="white")
			x += 10
		emulator_colors = Array(c_int, [0] * 150)

		def update_pixels():
			for i, pixel in enumerate(pixels):
				canvas.itemconfig(pixel, fill=hex_from_int(emulator_colors[i]))
			canvas.after(10, update_pixels)

		update_pixels()

	server = Process(target=run_server, args=(settings, read_lock))
	lights = Process(target=run_lights, args=(settings, read_lock, emulator_colors))

	server.start()
	lights.start()

	if EMULATOR:
		canvas.pack()
		window.mainloop()

	server.join()
	lights.join()
