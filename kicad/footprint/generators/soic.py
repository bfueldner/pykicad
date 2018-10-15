import kicad.footprint.generator

class soic(kicad.footprint.generator.base):
    '''Generator for small outline ICs'''

    def __init__(self, name, model, description, tags, package_width, package_height, pad_width, pad_height, pad_grid, pad_distance, pad_count):
        super().__init__(kicad.footprint.type.footprint.smd, name, model, description, tags)

        if pad_count % 2:
            raise ValueError("pad_count is odd")

        # Reference text
        super().add(
            kicad.footprint.element.text(
                kicad.footprint.layer.silkscreen_top,
                kicad.footprint.type.text.reference,
                None,
                -package_width / 2 - kicad.config.footprint.REFERENCE_FONT_SIZE,
                0.0,
                kicad.config.footprint.REFERENCE_FONT_SIZE,
                kicad.config.footprint.REFERENCE_FONT_THICKNESS,
                90.0,
            )
        )

        # Value text
        super().add(
            kicad.footprint.element.text(
                kicad.footprint.layer.fabrication_top,
                kicad.footprint.type.text.value,
                None,
                0.0,
                0.0,
                kicad.config.footprint.VALUE_FONT_SIZE,
                kicad.config.footprint.VALUE_FONT_THICKNESS
            )
        )

        pin = 1
        x = pad_grid * -((pad_count / 4.0) - 0.5)
        line_x = package_width / 2.0
        line_y = package_height / 2.0 - 0.5

        # Case
        super().add(
            kicad.footprint.element.centered_rectangle(
                kicad.footprint.layer.silkscreen_top,
                0, 0, package_width, package_height,
                kicad.config.footprint.PACKAGE_LINE_WIDTH,
            )
        )

        super().add(
            kicad.footprint.element.line(
                kicad.footprint.layer.silkscreen_top,
                -line_x, line_y, line_x, line_y,
                kicad.config.footprint.PACKAGE_LINE_WIDTH
            )
        )

        diff = -line_x - x
        line_y += diff

        # Marker
        super().add(
            kicad.footprint.element.circle(
                kicad.footprint.layer.silkscreen_top,
                x, line_y, x - 0.3, line_y,
                kicad.config.footprint.PACKAGE_LINE_WIDTH
            )
        )

        # Pads
        for i in range(pad_count // 2):
            super().add(
                kicad.footprint.element.pad(
                    kicad.footprint.layers.smd,
                    str(pin),
                    kicad.footprint.type.technology.smd,
                    kicad.footprint.type.shape.rectangle,
                    x, pad_distance / 2,
                    pad_width, pad_height
                )
            )
            x += pad_grid
            pin += 1

        for i in range(pad_count // 2, pad_count):
            x -= pad_grid
            super().add(
                kicad.footprint.element.pad(
                    kicad.footprint.layers.smd,
                    str(pin),
                    kicad.footprint.type.technology.smd,
                    kicad.footprint.type.shape.rectangle,
                    x, -pad_distance / 2,
                    pad_width, pad_height
                )
            )
            pin += 1

        # Outline!!!
