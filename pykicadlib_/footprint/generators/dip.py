import pykicadlib.footprint.generator

class dip(pykicadlib.footprint.generator.base):
    '''Generates footprint for dual inline ICs with pin marker on left side.

* `name`: Name of footprint
* `model`: Filename for 3D model. Be shure to use variable ${KISYS3DMOD} as starting point
* `description`: Textual description of footprint details
* `tags`: Space separated list of parameters with footprint details (searchable from within pykicadlib)
* `package_width`: Width of package body
* `package_height`: Height of package body
* `pad_width`: Width of pad
* `pad_height`: Height of pad
* `pad_grid`: Pad distance between pins of one side (Reference is pad center)
* `pad_distance`: Pad distance between pins of opposite pins (Reference is pad center)
* `pad_count`: Count of overall pins
* `pad_drill`: Drill diameter of pad hole
'''

    def __init__(self, name, model, description, tags, package_width, package_height, pad_width, pad_height, pad_grid, pad_distance, pad_count, pad_drill):
        super().__init__(pykicadlib.footprint.type.footprint.thd, name, model, description, tags)

        if pad_count % 2:
            raise ValueError("pad_count is odd")

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

        # Marker
        line_x = package_width / 2
        super().add(
            pykicadlib.footprint.element.arc(
                pykicadlib.footprint.layer.silkscreen_top,
                -line_x, 0.0, -line_x, 1.0,
                -180.0,
                pykicadlib.config.footprint.PACKAGE_LINE_WIDTH
            )
        )

        # Pads
        pin = 1
        x = pad_grid * -((pad_count / 4) - 0.5)
        for i in range(pad_count // 2):
            super().add(
                pykicadlib.footprint.element.pad(
                    pykicadlib.footprint.layers.thru_hole,
                    str(pin),
                    pykicadlib.footprint.type.technology.thru_hole,
                    pykicadlib.footprint.type.shape.oval,
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
                pykicadlib.footprint.element.pad(
                    pykicadlib.footprint.layers.thru_hole,
                    str(pin),
                    pykicadlib.footprint.type.technology.thru_hole,
                    pykicadlib.footprint.type.shape.oval,
                    x, -pad_distance / 2,
                    pad_width, pad_height,
                    pad_drill
                )
            )
            pin += 1

        # Outline!!!
