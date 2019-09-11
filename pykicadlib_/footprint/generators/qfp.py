import pykicadlib.footprint.generator

class qfp(pykicadlib.footprint.generator.base):
    '''Generator for LQFP/TQFP/PQFP and other xQFP footprints'''

    def __init__(self, name, model, description, tags, package_width, package_height, pad_width, pad_height, pad_grid, pad_distance_x, pad_distance_y, pad_count_x, pad_count_y):
        super().__init__(pykicadlib.footprint.type.footprint.smd, name, model, description, tags)

        if pad_count_x % 2 or pad_count_y % 2:
            raise ValueError("Pad count is odd!")

        # Reference text
        super().add(
            pykicadlib.footprint.element.text(
                pykicadlib.footprint.layer.silkscreen_top,
                pykicadlib.footprint.type.text.reference,
                None,
                0.0, 0.0,
                pykicadlib.config.footprint.REFERENCE_FONT_SIZE,
                pykicadlib.config.footprint.REFERENCE_FONT_THICKNESS
            )
        )

        # Value text
        super().add(
            pykicadlib.footprint.element.text(
                pykicadlib.footprint.layer.fabrication_top,
                pykicadlib.footprint.type.text.value,
                None,
                0.0, pykicadlib.config.footprint.VALUE_FONT_SIZE + 2 * pykicadlib.config.footprint.VALUE_FONT_THICKNESS,
                pykicadlib.config.footprint.VALUE_FONT_SIZE,
                pykicadlib.config.footprint.VALUE_FONT_THICKNESS
            )
        )

        # Case
        super().add(
            pykicadlib.footprint.element.centered_rectangle(
                pykicadlib.footprint.layer.silkscreen_top,
                0.0, 0.0, package_width, package_height,
                pykicadlib.config.footprint.PACKAGE_LINE_WIDTH
            )
        )

        pin = 1
        y = pad_grid * -((float(pad_count_y) / 4) - 0.5)
        x = pad_grid * -((float(pad_count_x) / 4) - 0.5)

        # Marker
        super().add(
            pykicadlib.footprint.element.circle(
                pykicadlib.footprint.layer.silkscreen_top,
                x, y, x + 0.5, y,
                pykicadlib.config.footprint.PACKAGE_LINE_WIDTH
            )
        )

        for i in range(pad_count_y // 2):
            super().add(
                pykicadlib.footprint.element.pad(
                    pykicadlib.footprint.layers.smd,
                    str(pin),
                    pykicadlib.footprint.type.technology.smd,
                    pykicadlib.footprint.type.shape.rectangle,
                    -pad_distance_x / 2, y, pad_width, pad_height,
                    None,
                    90.0
                )
            )
            y += pad_grid
            pin += 1

        for i in range(pad_count_x // 2):
            super().add(
                pykicadlib.footprint.element.pad(
                    pykicadlib.footprint.layers.smd,
                    str(pin),
                    pykicadlib.footprint.type.technology.smd,
                    pykicadlib.footprint.type.shape.rectangle,
                    x, pad_distance_y / 2, pad_width, pad_height,
                    None,
                    0.0
                )
            )
            x += pad_grid
            pin += 1

        y = pad_grid * ((float(pad_count_y) / 4) - 0.5)
        for i in range(pad_count_y // 2):
            super().add(
                pykicadlib.footprint.element.pad(
                    pykicadlib.footprint.layers.smd,
                    str(pin),
                    pykicadlib.footprint.type.technology.smd,
                    pykicadlib.footprint.type.shape.rectangle,
                    pad_distance_x / 2, y, pad_width, pad_height,
                    None,
                    90.0
                )
            )
            y -= pad_grid
            pin += 1

        x = pad_grid * ((float(pad_count_x) / 4) - 0.5)
        for i in range(pad_count_x // 2):
            super().add(
                pykicadlib.footprint.element.pad(
                    pykicadlib.footprint.layers.smd,
                    str(pin),
                    pykicadlib.footprint.type.technology.smd,
                    pykicadlib.footprint.type.shape.rectangle,
                    x, -pad_distance_y / 2, pad_width, pad_height,
                    None,
                    0.0
                )
            )
            x -= pad_grid
            pin += 1
