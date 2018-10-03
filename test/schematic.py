import unittest

import kicad.schematic

class case(unittest.TestCase):

    def test_ctor(self):
        test = kicad.schematic.schematic()

        self.assertEqual(test.render(), 'F5 "value" 0 0 10 H V C CNN "ValueX"')
