import unittest

import kicad.pcb.layer

class case(unittest.TestCase):

    def test_layer_set(self):
        self.assertEqual(str(kicad.pcb.layer.copper_top), "F.Cu")
        self.assertEqual(str(kicad.pcb.layer.copper_all), "*.Cu")
        self.assertEqual(str(kicad.pcb.layer.copper_bottom), "B.Cu")

        self.assertEqual(str(kicad.pcb.layer.adhes_top), "F.Adhes")
        self.assertEqual(str(kicad.pcb.layer.adhes_bottom), "B.Adhes")

        self.assertEqual(str(kicad.pcb.layer.paste_top), "F.Paste")
        self.assertEqual(str(kicad.pcb.layer.paste_bottom), "B.Paste")

        self.assertEqual(str(kicad.pcb.layer.silkscreen_top), "F.SilkS")
        self.assertEqual(str(kicad.pcb.layer.silkscreen_bottom), "B.SilkS")

        self.assertEqual(str(kicad.pcb.layer.soldermask_top), "F.Mask")
        self.assertEqual(str(kicad.pcb.layer.soldermask_bottom), "B.Mask")

        self.assertEqual(str(kicad.pcb.layer.courtyard_top), "F.CrtYd")
        self.assertEqual(str(kicad.pcb.layer.courtyard_bottom), "B.CrtYd")

        self.assertEqual(str(kicad.pcb.layer.fabrication_top), "F.Fab")
        self.assertEqual(str(kicad.pcb.layer.fabrication_bottom), "B.Fab")

        self.assertEqual(str(kicad.pcb.layer.user_drawing), "Dwgs.User")
        self.assertEqual(str(kicad.pcb.layer.user_comment), "Cmts.User")
        self.assertEqual(str(kicad.pcb.layer.user_eco1), "Eco1.User")
        self.assertEqual(str(kicad.pcb.layer.user_eco2), "Eco2.User")
        self.assertEqual(str(kicad.pcb.layer.board_outline), "Edge.Cuts")
    #   self.assertEqual(str(kicad.pcb.layer.margin), "Margin")
