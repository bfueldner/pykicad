import math
import pykicadlib.footprint.generator

class wired(pykicadlib.footprint.generator.base):
    '''Generator for wired resistors, capacitors, ...'''

    def __init__(self, name, model, description, tags, package_width, package_height, pad_width, pad_height, pad_grid, pad_distance, count, drill):
        super().__init__(pykicadlib.footprint.type.footprint.thd, name, model, description, tags)

class wired_resistor(pykicadlib.footprint.generator.base):
    '''Wired resistor with beveled edges'''

    def __init__(self, name, model, description, tags, package_width, package_height, pad_diameter, pad_distance, pad_drill):
        super().__init__(pykicadlib.footprint.type.footprint.thd, name, model, description, tags)

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
        bevel = math.sqrt(package_width * package_width + package_height * package_height) * 0.1
        super().add(
            pykicadlib.footprint.element.centered_beveled_rectangle(
                pykicadlib.footprint.layer.silkscreen_top,
                0, 0, package_width, package_height,
                pykicadlib.config.footprint.PACKAGE_LINE_WIDTH,
                bevel
            )
        )

        # Pads
        super().add(
            pykicadlib.footprint.element.pad(
                pykicadlib.footprint.layers.thru_hole,
                '1',
                pykicadlib.footprint.type.technology.thru_hole,
                pykicadlib.footprint.type.shape.circle,
                -pad_distance / 2, 0.0,
                pad_diameter, pad_diameter,
                pad_drill
            )
        )

        super().add(
            pykicadlib.footprint.element.pad(
                pykicadlib.footprint.layers.thru_hole,
                '2',
                pykicadlib.footprint.type.technology.thru_hole,
                pykicadlib.footprint.type.shape.circle,
                +pad_distance / 2, 0.0,
                pad_diameter, pad_diameter,
                pad_drill
            )
        )
