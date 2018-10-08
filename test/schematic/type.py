import unittest

import kicad.schematic.type

class case(unittest.TestCase):

    def test_schematic_type_field_reference(self):
        test = kicad.schematic.type.field.from_str(0)
        self.assertEqual(test, kicad.schematic.type.field.reference)

    def test_schematic_type_field_name(self):
        test = kicad.schematic.type.field.from_str(1)
        self.assertEqual(test, kicad.schematic.type.field.name)

    def test_schematic_type_field_footprint(self):
        test = kicad.schematic.type.field.from_str(2)
        self.assertEqual(test, kicad.schematic.type.field.footprint)

    def test_schematic_type_field_document(self):
        test = kicad.schematic.type.field.from_str(3)
        self.assertEqual(test, kicad.schematic.type.field.document)

    def test_schematic_type_field_manufacturer(self):
        test = kicad.schematic.type.field.from_str(4)
        self.assertEqual(test, kicad.schematic.type.field.manufacturer)

    def test_schematic_type_field_value(self):
        test = kicad.schematic.type.field.from_str(5)
        self.assertEqual(test, kicad.schematic.type.field.value)

    def test_schematic_type_field_tolerance(self):
        test = kicad.schematic.type.field.from_str(6)
        self.assertEqual(test, kicad.schematic.type.field.tolerance)

    def test_schematic_type_field_temperature(self):
        test = kicad.schematic.type.field.from_str(7)
        self.assertEqual(test, kicad.schematic.type.field.temperature)

    def test_schematic_type_field_model(self):
        test = kicad.schematic.type.field.from_str(8)
        self.assertEqual(test, kicad.schematic.type.field.model)

    def test_schematic_type_field_voltage(self):
        test = kicad.schematic.type.field.from_str(9)
        self.assertEqual(test, kicad.schematic.type.field.voltage)

    def test_schematic_type_field_power(self):
        test = kicad.schematic.type.field.from_str(10)
        self.assertEqual(test, kicad.schematic.type.field.power)

    def test_schematic_type_field_raise(self):
        with self.assertRaises(NotImplementedError):
            kicad.schematic.type.orientation.from_str(11)


    def test_schematic_type_orientation_horizontal(self):
        test = kicad.schematic.type.orientation.from_str('H')
        self.assertEqual(test, kicad.schematic.type.orientation.horizontal)

    def test_schematic_type_orientation_vertical(self):
        test = kicad.schematic.type.orientation.from_str('V')
        self.assertEqual(test, kicad.schematic.type.orientation.vertical)

    def test_schematic_type_orientation_raise(self):
        with self.assertRaises(NotImplementedError):
            kicad.schematic.type.orientation.from_str('X')


    def test_schematic_type_visibility_visible(self):
        test = kicad.schematic.type.visibility.from_str('V')
        self.assertEqual(test, kicad.schematic.type.visibility.visible)

    def test_schematic_type_visibility_invisible(self):
        test = kicad.schematic.type.visibility.from_str('I')
        self.assertEqual(test, kicad.schematic.type.visibility.invisible)

    def test_schematic_type_visibility_raise(self):
        with self.assertRaises(NotImplementedError):
            kicad.schematic.type.visibility.from_str('X')


    def test_schematic_type_hjustify_left(self):
        test = kicad.schematic.type.hjustify.from_str('L')
        self.assertEqual(test, kicad.schematic.type.hjustify.left)

    def test_schematic_type_hjustify_center(self):
        test = kicad.schematic.type.hjustify.from_str('C')
        self.assertEqual(test, kicad.schematic.type.hjustify.center)

    def test_schematic_type_hjustify_right(self):
        test = kicad.schematic.type.hjustify.from_str('R')
        self.assertEqual(test, kicad.schematic.type.hjustify.right)

    def test_schematic_type_hjustify_raise(self):
        with self.assertRaises(NotImplementedError):
            kicad.schematic.type.hjustify.from_str('X')


    def test_schematic_type_vjustify_top(self):
        test = kicad.schematic.type.vjustify.from_str('T')
        self.assertEqual(test, kicad.schematic.type.vjustify.top)

    def test_schematic_type_vjustify_center(self):
        test = kicad.schematic.type.vjustify.from_str('C')
        self.assertEqual(test, kicad.schematic.type.vjustify.center)

    def test_schematic_type_vjustify_bottom(self):
        test = kicad.schematic.type.vjustify.from_str('B')
        self.assertEqual(test, kicad.schematic.type.vjustify.bottom)

    def test_schematic_type_vjustify_raise(self):
        with self.assertRaises(NotImplementedError):
            kicad.schematic.type.vjustify.from_str('X')


    def test_schematic_type_style_none(self):
        test = kicad.schematic.type.style.from_str('NN')
        self.assertEqual(test, kicad.schematic.type.style.none)

    def test_schematic_type_style_italic(self):
        test = kicad.schematic.type.style.from_str('IN')
        self.assertEqual(test, kicad.schematic.type.style.italic)

    def test_schematic_type_style_bold(self):
        test = kicad.schematic.type.style.from_str('NB')
        self.assertEqual(test, kicad.schematic.type.style.bold)

    def test_schematic_type_style_italic_bold(self):
        test = kicad.schematic.type.style.from_str('IB')
        self.assertEqual(test, kicad.schematic.type.style.italic_bold)

    def test_schematic_type_style_raise(self):
        with self.assertRaises(NotImplementedError):
            kicad.schematic.type.style.from_str('')


    def test_schematic_type_fill_none(self):
        test = kicad.schematic.type.fill.from_str('N')
        self.assertEqual(test, kicad.schematic.type.fill.none)

    def test_schematic_type_fill_foreground(self):
        test = kicad.schematic.type.fill.from_str('F')
        self.assertEqual(test, kicad.schematic.type.fill.foreground)

    def test_schematic_type_fill_background(self):
        test = kicad.schematic.type.fill.from_str('f')
        self.assertEqual(test, kicad.schematic.type.fill.background)

    def test_schematic_type_fill_raise(self):
        with self.assertRaises(NotImplementedError):
            kicad.schematic.type.fill.from_str('X')


    def test_schematic_type_representation_both(self):
        test = kicad.schematic.type.representation.from_str(0)
        self.assertEqual(test, kicad.schematic.type.representation.both)

    def test_schematic_type_representation_normal(self):
        test = kicad.schematic.type.representation.from_str(1)
        self.assertEqual(test, kicad.schematic.type.representation.normal)

    def test_schematic_type_representation_morgan(self):
        test = kicad.schematic.type.representation.from_str(2)
        self.assertEqual(test, kicad.schematic.type.representation.morgan)

    def test_schematic_type_representation_raise(self):
        with self.assertRaises(NotImplementedError):
            kicad.schematic.type.representation.from_str(-1)
