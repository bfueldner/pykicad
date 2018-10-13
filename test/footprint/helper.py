import unittest

import kicad.footprint.helper

class case(unittest.TestCase):

    def test_footprint_helper_quote_str(self):
        self.assertEqual(kicad.footprint.helper.quote_str('Text'), '"Text"')
        self.assertEqual(kicad.footprint.helper.quote_str('Text "with" quote'), '"Text ""with"" quote"')

    def test_footprint_helper_quote_raise(self):
        with self.assertRaises(TypeError):
            kicad.footprint.helper.quote_str(1)

        with self.assertRaises(ValueError):
            kicad.footprint.helper.quote_str("\xc3")

    def test_footprint_helper_float_to_str(self):
        self.assertEqual(kicad.footprint.helper.float_to_str(0.0), "0.0")

        self.assertEqual(kicad.footprint.helper.float_to_str(1000000000.0), "1000000000.0")
        self.assertEqual(kicad.footprint.helper.float_to_str(1000000.0), "1000000.0")
        self.assertEqual(kicad.footprint.helper.float_to_str(1000.0), "1000.0")
        self.assertEqual(kicad.footprint.helper.float_to_str(1.0), "1.0")
        self.assertEqual(kicad.footprint.helper.float_to_str(0.001), "0.001")
        self.assertEqual(kicad.footprint.helper.float_to_str(0.000001), "0.000001")
        self.assertEqual(kicad.footprint.helper.float_to_str(0.000000001), "0.000000001")

    def test_footprint_helper_float_to_str_raise(self):
        with self.assertRaises(TypeError):
            kicad.footprint.helper.float_to_str(1)
