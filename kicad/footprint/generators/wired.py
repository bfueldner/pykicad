import fp
from fp import cfg

class wired(fp.base):
	"""Generator for wired resistors, capacitors, ..."""

	def __init__(self, name, model, description, tags, package_width, package_height, pad_width, pad_height, pad_grid, pad_distance, count, drill):
		super(wired, self).__init__(name, model, description, tags)

class wired_resistor(fp.base):
	"""Wired resistor with beveled edges"""

	def __init__(self, name, description, tags, package_width, package_height, pad_diameter, pad_distance, pad_drill):
		super(wired_resistor, self).__init__(name, description, tags)

		bevel = math.sqrt(package_width * package_width + package_height * package_height) * 0.1
		fp.base.add(self, fp.beveled_rectangle(cfg.FOOTPRINT_PACKAGE_LAYER, 0, 0, package_width, package_height, bevel, cfg.FOOTPRINT_PACKAGE_LINE_WIDTH, True))
		fp.base.add(self, fp.pad(cfg.FOOTPRINT_THD_LAYERS, 1, fp.technology.thru_hole, fp.type.circle, -pad_distance / 2, 0, pad_diameter, pad_diameter, pad_drill))
		fp.base.add(self, fp.pad(cfg.FOOTPRINT_THD_LAYERS, 2, fp.technology.thru_hole, fp.type.circle, pad_distance / 2, 0, pad_diameter, pad_diameter, pad_drill))
