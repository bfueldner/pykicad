import kicad.footprint.generator

class chip(kicad.footprint.generator.base):
    '''Generator for chip resistors, capacitors, inductors, MELF and Tantal devices'''

    def __init__(self, name, model, description, tags, package_width, package_height, pad_width, pad_height, pad_distance):
        super().__init__(kicad.footprint.type.footprint.smd, name, model, description, tags)

        self.package_width = package_width
        self.package_height = package_height
        self.pad_width = pad_width
        self.pad_height = pad_height

        # Reference text
        super().add(
            kicad.footprint.element.text(
                kicad.footprint.layer.silkscreen_top,
                kicad.footprint.type.text.reference,
                None,
                -package_width / 2 - kicad.config.footprint.REFERENCE_FONT_SIZE, 0.0,
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
                0.0, 0.0,
                kicad.config.footprint.VALUE_FONT_SIZE,
                kicad.config.footprint.VALUE_FONT_THICKNESS
            )
        )

        # Case
        super().add(
            kicad.footprint.element.centered_rectangle(
                kicad.footprint.layer.silkscreen_top,
                0, 0, package_width, package_height,
                kicad.config.footprint.PACKAGE_LINE_WIDTH,
            )
        )

        # Pads
        super().add(
            kicad.footprint.element.pad(
                kicad.footprint.layers.smd,
                '1',
                kicad.footprint.type.technology.smd,
                kicad.footprint.type.shape.rectangle,
                -pad_distance / 2, 0.0,
                pad_width, pad_height
            )
        )

        super().add(
            kicad.footprint.element.pad(
                kicad.footprint.layers.smd,
                '2',
                kicad.footprint.type.technology.smd,
                kicad.footprint.type.shape.rectangle,
                +pad_distance / 2, 0.0,
                pad_width, pad_height
            )
        )

class chip_pol(chip):
    '''Generator for chip devices with polarity marker'''

    def __init__(self, name, model, description, tags, package_width, package_height, pad_width, pad_height, pad_distance):
        super().__init__(name, model, description, tags, package_width, package_height, pad_width, pad_height, pad_distance)

        line_x = package_width / 4 # + package_width * 0.1
        line_y = package_height / 2

        # Marker
        super().add(
            kicad.footprint.element.line(
                kicad.footprint.layer.silkscreen_top,
                -line_x, -line_y, -line_x, line_y,
                kicad.config.footprint.PACKAGE_LINE_WIDTH,
            )
        )
