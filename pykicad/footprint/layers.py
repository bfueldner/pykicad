import pykicad.footprint.layer


connect = [
    pykicad.footprint.layer.copper_top,
    pykicad.footprint.layer.soldermask_top
]

smd = [
    pykicad.footprint.layer.copper_top,
    pykicad.footprint.layer.solderpaste_top,
    pykicad.footprint.layer.soldermask_top
]

thru_hole = [
    pykicad.footprint.layer.copper_all,
    pykicad.footprint.layer.soldermask_all
]
