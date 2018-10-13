import fp
from fp import cfg

class bga(fp.base):
	"""Generator for ball grid array footprints"""

	def __init__(self, name, model, description, tags, package_width, package_height, pad_diameter, pad_grid, pad_distance, count_x, count_y):
		super(bga, self).__init__(name, model, description, tags)
