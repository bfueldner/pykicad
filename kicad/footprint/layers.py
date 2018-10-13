import kicad.footprint.layer

connect = [
    kicad.footprint.layer.copper_top,
    kicad.footprint.layer.soldermask_top
]

smd = [
    kicad.footprint.layer.copper_top,
    kicad.footprint.layer.solderpaste_top,
    kicad.footprint.layer.soldermask_top
]

thru_hole = [
    kicad.footprint.layer.copper_all,
    kicad.footprint.layer.soldermask_all
]
