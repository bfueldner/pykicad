import unittest

import kicad.type

class case(unittest.TestCase):

    def test_field_reference(self):
        test = kicad.type.field.from_str(0)
        self.assertEqual(test, kicad.type.field.reference)

    def test_field_name(self):
        test = kicad.type.field.from_str(1)
        self.assertEqual(test, kicad.type.field.name)

    def test_field_footprint(self):
        test = kicad.type.field.from_str(2)
        self.assertEqual(test, kicad.type.field.footprint)

    def test_field_document(self):
        test = kicad.type.field.from_str(3)
        self.assertEqual(test, kicad.type.field.document)

    def test_field_manufacturer(self):
        test = kicad.type.field.from_str(4)
        self.assertEqual(test, kicad.type.field.manufacturer)

    def test_field_value(self):
        test = kicad.type.field.from_str(5)
        self.assertEqual(test, kicad.type.field.value)

    def test_field_tolerance(self):
        test = kicad.type.field.from_str(6)
        self.assertEqual(test, kicad.type.field.tolerance)

    def test_field_temperature(self):
        test = kicad.type.field.from_str(7)
        self.assertEqual(test, kicad.type.field.temperature)

    def test_field_model(self):
        test = kicad.type.field.from_str(8)
        self.assertEqual(test, kicad.type.field.model)

    def test_field_voltage(self):
        test = kicad.type.field.from_str(9)
        self.assertEqual(test, kicad.type.field.voltage)

    def test_field_power(self):
        test = kicad.type.field.from_str(10)
        self.assertEqual(test, kicad.type.field.power)

    def test_field_raise(self):
        with self.assertRaises(NotImplementedError):
            kicad.type.orientation.from_str(11)


    def test_orientation_horizontal(self):
        test = kicad.type.orientation.from_str('H')
        self.assertEqual(test, kicad.type.orientation.horizontal)

    def test_orientation_vertical(self):
        test = kicad.type.orientation.from_str('V')
        self.assertEqual(test, kicad.type.orientation.vertical)

    def test_orientation_raise(self):
        with self.assertRaises(NotImplementedError):
            kicad.type.orientation.from_str('X')


    def test_visibility_visible(self):
        test = kicad.type.visibility.from_str('V')
        self.assertEqual(test, kicad.type.visibility.visible)

    def test_visibility_invisible(self):
        test = kicad.type.visibility.from_str('I')
        self.assertEqual(test, kicad.type.visibility.invisible)

    def test_visibility_raise(self):
        with self.assertRaises(NotImplementedError):
            kicad.type.visibility.from_str('X')


    def test_hjustify_left(self):
        test = kicad.type.hjustify.from_str('L')
        self.assertEqual(test, kicad.type.hjustify.left)

    def test_hjustify_center(self):
        test = kicad.type.hjustify.from_str('C')
        self.assertEqual(test, kicad.type.hjustify.center)

    def test_hjustify_right(self):
        test = kicad.type.hjustify.from_str('R')
        self.assertEqual(test, kicad.type.hjustify.right)

    def test_hjustify_raise(self):
        with self.assertRaises(NotImplementedError):
            kicad.type.hjustify.from_str('X')


    def test_vjustify_top(self):
        test = kicad.type.vjustify.from_str('T')
        self.assertEqual(test, kicad.type.vjustify.top)

    def test_vjustify_center(self):
        test = kicad.type.vjustify.from_str('C')
        self.assertEqual(test, kicad.type.vjustify.center)

    def test_vjustify_bottom(self):
        test = kicad.type.vjustify.from_str('B')
        self.assertEqual(test, kicad.type.vjustify.bottom)

    def test_vjustify_raise(self):
        with self.assertRaises(NotImplementedError):
            kicad.type.vjustify.from_str('X')


    def test_style_none(self):
        test = kicad.type.style.from_str('NN')
        self.assertEqual(test, kicad.type.style.none)

    def test_style_italic(self):
        test = kicad.type.style.from_str('IN')
        self.assertEqual(test, kicad.type.style.italic)

    def test_style_bold(self):
        test = kicad.type.style.from_str('NB')
        self.assertEqual(test, kicad.type.style.bold)

    def test_style_italic_bold(self):
        test = kicad.type.style.from_str('IB')
        self.assertEqual(test, kicad.type.style.italic_bold)

    def test_style_raise(self):
        with self.assertRaises(NotImplementedError):
            kicad.type.style.from_str('')
