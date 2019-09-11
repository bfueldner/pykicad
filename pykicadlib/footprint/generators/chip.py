import pykicadlib.footprint.generator

class chip(pykicadlib.footprint.generator.base):
    '''Generator for chip resistors, capacitors, inductors, MELF and Tantal devices'''

    def __init__(self, name, model, description, tags, package_width, package_height, pad_width, pad_height, pad_distance):
        super().__init__(pykicadlib.footprint.type.footprint.smd, name, model, description, tags)

        self.package_width = package_width
        self.package_height = package_height
        self.pad_width = pad_width
        self.pad_height = pad_height

        # Reference text
        super().add(
            pykicadlib.footprint.element.text(
                pykicadlib.footprint.layer.silkscreen_top,
                pykicadlib.footprint.type.text.reference,
                None,
                -package_width / 2 - pykicadlib.config.footprint.REFERENCE_FONT_SIZE, 0.0,
                pykicadlib.config.footprint.REFERENCE_FONT_SIZE,
                pykicadlib.config.footprint.REFERENCE_FONT_THICKNESS,
                90.0,
            )
        )

        # Value text
        super().add(
            pykicadlib.footprint.element.text(
                pykicadlib.footprint.layer.fabrication_top,
                pykicadlib.footprint.type.text.value,
                None,
                0.0, 0.0,
                pykicadlib.config.footprint.VALUE_FONT_SIZE,
                pykicadlib.config.footprint.VALUE_FONT_THICKNESS
            )
        )

        # Case
        super().add(
            pykicadlib.footprint.element.centered_rectangle(
                pykicadlib.footprint.layer.silkscreen_top,
                0, 0, package_width, package_height,
                pykicadlib.config.footprint.PACKAGE_LINE_WIDTH,
            )
        )

        # Pads
        super().add(
            pykicadlib.footprint.element.pad(
                pykicadlib.footprint.layers.smd,
                '1',
                pykicadlib.footprint.type.technology.smd,
                pykicadlib.footprint.type.shape.rectangle,
                -pad_distance / 2, 0.0,
                pad_width, pad_height
            )
        )

        super().add(
            pykicadlib.footprint.element.pad(
                pykicadlib.footprint.layers.smd,
                '2',
                pykicadlib.footprint.type.technology.smd,
                pykicadlib.footprint.type.shape.rectangle,
                +pad_distance / 2, 0.0,
                pad_width, pad_height
            )
        )

class chip_pol(chip):
    '''Generator for chip devices with polarity marker'''

    def __init__(self, name, model, description, tags, package_width, package_height, pad_width, pad_height, pad_distance):
        super().__init__(name, model, description, tags, package_width, package_height, pad_width, pad_height, pad_distance)

        # Marker
        line_x = package_width / 4
        line_y = package_height / 2
        super().add(
            pykicadlib.footprint.element.line(
                pykicadlib.footprint.layer.silkscreen_top,
                -line_x, -line_y, -line_x, line_y,
                pykicadlib.config.footprint.PACKAGE_LINE_WIDTH,
            )
        )
