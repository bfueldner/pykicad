import kicad.footprint.generator

class bga(kicad.footprint.generator.base):
	'''Generator for ball grid array footprints'''

	def __init__(self, name, model, description, tags, package_width, package_height, pad_diameter, pad_grid, pad_distance, count_x, count_y):
		super().__init__(kicad.footprint.type.footprint.smd, name, model, description, tags)
