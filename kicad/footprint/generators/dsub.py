import fp
from fp import cfg

class dsub(fp.base):
	"""Generator for dsub connectors (this one will be tricky...)"""

	def __init__(self, name, model, description, tags, package_width, package_height, pad_width, pad_height, pad_grid, pad_distance, count_x, count_y, drill):
		super(dsub, self).__init__(name, model, description, tags)
