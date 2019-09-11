import math

import pykicadlib.footprint.generator

class dsub(pykicadlib.footprint.generator.base):
    '''Generates footprint for dsub connectors.

* `name`: Name of footprint
* `model`: Filename for 3D model. Be shure to use variable ${KISYS3DMOD} as starting point
* `description`: Textual description of footprint details
* `tags`: Space separated list of parameters with footprint details (searchable from within KiCAD)
* `package_width`: Width of package body
* `package_height`: Height of package body
* `mounting_distance`: Distance of mounting holes
* `mounting_drill`: Drill diameter of mounting hole Distance of mounting holes

* `pad_width`: Width of pad
* `pad_height`: Height of pad
* `pad_grid`: Pad distance between pins of one side (Reference is pad center)
* `pad_distance`: Pad distance between pins of opposite pins (Reference is pad center)
* `pad_count`: Count of overall pins
* `pad_drill`: Drill diameter of pad hole
'''

    def __init__(self, name, model, description, tags, package_width, package_height_up, package_height_down, mounting_distance, mounting_diameter, mounting_drill, connector_width, connector_height, screw_width, screw_height, pad_diameter, pad_grid, pad_distance, pad_drill, pin_count):
        super().__init__(pykicadlib.footprint.type.footprint.thd, name, model, description, tags)

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
                0.0, pad_distance / 2 + pad_diameter / 2 + pykicadlib.config.footprint.VALUE_FONT_SIZE,
                pykicadlib.config.footprint.VALUE_FONT_SIZE,
                pykicadlib.config.footprint.VALUE_FONT_THICKNESS
            )
        )

        # Case
        super().add(
            pykicadlib.footprint.element.rectangle(
                pykicadlib.footprint.layer.silkscreen_top,
                -package_width / 2, package_height_up,
                package_width / 2, package_height_down,
                pykicadlib.config.footprint.PACKAGE_LINE_WIDTH,
            )
        )

        # Line
        y = package_height_down - 0.5
        super().add(
            pykicadlib.footprint.element.line(
                pykicadlib.footprint.layer.silkscreen_top,
                -package_width / 2, y,
                package_width / 2, y,
                pykicadlib.config.footprint.PACKAGE_LINE_WIDTH,
            )
        )

        # Frame
        y -= 2.0
        super().add(
            pykicadlib.footprint.element.line(
                pykicadlib.footprint.layer.silkscreen_top,
                -connector_width / 2, package_height_up,
                -connector_width / 2, y,
                pykicadlib.config.footprint.PACKAGE_LINE_WIDTH,
            )
        )
        super().add(
            pykicadlib.footprint.element.line(
                pykicadlib.footprint.layer.silkscreen_top,
                -connector_width / 2, y,
                connector_width / 2, y,
                pykicadlib.config.footprint.PACKAGE_LINE_WIDTH,
            )
        )
        super().add(
            pykicadlib.footprint.element.line(
                pykicadlib.footprint.layer.silkscreen_top,
                connector_width / 2, y,
                connector_width / 2, package_height_up,
                pykicadlib.config.footprint.PACKAGE_LINE_WIDTH,
            )
        )

        # Connector
        radius = 1.0
        x = -connector_width / 2
        y = package_height_down + connector_height - radius
        super().add(
            pykicadlib.footprint.element.line(
                pykicadlib.footprint.layer.silkscreen_top,
                x, package_height_down,
                x, y,
                pykicadlib.config.footprint.PACKAGE_LINE_WIDTH,
            )
        )
        y += radius
        x += radius
        super().add(
            pykicadlib.footprint.element.arc(
                pykicadlib.footprint.layer.silkscreen_top,
                x, y - radius,
                x, y,
                90.0,
                pykicadlib.config.footprint.PACKAGE_LINE_WIDTH,
            )
        )
        super().add(
            pykicadlib.footprint.element.line(
                pykicadlib.footprint.layer.silkscreen_top,
                x, y,
                -x, y,
                pykicadlib.config.footprint.PACKAGE_LINE_WIDTH,
            )
        )
        x = -x + radius
        y -= radius
        super().add(
            pykicadlib.footprint.element.arc(
                pykicadlib.footprint.layer.silkscreen_top,
                x - radius, y,
                x, y,
                90.0,
                pykicadlib.config.footprint.PACKAGE_LINE_WIDTH,
            )
        )
        super().add(
            pykicadlib.footprint.element.line(
                pykicadlib.footprint.layer.silkscreen_top,
                x, y,
                x, package_height_down,
                pykicadlib.config.footprint.PACKAGE_LINE_WIDTH,
            )
        )

        # Screws
        y = package_height_down
        for x in [-mounting_distance / 2, mounting_distance / 2]:
            super().add(
                pykicadlib.footprint.element.rounded_rectangle(
                    pykicadlib.footprint.layer.silkscreen_top,
                    x - screw_width / 2, y,
                    x - screw_width * 0.5 / 2, y + screw_height,
                    pykicadlib.config.footprint.PACKAGE_LINE_WIDTH,
                    0.5
                )
            )
            super().add(
                pykicadlib.footprint.element.rounded_rectangle(
                    pykicadlib.footprint.layer.silkscreen_top,
                    x - screw_width * 0.5 / 2, y,
                    x + screw_width * 0.5 / 2, y + screw_height,
                    pykicadlib.config.footprint.PACKAGE_LINE_WIDTH,
                    0.5
                )
            )
            super().add(
                pykicadlib.footprint.element.rounded_rectangle(
                    pykicadlib.footprint.layer.silkscreen_top,
                    x + screw_width * 0.5 / 2, y,
                    x + screw_width / 2, y + screw_height,
                    pykicadlib.config.footprint.PACKAGE_LINE_WIDTH,
                    0.5
                )
            )
            super().add(
                pykicadlib.footprint.element.line(
                    pykicadlib.footprint.layer.silkscreen_top,
                    x - screw_width / 2 + 0.5, y + screw_height,
                    x + screw_width / 2 - 0.5, y + screw_height,
                    pykicadlib.config.footprint.PACKAGE_LINE_WIDTH
                )
            )

        # Mounting
        super().add(
            pykicadlib.footprint.element.pad(
                pykicadlib.footprint.layers.thru_hole,
                '',
                pykicadlib.footprint.type.technology.thru_hole,
                pykicadlib.footprint.type.shape.circle,
                -mounting_distance / 2, 0.0,
                mounting_diameter, mounting_diameter,
                mounting_drill
            )
        )

        super().add(
            pykicadlib.footprint.element.pad(
                pykicadlib.footprint.layers.thru_hole,
                '',
                pykicadlib.footprint.type.technology.np_thru_hole,
                pykicadlib.footprint.type.shape.circle,
                mounting_distance / 2, 0.0,
                mounting_drill, mounting_drill,
                mounting_drill
            )
        )

        # Pads
        pin = 1
        upper_row = math.ceil(pin_count / 2)
        lower_row = pin_count - upper_row

        x = -(upper_row - 1) / 2 * pad_grid
        y = -pad_distance / 2
        for i in range(math.ceil(pin_count / 2)):
            super().add(
                pykicadlib.footprint.element.pad(
                    pykicadlib.footprint.layers.thru_hole,
                    str(pin),
                    pykicadlib.footprint.type.technology.thru_hole,
                    pykicadlib.footprint.type.shape.rectangle if pin == 1 else pykicadlib.footprint.type.shape.circle,
                    x, y,
                    pad_diameter, pad_diameter,
                    pad_drill
                )
            )
            x += pad_grid
            pin += 1

        x = -(lower_row - 1) / 2 * pad_grid
        y = pad_distance / 2
        for i in range(math.floor(pin_count / 2)):
            super().add(
                pykicadlib.footprint.element.pad(
                    pykicadlib.footprint.layers.thru_hole,
                    str(pin),
                    pykicadlib.footprint.type.technology.thru_hole,
                    pykicadlib.footprint.type.shape.circle,
                    x, y,
                    pad_diameter, pad_diameter,
                    pad_drill
                )
            )
            x += pad_grid
            pin += 1
