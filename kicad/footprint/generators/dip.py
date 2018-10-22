import kicad.footprint.generator

class dip(kicad.footprint.generator.base):
    '''Generates footprint for dual inline ICs with pin marker on left side.

* `name`: Name of footprint
* `model`: Filename for 3D model. Be shure to use variable ${KISYS3DMOD} as starting point
* `description`: Textual description of footprint details
* `tags`: Space separated list of parameters with footprint details (searchable from within KiCAD)
* `package_width`: Width of package body
* `package_height`: Height of package body
* `pad_width`: Width of pad
* `pad_height`: Height of pad
* `pad_grid`: Pad distance between pins of one side (Reference is pad center)
* `pad_distance`: Pad distance between pins of opposite pins (Reference is pad center)
* `pad_count`: Count of overall pins
* `pad_drill`: Drill diameter of pad whole
'''

    def __init__(self, name, model, description, tags, package_width, package_height, pad_width, pad_height, pad_grid, pad_distance, pad_count, pad_drill):
        super().__init__(kicad.footprint.type.footprint.thd, name, model, description, tags)

        if pad_count % 2:
            raise ValueError("pad_count is odd")

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

        pin = 1
        x = pad_grid * -((pad_count / 4) - 0.5)
        line_x = package_width / 2

        # Case
        super().add(
            kicad.footprint.element.centered_rectangle(
                kicad.footprint.layer.silkscreen_top,
                0, 0, package_width, package_height,
                kicad.config.footprint.PACKAGE_LINE_WIDTH,
            )
        )

        # Marker
        super().add(
            kicad.footprint.element.arc(
                kicad.footprint.layer.silkscreen_top,
                -line_x, 0.0, -line_x, 1.0,
                -180.0,
                kicad.config.footprint.PACKAGE_LINE_WIDTH
            )
        )

        # Pads
        for i in range(pad_count // 2):
            super().add(
                kicad.footprint.element.pad(
                    kicad.footprint.layers.thru_hole,
                    str(pin),
                    kicad.footprint.type.technology.thru_hole,
                    kicad.footprint.type.shape.oval,
                    x, pad_distance / 2,
                    pad_width, pad_height,
                    pad_drill
                )
            )
            x += pad_grid
            pin += 1

        for i in range(pad_count // 2, pad_count):
            x -= pad_grid
            super().add(
                kicad.footprint.element.pad(
                    kicad.footprint.layers.thru_hole,
                    str(pin),
                    kicad.footprint.type.technology.thru_hole,
                    kicad.footprint.type.shape.oval,
                    x, -pad_distance / 2,
                    pad_width, pad_height,
                    pad_drill
                )
            )
            pin += 1

        # Outline!!!
