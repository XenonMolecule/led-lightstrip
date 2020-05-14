import yaml
import time
from lightstrip import Lightstrip

if __name__ == "__main__":
	cfg = {}

	# Load settings
	with open("config.yaml", "r") as yamlfile:
		cfg = yaml.safe_load(yamlfile)

	# Create NeoPixel object with appropriate configuration
	strip = Lightstrip(cfg)
	
	strip.clear()
