import unittest

import kicad.schematic

class case(unittest.TestCase):

    def test_render(self):
        test = kicad.schematic.field(
            kicad.type.field.name,
            "Text",
            10,
            20,
            50,
            kicad.type.orientation.horizontal,
            kicad.type.visibility.visible,
            kicad.type.hjustify.center,
            kicad.type.vjustify.center,
            kicad.type.style.none
        )
        self.assertEqual(test.render(), 'F1 "Text" 10 20 50 H V C CNN "Name"')

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
            )

    def test_error_param_text(self):
        with self.assertRaises(TypeError):
            kicad.schematic.field(
                kicad.type.field.name,
                0,
                10,
                20,
                50,
                kicad.type.orientation.horizontal,
                kicad.type.visibility.visible,
                kicad.type.hjustify.center,
                kicad.type.vjustify.center,
                kicad.type.style.none
            )

    def test_error_param_x(self):
        with self.assertRaises(TypeError):
            kicad.schematic.field(
                kicad.type.field.name,
                "Text",
                0.1,
                20,
                50,
                kicad.type.orientation.horizontal,
                kicad.type.visibility.visible,
                kicad.type.hjustify.center,
                kicad.type.vjustify.center,
                kicad.type.style.none
            )

    def test_error_param_y(self):
        with self.assertRaises(TypeError):
            kicad.schematic.field(
                kicad.type.field.name,
                "Text",
                10,
                0.2,
                50,
                kicad.type.orientation.horizontal,
                kicad.type.visibility.visible,
                kicad.type.hjustify.center,
                kicad.type.vjustify.center,
                kicad.type.style.none
            )

    def test_error_param_dimension(self):
        with self.assertRaises(TypeError):
            kicad.schematic.field(
                kicad.type.field.name,
                "Text",
                10,
                20,
                0.5,
                kicad.type.orientation.horizontal,
                kicad.type.visibility.visible,
                kicad.type.hjustify.center,
                kicad.type.vjustify.center,
                kicad.type.style.none
            )

    def test_error_param_orientation(self):
        with self.assertRaises(TypeError):
            kicad.schematic.field(
                kicad.type.field.name,
                "Text",
                10,
                20,
                50,
                0,
                kicad.type.visibility.visible,
                kicad.type.hjustify.center,
                kicad.type.vjustify.center,
                kicad.type.style.none
            )


    def test_error_param_visibility(self):
        with self.assertRaises(TypeError):
            kicad.schematic.field(
                kicad.type.field.name,
                "Text",
                10,
                20,
                50,
                kicad.type.orientation.horizontal,
                0,
                kicad.type.hjustify.center,
                kicad.type.vjustify.center,
                kicad.type.style.none
            )

    def test_error_param_hjustify(self):
        with self.assertRaises(TypeError):
            kicad.schematic.field(
                kicad.type.field.name,
                "Text",
                10,
                20,
                50,
                kicad.type.orientation.horizontal,
                kicad.type.visibility.visible,
                0,
                kicad.type.vjustify.center,
                kicad.type.style.none
            )


    def test_error_param_vjustify(self):
        with self.assertRaises(TypeError):
            kicad.schematic.field(
                kicad.type.field.name,
                "Text",
                10,
                20,
                50,
                kicad.type.orientation.horizontal,
                kicad.type.visibility.visible,
                kicad.type.hjustify.center,
                0,
                kicad.type.style.none
            )

    def test_error_param_style(self):
        with self.assertRaises(TypeError):
            kicad.schematic.field(
                kicad.type.field.name,
                "Text",
                10,
                20,
                50,
                kicad.type.orientation.horizontal,
                kicad.type.visibility.visible,
                kicad.type.hjustify.center,
                kicad.type.vjustify.center,
                0
            )
