import kicad.footprint.generator

class connector_grid_male(kicad.footprint.generator.base):
    '''Generator wired connector lines (pins)'''

    def __init__(self, name, model, description, tags, package_width, package_height, pad_diameter, pad_grid, pad_drill, pin_count_x, pin_count_y):
        super().__init__(kicad.footprint.type.footprint.thd, name, model, description, tags)

        # Reference text
        super().add(
            kicad.footprint.element.text(
                kicad.footprint.layer.silkscreen_top,
                kicad.footprint.type.text.reference,
                None,
                0.0, -(package_height + kicad.config.footprint.REFERENCE_FONT_SIZE) / 2 - 2 * kicad.config.footprint.REFERENCE_FONT_THICKNESS,
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
                0.0, (package_height + kicad.config.footprint.VALUE_FONT_SIZE) / 2 + 2 * kicad.config.footprint.VALUE_FONT_THICKNESS,
                kicad.config.footprint.VALUE_FONT_SIZE,
                kicad.config.footprint.VALUE_FONT_THICKNESS
            )
        )

        # Case
        bevel = pad_grid * 0.2
        super().add(
            kicad.footprint.element.centered_beveled_outline(
                kicad.footprint.layer.fabrication_top,
                0.0, 0.0, package_width, package_height,
                kicad.config.footprint.PACKAGE_LINE_WIDTH,
                bevel,
                pad_grid
            )
        )

        # Pads
        pin = 1
        y = pad_grid * -((float(pin_count_y) / 2) - 0.5)
        for i in range(pin_count_y):
            x = pad_grid * -((float(pin_count_x) / 2) - 0.5)
            for j in range(pin_count_x):
                super().add(
                    kicad.footprint.element.pad(
                        kicad.footprint.layers.thru_hole,
                        str(pin),
                        kicad.footprint.type.technology.thru_hole,
                        kicad.footprint.type.shape.rectangle if pin == 1 else kicad.footprint.type.shape.circle,
                        x, y,
                        pad_diameter, pad_diameter,
                        pad_drill
                    )
                )

                pin += 1
                x += pad_grid
            y += pad_grid

class connector_grid_female(kicad.footprint.generator.base):
    '''Generator wired connector lines (plugs)'''

    def __init__(self, name, description, tags, package_width, package_height, pad_diameter, pad_grid, pad_drill, pin_count_x, pin_count_y):
        super().__init__(kicad.footprint.type.footprint.thd, name, model, description, tags)

        # Reference text
        super().add(
            kicad.footprint.element.text(
                kicad.footprint.layer.silkscreen_top,
                kicad.footprint.type.text.reference,
                None,
                0.0, -(package_height + kicad.config.footprint.REFERENCE_FONT_SIZE) / 2 - 2 * kicad.config.footprint.REFERENCE_FONT_THICKNESS,
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
                0.0, (package_height + kicad.config.footprint.VALUE_FONT_SIZE) / 2 + 2 * kicad.config.footprint.VALUE_FONT_THICKNESS,
                kicad.config.footprint.VALUE_FONT_SIZE,
                kicad.config.footprint.VALUE_FONT_THICKNESS
            )
        )

        # Case
        bevel = pad_grid * 0.2
        super().add(
            kicad.footprint.element.centered_beveled_outline(
                kicad.footprint.layer.fabrication_top,
                0.0, 0.0, package_width, package_height,
                kicad.config.footprint.PACKAGE_LINE_WIDTH,
                bevel,
                pad_grid
            )
        )

        pin = 1
        y = pad_grid * -((float(pin_count_y) / 2) - 0.5)
        for i in range(pin_count_y):
            x = pad_grid * ((float(pin_count_x) / 2) - 0.5)
            for j in range(pin_count_x):
                super().add(
                    kicad.footprint.element.pad(
                        kicad.footprint.layers.thru_hole,
                        str(pin),
                        kicad.footprint.type.technology.thru_hole,
                        kicad.footprint.type.shape.rectangle if pin == 1 else kicad.footprint.type.shape.circle,
                        x, y,
                        pad_diameter, pad_diameter,
                        pad_drill
                    )
                )

                pin += 1
                x -= pad_grid
            y += pad_grid
