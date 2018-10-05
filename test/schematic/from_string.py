import unittest

import kicad.schematic

class case(unittest.TestCase):

    def test_field(self):
        test = kicad.schematic.from_str(' F1 "Text" 10 20 50 H V C CNN "Name" ')
        self.assertIsInstance(test, kicad.schematic.field)
        #self.assertEqual(test.render(), 'F1 "Text" 10 20 50 H V C CNN "Name"')

    def test_polygon(self):
        test = kicad.schematic.from_str('P 3 0 1 0 -50 50 50 0 -50 -50 F')
        self.assertIsInstance(test, kicad.schematic.polygon)

        test = kicad.schematic.from_str('P 2 0 1 0 50 50 50 -50 N')
        self.assertIsInstance(test, kicad.schematic.polygon)

    def test_polygon(self):
        test = kicad.schematic.from_str('S 0 50 900 900 0 1 0 f')
        self.assertIsInstance(test, kicad.schematic.rectangle)

    def test_circle(self):
        test = kicad.schematic.from_str('C 0 0 70 0 1 0 F')
        self.assertIsInstance(test, kicad.schematic.circle)

        test = kicad.schematic.from_str('C 0 0 20 0 1 0 N')
        self.assertIsInstance(test, kicad.schematic.circle)

    def test_arc(self):
        test = kicad.schematic.from_str('A -1 -200 49 900 -11 0 1 0 N -50 -200 0 -150')
        self.assertIsInstance(test, kicad.schematic.arc)

        test = kicad.schematic.from_str('A 0 -199 49 0 -911 0 1 0 N 0 -150 50 -200')
        self.assertIsInstance(test, kicad.schematic.arc)

    def test_text(self):
        test = kicad.schematic.from_str('T 0 -320 -10 100 0 0 1 VREF')
        self.assertIsInstance(test, kicad.schematic.arc)
