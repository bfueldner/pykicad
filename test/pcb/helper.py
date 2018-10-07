import unittest

import kicad.pcb.helper

class case(unittest.TestCase):

    def test_helper_quote(self):
        test = kicad.pcb.helper.quote('Text "with" quote')
        self.assertEqual(test, '"Text ""with"" quote"')

    def test_helper_quote_raise(self):
        with self.assertRaises(ValueError):
            kicad.pcb.helper.quote("\xc3")

    def test_float_str(self):
        self.assertEqual(kicad.pcb.helper.float_str(100000.0), "100000.0")
        self.assertEqual(kicad.pcb.helper.float_str(100.0), "100.0")
        self.assertEqual(kicad.pcb.helper.float_str(0.0), "0.0")
        self.assertEqual(kicad.pcb.helper.float_str(0.001), "0.001")
        self.assertEqual(kicad.pcb.helper.float_str(0.000001), "0.000001")

    def test_helper_dimension(self):
        self.assertEqual(str(kicad.pcb.helper.key_value('key', kicad.pcb.helper.dimension(0.0))), "(key 0.0)")

    def test_helper_point2d(self):
        self.assertEqual(str(kicad.pcb.helper.key_value('key', kicad.pcb.helper.point2d(1.0, 2.0))), "(key 1.0 2.0)")

    def test_helper_point2d(self):
        self.assertEqual(str(kicad.pcb.helper.key_value('key', kicad.pcb.helper.point3d(1.0, 2.0, 3.0))), "(key 1.0 2.0 3.0)")

    def test_helper_area(self):
        self.assertEqual(str(kicad.pcb.helper.key_value('key', kicad.pcb.helper.area(-1.0, -2.0, 1.0, 2.0))), "(key -1.0 -2.0 1.0 2.0)")

    def test_key_value(self):
        test = kicad.pcb.helper.key_value('key', 'text')
        self.assertEqual(str(test), '(key text)')

        test = kicad.pcb.helper.key_value('key', kicad.pcb.helper.point2d(1.1, 2.2))
        self.assertEqual(str(test), '(key 1.1 2.2)')

        test.key = 'abc'
        self.assertEqual(str(test), '(abc 1.1 2.2)')

        test.value.x = 1.0
        test.value.y = 2.0
        self.assertEqual(str(test), '(abc 1.0 2.0)')
