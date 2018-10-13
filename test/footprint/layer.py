import unittest

import kicad.footprint.layer

class case(unittest.TestCase):

    def test_footprint_layer_set(self):
        self.assertEqual(str(kicad.footprint.layer.copper_top), "F.Cu")
        self.assertEqual(str(kicad.footprint.layer.copper_all), "*.Cu")
        self.assertEqual(str(kicad.footprint.layer.copper_bottom), "B.Cu")

        self.assertEqual(str(kicad.footprint.layer.adhes_top), "F.Adhes")
        self.assertEqual(str(kicad.footprint.layer.adhes_bottom), "B.Adhes")

        self.assertEqual(str(kicad.footprint.layer.solderpaste_top), "F.Paste")
        self.assertEqual(str(kicad.footprint.layer.solderpaste_bottom), "B.Paste")

        self.assertEqual(str(kicad.footprint.layer.silkscreen_top), "F.SilkS")
        self.assertEqual(str(kicad.footprint.layer.silkscreen_bottom), "B.SilkS")

        self.assertEqual(str(kicad.footprint.layer.soldermask_top), "F.Mask")
        self.assertEqual(str(kicad.footprint.layer.soldermask_bottom), "B.Mask")

        self.assertEqual(str(kicad.footprint.layer.courtyard_top), "F.CrtYd")
        self.assertEqual(str(kicad.footprint.layer.courtyard_bottom), "B.CrtYd")

        self.assertEqual(str(kicad.footprint.layer.fabrication_top), "F.Fab")
        self.assertEqual(str(kicad.footprint.layer.fabrication_bottom), "B.Fab")

        self.assertEqual(str(kicad.footprint.layer.user_drawing), "Dwgs.User")
        self.assertEqual(str(kicad.footprint.layer.user_comment), "Cmts.User")
        self.assertEqual(str(kicad.footprint.layer.user_eco1), "Eco1.User")
        self.assertEqual(str(kicad.footprint.layer.user_eco2), "Eco2.User")
        self.assertEqual(str(kicad.footprint.layer.board_outline), "Edge.Cuts")
    #   self.assertEqual(str(kicad.footprint.layer.margin), "Margin")
