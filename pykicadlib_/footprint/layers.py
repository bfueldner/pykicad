import pykicadlib


connect = [
    pykicadlib.footprint.layer.copper_top,
    pykicadlib.footprint.layer.soldermask_top
]

smd = [
    pykicadlib.footprint.layer.copper_top,
    pykicadlib.footprint.layer.solderpaste_top,
    pykicadlib.footprint.layer.soldermask_top
]

thru_hole = [
    pykicadlib.footprint.layer.copper_all,
    pykicadlib.footprint.layer.soldermask_all
]
