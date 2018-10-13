import fp
from fp import cfg

class qfp(fp.base):
	"""Generator for LQFP/TQFP/PQFP and other xQFP footprints"""

	def __init__(self, name, model, description, tags, package_width, package_height, pad_width, pad_height, pad_grid, pad_distance_x, pad_distance_y, pad_count_x, pad_count_y):
		super(qfp, self).__init__(name, model, description, tags)

		if pad_count_x % 2 or pad_count_y % 2:
			raise NameError("Pad count is odd!")

		fp.base.add(self, fp.rectangle(cfg.FOOTPRINT_PACKAGE_LAYER, 0, 0, package_width, package_height, cfg.FOOTPRINT_PACKAGE_LINE_WIDTH, True))

		pin = 1
		y = pad_grid * -((float(pad_count_y) / 4) - 0.5)
		x = pad_grid * -((float(pad_count_x) / 4) - 0.5)
		fp.base.add(self, fp.circle(cfg.FOOTPRINT_PACKAGE_LAYER, x, y, x + 0.5, y, cfg.FOOTPRINT_PACKAGE_LINE_WIDTH))
		for i in range(pad_count_y / 2):
			fp.base.add(self, fp.pad(cfg.FOOTPRINT_SMD_LAYERS, pin, fp.technology.smd, fp.type.rect, -pad_distance_x / 2, y, pad_width, pad_height, 0, 90))
			y += pad_grid
			pin += 1

		for i in range(pad_count_x / 2):
			fp.base.add(self, fp.pad(cfg.FOOTPRINT_SMD_LAYERS, pin, fp.technology.smd, fp.type.rect, x, pad_distance_y / 2, pad_width, pad_height, 0, 0))
			x += pad_grid
			pin += 1

		y = pad_grid * ((float(pad_count_y) / 4) - 0.5)
		for i in range(pad_count_y / 2):
			fp.base.add(self, fp.pad(cfg.FOOTPRINT_SMD_LAYERS, pin, fp.technology.smd, fp.type.rect, pad_distance_x / 2, y, pad_width, pad_height, 0, 90))
			y -= pad_grid
			pin += 1

		x = pad_grid * ((float(pad_count_x) / 4) - 0.5)
		for i in range(pad_count_x / 2):
			fp.base.add(self, fp.pad(cfg.FOOTPRINT_SMD_LAYERS, pin, fp.technology.smd, fp.type.rect, x, -pad_distance_y / 2, pad_width, pad_height, 0, 0))
			x -= pad_grid
			pin += 1
