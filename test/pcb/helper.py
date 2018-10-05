import unittest

import kicad.pcb.helper

class case(unittest.TestCase):

    def test_helper_quote(self):
        test = kicad.pcb.helper.quote('Text "with" quote')
        self.assertEqual(test, '"Text ""with"" quote"')

    def test_helper_quote_raise(self):
        with self.assertRaises(ValueError):
            kicad.pcb.helper.quote("\xc3")

    def test_helper_dimension(self):
        self.assertEqual(kicad.pcb.helper.dimension('key', 0.0).render(), "(key 0.000000)")

    def test_helper_point(self):
        self.assertEqual(kicad.pcb.helper.point('key', 0.0, 0.0).render(), "(key 0.000000 0.000000)")
    #   self.assertEqual(kicad.pcb.helper.point('key', 1.0, 1000.0).render(), "(key 1.0 1000.0)")
    #   self.assertEqual(kicad.pcb.helper.point('key', 0.001, 0.000001).render(), "(key 0.001 0.000001)")

    def test_helper_area(self):
        self.assertEqual(kicad.pcb.helper.area('key', 0.0, 0.0, 0.0, 0.0).render(), "(key 0.000000 0.000000 0.000000 0.000000)")
