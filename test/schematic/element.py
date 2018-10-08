import unittest

import kicad.schematic.element

class case(unittest.TestCase):

    def test_schematic_element_field(self):
        test = kicad.schematic.element.field(
            kicad.schematic.type.field.name,
            "Text",
            10,
            20,
            50,
            kicad.schematic.type.orientation.horizontal,
            kicad.schematic.type.visibility.visible,
            kicad.schematic.type.hjustify.center,
            kicad.schematic.type.vjustify.center,
            kicad.schematic.type.style.none
        )
        self.assertEqual(str(test), 'F1 "Text" 10 20 50 H V C CNN "Name"')

    def test_schematic_element_field_error_type(self):
        with self.assertRaises(TypeError):
            kicad.schematic.element.field(
                0,
                "Text",
                10,
                20,
                50,
                kicad.schematic.type.orientation.horizontal,
                kicad.schematic.type.visibility.visible,
                kicad.schematic.type.hjustify.center,
                kicad.schematic.type.vjustify.center,
                kicad.schematic.type.style.none
            )

    def test_schematic_element_field_error_text(self):
        with self.assertRaises(TypeError):
            kicad.schematic.element.field(
                kicad.schematic.type.field.name,
                0,
                10,
                20,
                50,
                kicad.schematic.type.orientation.horizontal,
                kicad.schematic.type.visibility.visible,
                kicad.schematic.type.hjustify.center,
                kicad.schematic.type.vjustify.center,
                kicad.schematic.type.style.none
            )

    def test_schematic_element_field_error_x(self):
        with self.assertRaises(TypeError):
            kicad.schematic.element.field(
                kicad.schematic.type.field.name,
                "Text",
                0.1,
                20,
                50,
                kicad.schematic.type.orientation.horizontal,
                kicad.schematic.type.visibility.visible,
                kicad.schematic.type.hjustify.center,
                kicad.schematic.type.vjustify.center,
                kicad.schematic.type.style.none
            )

    def test_schematic_element_field_error_y(self):
        with self.assertRaises(TypeError):
            kicad.schematic.element.field(
                kicad.schematic.type.field.name,
                "Text",
                10,
                0.2,
                50,
                kicad.schematic.type.orientation.horizontal,
                kicad.schematic.type.visibility.visible,
                kicad.schematic.type.hjustify.center,
                kicad.schematic.type.vjustify.center,
                kicad.schematic.type.style.none
            )

    def test_schematic_element_field_error_dimension(self):
        with self.assertRaises(TypeError):
            kicad.schematic.element.field(
                kicad.schematic.type.field.name,
                "Text",
                10,
                20,
                0.5,
                kicad.schematic.type.orientation.horizontal,
                kicad.schematic.type.visibility.visible,
                kicad.schematic.type.hjustify.center,
                kicad.schematic.type.vjustify.center,
                kicad.schematic.type.style.none
            )

    def test_schematic_element_field_error_orientation(self):
        with self.assertRaises(TypeError):
            kicad.schematic.element.field(
                kicad.schematic.type.field.name,
                "Text",
                10,
                20,
                50,
                0,
                kicad.schematic.type.visibility.visible,
                kicad.schematic.type.hjustify.center,
                kicad.schematic.type.vjustify.center,
                kicad.schematic.type.style.none
            )


    def test_schematic_element_field_error_visibility(self):
        with self.assertRaises(TypeError):
            kicad.schematic.element.field(
                kicad.schematic.type.field.name,
                "Text",
                10,
                20,
                50,
                kicad.schematic.type.orientation.horizontal,
                0,
                kicad.schematic.type.hjustify.center,
                kicad.schematic.type.vjustify.center,
                kicad.schematic.type.style.none
            )

    def test_schematic_element_field_error_hjustify(self):
        with self.assertRaises(TypeError):
            kicad.schematic.element.field(
                kicad.schematic.type.field.name,
                "Text",
                10,
                20,
                50,
                kicad.schematic.type.orientation.horizontal,
                kicad.schematic.type.visibility.visible,
                0,
                kicad.schematic.type.vjustify.center,
                kicad.schematic.type.style.none
            )


    def test_schematic_element_field_error_vjustify(self):
        with self.assertRaises(TypeError):
            kicad.schematic.element.field(
                kicad.schematic.type.field.name,
                "Text",
                10,
                20,
                50,
                kicad.schematic.type.orientation.horizontal,
                kicad.schematic.type.visibility.visible,
                kicad.schematic.type.hjustify.center,
                0,
                kicad.schematic.type.style.none
            )

    def test_schematic_element_field_error_style(self):
        with self.assertRaises(TypeError):
            kicad.schematic.element.field(
                kicad.schematic.type.field.name,
                "Text",
                10,
                20,
                50,
                kicad.schematic.type.orientation.horizontal,
                kicad.schematic.type.visibility.visible,
                kicad.schematic.type.hjustify.center,
                kicad.schematic.type.vjustify.center,
                0
            )

    def test_schematic_element_rectangle(self):
        test = kicad.schematic.element.rectangle(
            -10,
            -20,
            10,
            20,
            50,
            kicad.schematic.type.fill.background
        )
        self.assertEqual(str(test), 'S -10 -20 10 20 0 1 50 f')
