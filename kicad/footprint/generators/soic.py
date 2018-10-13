import kicad.footprint.generator

class soic(kicad.footprint.generator.base):
    '''Generator for small outline ICs'''

    def __init__(self, name, model, description, tags, package_width, package_height, pad_width, pad_height, pad_grid, pad_distance, pad_count):
        super().__init__(kicad.footprint.type.technology.smd, name, model, description, tags)

        if pad_count % 2:
            raise ValueError("pad_count is odd")

        # Reference text
        super().add(
            kicad.footprint.element.text(
                kicad.footprint.layer.silkscreen_top,
                "reference",
                "REF**",
                -package_width / 2 - kicad.config.footprint.REFERENCE_FONT_SIZE,
                0,
                90,
                kicad.config.footprint.REFERENCE_FONT_SIZE,
                kicad.config.footprint.REFERENCE_FONT_THICKNESS
            )
        )

        # Value text
        super().add(
            kicad.footprint.element.text(
                kicad.footprint.layer.fabrication_top,
                "value",
                "VAL**",
                0,
                0,
                0,
                kicad.config.footprint.VALUE_FONT_SIZE,
                kicad.config.footprint.VALUE_FONT_THICKNESS
            )
        )

        pin = 1
        x = pad_grid * -((float(pad_count) / 4.0) - 0.5)
        line_x = package_width / 2.0
        line_y = package_height / 2.0 - 0.5

        x = '''
        super().add(
            kicad.footprint.element.rectangle(
                kicad.footprint.layer.silkscreen_top,
                0, 0, package_width, package_height,
                cfg.FOOTPRINT_PACKAGE_LINE_WIDTH,
                True
            )
        )

        super().add(
            kicad.footprint.element.line(
                cfg.FOOTPRINT_PACKAGE_LAYER, -line_x, line_y, line_x, line_y, cfg.FOOTPRINT_PACKAGE_LINE_WIDTH
            )
        )

        diff = -line_x - x
        line_y += diff
        fp.base.add(self, fp.circle(cfg.FOOTPRINT_PACKAGE_LAYER, x, line_y, x - 0.3, line_y, cfg.FOOTPRINT_PACKAGE_LINE_WIDTH))
        for i in range(pad_count / 2):
            fp.base.add(self, fp.pad(cfg.FOOTPRINT_SMD_LAYERS, pin, fp.technology.smd, fp.type.rect, x, pad_distance / 2, pad_width, pad_height))
            x += pad_grid
            pin += 1

        for i in range(pad_count / 2, pad_count):
            x -= pad_grid
            fp.base.add(self, fp.pad(cfg.FOOTPRINT_SMD_LAYERS, pin, fp.technology.smd, fp.type.rect, x, -pad_distance / 2, pad_width, pad_height))
            pin += 1'''
