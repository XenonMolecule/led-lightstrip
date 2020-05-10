# Converts RGB to GRB which is needed by the lightstrip
def Color(red, green, blue, white = 0):
	"""Convert the provided red, green, blue color to a 24-bit color value.
	Each color component should be a value 0-255 where 0 is the lowest intensity
	and 255 is the highest intensity.
	"""
	return (white << 24) | (green << 16)| (red << 8) | blue
	
def red(n):
	return Color(255, 0, 0)
	
def green(n):
	return Color(0, 255, 0)
	
def blue(n):
	return Color(0, 0, 255)
	
def clear(n):
	return Color(0, 0, 0)

def rainbow(n):
	n = n & 255
	n = 255 - n
	if n < 85:
		return Color(255 - n * 3, 0, n * 3)
		
	elif n < 170:
		n -= 85
		return Color(0, n * 3, 255 - n * 3)
	else:
		n -= 170
		return Color(n * 3, 255 - n * 3, 0)
		

def rainbow_cycle(length):
	def rainbowCycleFunc(n):
			return rainbow(n * 256 // length)
	return rainbowCycleFunc

def online(connection):
	def onlineSetColor(n):
		color = connection.getColor()
		return Color(color['red'], color['green'], color['blue'])
	return onlineSetColor
