import math
import kicad.footprint.generator

class wired(kicad.footprint.generator.base):
    '''Generator for wired resistors, capacitors, ...'''

    def __init__(self, name, model, description, tags, package_width, package_height, pad_width, pad_height, pad_grid, pad_distance, count, drill):
        super().__init__(kicad.footprint.type.footprint.thd, name, model, description, tags)

class wired_resistor(kicad.footprint.generator.base):
    '''Wired resistor with beveled edges'''

    def __init__(self, name, model, description, tags, package_width, package_height, pad_diameter, pad_distance, pad_drill):
        super().__init__(kicad.footprint.type.footprint.thd, name, model, description, tags)

        # Reference text
        super().add(
            kicad.footprint.element.text(
                kicad.footprint.layer.silkscreen_top,
                kicad.footprint.type.text.reference,
                None,
                0.0, 0.0,
                kicad.config.footprint.REFERENCE_FONT_SIZE,
                kicad.config.footprint.REFERENCE_FONT_THICKNESS
            )
        )

        # Value text
        super().add(
            kicad.footprint.element.text(
                kicad.footprint.layer.fabrication_top,
                kicad.footprint.type.text.value,
                None,
                0.0, kicad.config.footprint.VALUE_FONT_SIZE + 2 * kicad.config.footprint.VALUE_FONT_THICKNESS,
                kicad.config.footprint.VALUE_FONT_SIZE,
                kicad.config.footprint.VALUE_FONT_THICKNESS
            )
        )

        # Case
        bevel = math.sqrt(package_width * package_width + package_height * package_height) * 0.1
        super().add(
            kicad.footprint.element.centered_beveled_rectangle(
                kicad.footprint.layer.silkscreen_top,
                0, 0, package_width, package_height,
                kicad.config.footprint.PACKAGE_LINE_WIDTH,
                bevel
            )
        )

        # Pads
        super().add(
            kicad.footprint.element.pad(
                kicad.footprint.layers.thru_hole,
                '1',
                kicad.footprint.type.technology.thru_hole,
                kicad.footprint.type.shape.circle,
                -pad_distance / 2, 0.0,
                pad_diameter, pad_diameter,
                pad_drill
            )
        )

        super().add(
            kicad.footprint.element.pad(
                kicad.footprint.layers.thru_hole,
                '2',
                kicad.footprint.type.technology.thru_hole,
                kicad.footprint.type.shape.circle,
                +pad_distance / 2, 0.0,
                pad_diameter, pad_diameter,
                pad_drill
            )
        )
