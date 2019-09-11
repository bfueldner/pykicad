import unittest
import pykicadlib.footprint.layer


class TestFootprintLayer(unittest.TestCase):
    def test_set(self):
        self.assertEqual(str(pykicadlib.footprint.layer.copper_top), "F.Cu")
        self.assertEqual(str(pykicadlib.footprint.layer.copper_all), "*.Cu")
        self.assertEqual(str(pykicadlib.footprint.layer.copper_bottom), "B.Cu")

        self.assertEqual(str(pykicadlib.footprint.layer.adhes_top), "F.Adhes")
        self.assertEqual(str(pykicadlib.footprint.layer.adhes_bottom), "B.Adhes")

        self.assertEqual(str(pykicadlib.footprint.layer.solderpaste_top), "F.Paste")
        self.assertEqual(str(pykicadlib.footprint.layer.solderpaste_bottom), "B.Paste")

        self.assertEqual(str(pykicadlib.footprint.layer.silkscreen_top), "F.SilkS")
        self.assertEqual(str(pykicadlib.footprint.layer.silkscreen_bottom), "B.SilkS")

        self.assertEqual(str(pykicadlib.footprint.layer.soldermask_top), "F.Mask")
        self.assertEqual(str(pykicadlib.footprint.layer.soldermask_bottom), "B.Mask")

        self.assertEqual(str(pykicadlib.footprint.layer.courtyard_top), "F.CrtYd")
        self.assertEqual(str(pykicadlib.footprint.layer.courtyard_bottom), "B.CrtYd")

        self.assertEqual(str(pykicadlib.footprint.layer.fabrication_top), "F.Fab")
        self.assertEqual(str(pykicadlib.footprint.layer.fabrication_bottom), "B.Fab")

        self.assertEqual(str(pykicadlib.footprint.layer.user_drawing), "Dwgs.User")
        self.assertEqual(str(pykicadlib.footprint.layer.user_comment), "Cmts.User")
        self.assertEqual(str(pykicadlib.footprint.layer.user_eco1), "Eco1.User")
        self.assertEqual(str(pykicadlib.footprint.layer.user_eco2), "Eco2.User")
        self.assertEqual(str(pykicadlib.footprint.layer.board_outline), "Edge.Cuts")
    #   self.assertEqual(str(pykicadlib.footprint.layer.margin), "Margin")
