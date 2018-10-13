import fp
from fp import cfg

class connector_grid_male(fp.base):
	"""Generator wired connector lines (pins)"""

	def __init__(self, name, model, description, tags, package_width, package_height, pad_diameter, pad_grid, pad_drill, pin_count_x, pin_count_y):
		super(connector_grid_male, self).__init__(name, model, description, tags, False, False)

		bevel = pad_grid * 0.2
		fp.base.add(self, fp.text(cfg.FOOTPRINT_REFERENCE_LAYER, "reference", "REF**", 0, -(package_height + cfg.FOOTPRINT_REFERENCE_FONT_SIZE) / 2 - 2 * cfg.FOOTPRINT_REFERENCE_FONT_THICKNESS, cfg.FOOTPRINT_REFERENCE_FONT_SIZE, cfg.FOOTPRINT_REFERENCE_FONT_THICKNESS))
		fp.base.add(self, fp.text(cfg.FOOTPRINT_VALUE_LAYER, "value", "VAL**", 0, (package_height + cfg.FOOTPRINT_VALUE_FONT_SIZE) / 2 + 2 * cfg.FOOTPRINT_VALUE_FONT_THICKNESS, cfg.FOOTPRINT_VALUE_FONT_SIZE, cfg.FOOTPRINT_VALUE_FONT_THICKNESS))
		fp.base.add(self, fp.beveled_outline(cfg.FOOTPRINT_PACKAGE_LAYER, 0, 0, package_width, package_height, bevel, pad_grid, cfg.FOOTPRINT_PACKAGE_LINE_WIDTH, True))

		pin = 1
		y = pad_grid * -((float(pin_count_y) / 2) - 0.5)
		for i in range(pin_count_y):
			x = pad_grid * -((float(pin_count_x) / 2) - 0.5)
			for j in range(pin_count_x):
				if pin == 1:
					fp.base.add(self, fp.pad(cfg.FOOTPRINT_THD_LAYERS, pin, fp.technology.thru_hole, fp.type.rect, x, y, pad_diameter, pad_diameter, pad_drill))
				else:
					fp.base.add(self, fp.pad(cfg.FOOTPRINT_THD_LAYERS, pin, fp.technology.thru_hole, fp.type.circle, x, y, pad_diameter, pad_diameter, pad_drill))

				pin += 1
				x += pad_grid
			y += pad_grid

class connector_grid_female(fp.base):
	"""Generator wired connector lines (plugs)"""

	def __init__(self, name, description, tags, package_width, package_height, pad_diameter, pad_grid, pad_drill, pin_count_x, pin_count_y):
		super(connector_grid_female, self).__init__(name, description, tags, False, False)

		bevel = pad_grid * 0.2
		fp.base.add(self, fp.text(cfg.FOOTPRINT_REFERENCE_LAYER, "reference", "REF**", 0, -(package_height + cfg.FOOTPRINT_REFERENCE_FONT_SIZE) / 2 - 2 * cfg.FOOTPRINT_REFERENCE_FONT_THICKNESS, cfg.FOOTPRINT_REFERENCE_FONT_SIZE, cfg.FOOTPRINT_REFERENCE_FONT_THICKNESS))
		fp.base.add(self, fp.text(cfg.FOOTPRINT_VALUE_LAYER, "value", "VAL**", 0, (package_height + cfg.FOOTPRINT_VALUE_FONT_SIZE) / 2 + 2 * cfg.FOOTPRINT_VALUE_FONT_THICKNESS, cfg.FOOTPRINT_VALUE_FONT_SIZE, cfg.FOOTPRINT_VALUE_FONT_THICKNESS))
		fp.base.add(self, fp.beveled_outline(cfg.FOOTPRINT_PACKAGE_LAYER, 0, 0, package_width, package_height, bevel, pad_grid, cfg.FOOTPRINT_PACKAGE_LINE_WIDTH, True))

		pin = 1
		y = pad_grid * -((float(pin_count_y) / 2) - 0.5)
		for i in range(pin_count_y):
			x = pad_grid * ((float(pin_count_x) / 2) - 0.5)
			for j in range(pin_count_x):
				if pin == 1:
					fp.base.add(self, fp.pad(cfg.FOOTPRINT_THD_LAYERS, pin, fp.technology.thru_hole, fp.type.rect, x, y, pad_diameter, pad_diameter, pad_drill))
				else:
					fp.base.add(self, fp.pad(cfg.FOOTPRINT_THD_LAYERS, pin, fp.technology.thru_hole, fp.type.circle, x, y, pad_diameter, pad_diameter, pad_drill))

				pin += 1
				x -= pad_grid
			y += pad_grid
