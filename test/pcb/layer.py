import unittest

import kicad.layer

class case(unittest.TestCase):

    def test_layer_set(self):
        self.assertEqual(kicad.layer.copper_top.render(), "F.Cu")
        self.assertEqual(kicad.layer.copper_all.render(), "*.Cu")
        self.assertEqual(kicad.layer.copper_bottom.render(), "B.Cu")

        self.assertEqual(kicad.layer.adhes_top.render(), "F.Adhes")
        self.assertEqual(kicad.layer.adhes_bottom.render(), "B.Adhes")

        self.assertEqual(kicad.layer.paste_top.render(), "F.Paste")
        self.assertEqual(kicad.layer.paste_bottom.render(), "B.Paste")

        self.assertEqual(kicad.layer.silkscreen_top.render(), "F.SilkS")
        self.assertEqual(kicad.layer.silkscreen_bottom.render(), "B.SilkS")

        self.assertEqual(kicad.layer.soldermask_top.render(), "F.Mask")
        self.assertEqual(kicad.layer.soldermask_bottom.render(), "B.Mask")

        self.assertEqual(kicad.layer.courtyard_top.render(), "F.CrtYd")
        self.assertEqual(kicad.layer.courtyard_bottom.render(), "B.CrtYd")

        self.assertEqual(kicad.layer.fabrication_top.render(), "F.Fab")
        self.assertEqual(kicad.layer.fabrication_bottom.render(), "B.Fab")

        self.assertEqual(kicad.layer.user_drawing.render(), "Dwgs.User")
        self.assertEqual(kicad.layer.user_comment.render(), "Cmts.User")
        self.assertEqual(kicad.layer.user_eco1.render(), "Eco1.User")
        self.assertEqual(kicad.layer.user_eco2.render(), "Eco2.User")
        self.assertEqual(kicad.layer.board_outline.render(), "Edge.Cuts")
    #   self.assertEqual(kicad.layer.margin.render(), "Margin")
