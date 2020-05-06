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
