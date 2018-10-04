import unittest

import kicad.schematic

class case(unittest.TestCase):

    def test_render(self):
        test = kicad.schematic.from_str(' F1 "Text" 10 20 50 H V C CNN "Name" ')
        self.assertIsInstance(test, kicad.schematic.field)
        #self.assertEqual(test.render(), 'F1 "Text" 10 20 50 H V C CNN "Name"')
