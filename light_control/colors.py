# Converts RGB to GRB which is needed by the lightstrip
def Color(red, green, blue, white = 0):
	"""Convert the provided red, green, blue color to a 24-bit color value.
	Each color component should be a value 0-255 where 0 is the lowest intensity
	and 255 is the highest intensity.
	"""
	return (white << 24) | (green << 16)| (red << 8) | blue
	
def getRGB(color):
	r = 0b11111111 & (color >> 8)
	g = 0b11111111 & (color >> 16)
	b = 0b11111111 & color
	return r, g, b

def calcGradient(color1, color2, progress = 0.5):
	r1, g1, b1 = getRGB(color1)
	r2, g2, b2 = getRGB(color2)
	dr = (r2 - r1)
	dg = (g2 - g1)
	db = (b2 - b1)
	return Color(r1 + int(round(dr * progress)), g1 + int(round(dg * progress)), b1 + int(round(db * progress)))
	
def red(n):
	return Color(255, 0, 0)
	
def green(n):
	return Color(0, 255, 0)
	
def blue(n):
	return Color(0, 0, 255)
	
def clear(n):
	return Color(0, 0, 0)
	
def color(r, g, b):
	def colorFunc(n):
		return Color(r, g, b)
	return colorFunc
	
def gradient(r1, g1, b1, r2, g2, b2):
	dr = (r2 - r1) / 128.0
	dg = (g2 - g1) / 128.0
	db = (b2 - b1) / 128.0
	def gradientFunc(n):
		n += 128
		n = n & 255
		n = abs(128 - n)
		return Color(r1 + int(round(dr * n)), g1 + int(round(dg * n)), b1 + int(round(db * n)))
	return gradientFunc
	
def gradient_cycle(r1, g1, b1, r2, g2, b2, length):
	default_gradient = gradient(r1, g1, b1, r2, g2, b2)
	def gradCycleFunc(n):
		return default_gradient(n * 256 // length)
	return gradCycleFunc

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

def online_background(connection):
	def onlineSetColor(n):
		color = connection.getBackgroundColor()
		return Color(color['red'], color['green'], color['blue'])
	return onlineSetColor

def online_foreground(connection):
	def onlineSetColor(n):
		color = connection.getForegroundColor()
		return Color(color['red'], color['green'], color['blue'])
	return onlineSetColor