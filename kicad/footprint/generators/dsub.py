import kicad.footprint.generator

class dsub(kicad.footprint.generator.base):
	'''Generator for dsub connectors (this one will be tricky...)'''

	def __init__(self, name, model, description, tags, package_width, package_height, pad_width, pad_height, pad_grid, pad_distance, count_x, count_y, drill):
		super().__init__(kicad.footprint.type.footprint.thd, name, model, description, tags)
