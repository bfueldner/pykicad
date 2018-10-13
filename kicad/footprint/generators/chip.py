import fp
from fp import cfg

class chip(fp.base):
	"""Generator for chip resistors, capacitors, inductors, MELF and Tantal devices"""

	def __init__(self, name, model, description, tags, package_width, package_height, pad_width, pad_height, pad_distance):
		super(chip, self).__init__(name, model, description, tags, True, False)

		self.package_width = package_width
		self.package_height = package_height
		self.pad_width = pad_width
		self.pad_height = pad_height

		fp.base.add(self, fp.text(cfg.FOOTPRINT_REFERENCE_LAYER, "reference", "REF**", 0, -package_height / 2 - cfg.FOOTPRINT_REFERENCE_FONT_SIZE, 0, cfg.FOOTPRINT_REFERENCE_FONT_SIZE, cfg.FOOTPRINT_REFERENCE_FONT_THICKNESS))
		fp.base.add(self, fp.text(cfg.FOOTPRINT_VALUE_LAYER, "value", "VAL**", 0, 0, 0, cfg.FOOTPRINT_VALUE_FONT_SIZE, cfg.FOOTPRINT_VALUE_FONT_THICKNESS))

		fp.base.add(self, fp.rectangle(cfg.FOOTPRINT_PACKAGE_LAYER, 0, 0, package_width, package_height, cfg.FOOTPRINT_PACKAGE_LINE_WIDTH, True))
		fp.base.add(self, fp.pad(cfg.FOOTPRINT_SMD_LAYERS, 1, fp.technology.smd, fp.type.rect, -pad_distance / 2, 0, pad_width, pad_height))
		fp.base.add(self, fp.pad(cfg.FOOTPRINT_SMD_LAYERS, 2, fp.technology.smd, fp.type.rect, +pad_distance / 2, 0, pad_width, pad_height))

class chip_pol(chip):
	"""Generator for chip devices with polarity marker"""

	def __init__(self, name, description, tags, package_width, package_height, pad_width, pad_height, pad_distance):
		super(chip_pol, self).__init__(name, description, tags, package_width, package_height, pad_width, pad_height, pad_distance)

		line_x = package_width / 2 + package_widht * 0.1
		line_y = package_height / 2
		fp.base.add(self, fp.line(cfg.FOOTPRINT_PACKAGE_LAYER, -line_x, -line_y, -line_x, line_y, cfg.FOOTPRINT_PACKAGE_LINE_WIDTH))
