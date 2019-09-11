import unittest
import pykicadlib.footprint.helper


class TestFootprintHelperQuoteStr(unittest.TestCase):
    def test_values(self):
        self.assertEqual(pykicadlib.footprint.helper.quote_str('Text'), '"Text"')
        self.assertEqual(pykicadlib.footprint.helper.quote_str('Text "with" quote'), '"Text ""with"" quote"')

    def test_exception(self):
        with self.assertRaises(TypeError):
            pykicadlib.footprint.helper.quote_str(1)

        with self.assertRaises(ValueError):
            pykicadlib.footprint.helper.quote_str("\xc3")


class TestFootprintHelperFloatToStr(unittest.TestCase):
    def test_values(self):
        self.assertEqual(pykicadlib.footprint.helper.float_to_str(0.0), "0.0")

        self.assertEqual(pykicadlib.footprint.helper.float_to_str(1000000000.0), "1000000000.0")
        self.assertEqual(pykicadlib.footprint.helper.float_to_str(1000000.0), "1000000.0")
        self.assertEqual(pykicadlib.footprint.helper.float_to_str(1000.0), "1000.0")
        self.assertEqual(pykicadlib.footprint.helper.float_to_str(1.0), "1.0")
        self.assertEqual(pykicadlib.footprint.helper.float_to_str(0.001), "0.001")
        self.assertEqual(pykicadlib.footprint.helper.float_to_str(0.000001), "0.000001")
        self.assertEqual(pykicadlib.footprint.helper.float_to_str(0.000000001), "0.000000001")

    def test_exception(self):
        with self.assertRaises(TypeError):
            pykicadlib.footprint.helper.float_to_str(1)
