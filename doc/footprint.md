# Footprint

## Generator `chip`

Generator for chip resistors, capacitors, inductors, MELF and Tantal devices

## Generator `chip_pol`

Generator for chip devices with polarity marker

## Generator `connector_grid_male`

Generator wired connector lines (pins)

## Generator `connector_grid_female`

Generator wired connector lines (plugs)

## Generator `dip`

Generates footprint for dual inline ICs with pin marker on left side.

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


## Generator `qfp`

Generator for LQFP/TQFP/PQFP and other xQFP footprints

## Generator `soic`

Generator for small outline ICs

## Generator `wired`

Generator for wired resistors, capacitors, ...

## Generator `wired_resistor`

Wired resistor with beveled edges

