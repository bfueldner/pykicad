import unittest

import kicad.schematic

class case(unittest.TestCase):

    def test_render(self):
        test = kicad.schematic.rectangle(
            -10,
            -20,
            10,
            20,
            50,
            kicad.type.fill.background
        )
        self.assertEqual(test.render(), 'S -10 -20 10 20 0 1 50 f')

        x ='''
    def test_error_param_type(self):
        with self.assertRaises(TypeError):
            kicad.schematic.field(
                0,
                "Text",
                10,
                20,
                50,
                kicad.type.orientation.horizontal,
                kicad.type.visibility.visible,
                kicad.type.hjustify.center,
                kicad.type.vjustify.center,
                kicad.type.style.none
            )'''
