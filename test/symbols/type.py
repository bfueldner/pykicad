import unittest

import kicad.symbols.type

class case(unittest.TestCase):

    def test_symbols_type_field_reference(self):
        test = kicad.symbols.type.field.from_str('0')
        self.assertEqual(test, kicad.symbols.type.field.reference)
        self.assertEqual(str(kicad.symbols.type.field.reference), 'Reference')

    def test_symbols_type_field_name(self):
        test = kicad.symbols.type.field.from_str('1')
        self.assertEqual(test, kicad.symbols.type.field.name)
        self.assertEqual(str(kicad.symbols.type.field.name), 'Name')

    def test_symbols_type_field_footprint(self):
        test = kicad.symbols.type.field.from_str('2')
        self.assertEqual(test, kicad.symbols.type.field.footprint)
        self.assertEqual(str(kicad.symbols.type.field.footprint), 'Footprint')

    def test_symbols_type_field_document(self):
        test = kicad.symbols.type.field.from_str('3')
        self.assertEqual(test, kicad.symbols.type.field.document)
        self.assertEqual(str(kicad.symbols.type.field.document), 'Document')

    def test_symbols_type_field_manufacturer(self):
        test = kicad.symbols.type.field.from_str('4')
        self.assertEqual(test, kicad.symbols.type.field.manufacturer)
        self.assertEqual(str(kicad.symbols.type.field.manufacturer), 'Manufacturer')

    def test_symbols_type_field_value(self):
        test = kicad.symbols.type.field.from_str('5')
        self.assertEqual(test, kicad.symbols.type.field.value)
        self.assertEqual(str(kicad.symbols.type.field.value), 'Value')

    def test_symbols_type_field_tolerance(self):
        test = kicad.symbols.type.field.from_str('6')
        self.assertEqual(test, kicad.symbols.type.field.tolerance)
        self.assertEqual(str(kicad.symbols.type.field.tolerance), 'Tolerance')

    def test_symbols_type_field_temperature(self):
        test = kicad.symbols.type.field.from_str('7')
        self.assertEqual(test, kicad.symbols.type.field.temperature)
        self.assertEqual(str(kicad.symbols.type.field.temperature), 'Temperature')

    def test_symbols_type_field_model(self):
        test = kicad.symbols.type.field.from_str('8')
        self.assertEqual(test, kicad.symbols.type.field.model)
        self.assertEqual(str(kicad.symbols.type.field.model), 'Model')

    def test_symbols_type_field_voltage(self):
        test = kicad.symbols.type.field.from_str('9')
        self.assertEqual(test, kicad.symbols.type.field.voltage)
        self.assertEqual(str(kicad.symbols.type.field.voltage), 'Voltage')

    def test_symbols_type_field_power(self):
        test = kicad.symbols.type.field.from_str('10')
        self.assertEqual(test, kicad.symbols.type.field.power)
        self.assertEqual(str(kicad.symbols.type.field.power), 'Power')

    def test_symbols_type_field_raise(self):
        with self.assertRaises(ValueError):
            kicad.symbols.type.field.from_str('')

        with self.assertRaises(ValueError):
            kicad.symbols.type.field.from_str('A')

        with self.assertRaises(NotImplementedError):
            kicad.symbols.type.field.from_str('11')


    def test_symbols_type_orientation_horizontal(self):
        test = kicad.symbols.type.orientation.from_str('H')
        self.assertEqual(test, kicad.symbols.type.orientation.horizontal)
        self.assertEqual(str(kicad.symbols.type.orientation.horizontal), 'H')

    def test_symbols_type_orientation_vertical(self):
        test = kicad.symbols.type.orientation.from_str('V')
        self.assertEqual(test, kicad.symbols.type.orientation.vertical)
        self.assertEqual(str(kicad.symbols.type.orientation.vertical), 'V')

    def test_symbols_type_orientation_raise(self):
        with self.assertRaises(NotImplementedError):
            kicad.symbols.type.orientation.from_str('')


    def test_symbols_type_visibility_visible(self):
        test = kicad.symbols.type.visibility.from_str('V')
        self.assertEqual(test, kicad.symbols.type.visibility.visible)
        self.assertEqual(str(kicad.symbols.type.visibility.visible), 'V')

    def test_symbols_type_visibility_invisible(self):
        test = kicad.symbols.type.visibility.from_str('I')
        self.assertEqual(test, kicad.symbols.type.visibility.invisible)
        self.assertEqual(str(kicad.symbols.type.visibility.invisible), 'I')

    def test_symbols_type_visibility_raise(self):
        with self.assertRaises(NotImplementedError):
            kicad.symbols.type.visibility.from_str('')


    def test_symbols_type_hjustify_left(self):
        test = kicad.symbols.type.hjustify.from_str('L')
        self.assertEqual(test, kicad.symbols.type.hjustify.left)
        self.assertEqual(str(kicad.symbols.type.hjustify.left), 'L')

    def test_symbols_type_hjustify_center(self):
        test = kicad.symbols.type.hjustify.from_str('C')
        self.assertEqual(test, kicad.symbols.type.hjustify.center)
        self.assertEqual(str(kicad.symbols.type.hjustify.center), 'C')

    def test_symbols_type_hjustify_right(self):
        test = kicad.symbols.type.hjustify.from_str('R')
        self.assertEqual(test, kicad.symbols.type.hjustify.right)
        self.assertEqual(str(kicad.symbols.type.hjustify.right), 'R')

    def test_symbols_type_hjustify_raise(self):
        with self.assertRaises(NotImplementedError):
            kicad.symbols.type.hjustify.from_str('')


    def test_symbols_type_vjustify_top(self):
        test = kicad.symbols.type.vjustify.from_str('T')
        self.assertEqual(test, kicad.symbols.type.vjustify.top)
        self.assertEqual(str(kicad.symbols.type.vjustify.top), 'T')

    def test_symbols_type_vjustify_center(self):
        test = kicad.symbols.type.vjustify.from_str('C')
        self.assertEqual(test, kicad.symbols.type.vjustify.center)
        self.assertEqual(str(kicad.symbols.type.vjustify.center), 'C')

    def test_symbols_type_vjustify_bottom(self):
        test = kicad.symbols.type.vjustify.from_str('B')
        self.assertEqual(test, kicad.symbols.type.vjustify.bottom)
        self.assertEqual(str(kicad.symbols.type.vjustify.bottom), 'B')

    def test_symbols_type_vjustify_raise(self):
        with self.assertRaises(NotImplementedError):
            kicad.symbols.type.vjustify.from_str('X')


    def test_symbols_type_style_none(self):
        test = kicad.symbols.type.style.from_str('NN')
        self.assertEqual(test, kicad.symbols.type.style.none)
        self.assertEqual(str(kicad.symbols.type.style.none), 'NN')

    def test_symbols_type_style_italic(self):
        test = kicad.symbols.type.style.from_str('IN')
        self.assertEqual(test, kicad.symbols.type.style.italic)
        self.assertEqual(str(kicad.symbols.type.style.italic), 'IN')

    def test_symbols_type_style_bold(self):
        test = kicad.symbols.type.style.from_str('NB')
        self.assertEqual(test, kicad.symbols.type.style.bold)
        self.assertEqual(str(kicad.symbols.type.style.bold), 'NB')

    def test_symbols_type_style_italic_bold(self):
        test = kicad.symbols.type.style.from_str('IB')
        self.assertEqual(test, kicad.symbols.type.style.italic_bold)
        self.assertEqual(str(kicad.symbols.type.style.italic_bold), 'IB')

    def test_symbols_type_style_raise(self):
        with self.assertRaises(NotImplementedError):
            kicad.symbols.type.style.from_str('')


    def test_symbols_type_fill_none(self):
        test = kicad.symbols.type.fill.from_str('N')
        self.assertEqual(test, kicad.symbols.type.fill.none)
        self.assertEqual(str(kicad.symbols.type.fill.none), 'N')

    def test_symbols_type_fill_foreground(self):
        test = kicad.symbols.type.fill.from_str('F')
        self.assertEqual(test, kicad.symbols.type.fill.foreground)
        self.assertEqual(str(kicad.symbols.type.fill.foreground), 'F')

    def test_symbols_type_fill_background(self):
        test = kicad.symbols.type.fill.from_str('f')
        self.assertEqual(test, kicad.symbols.type.fill.background)
        self.assertEqual(str(kicad.symbols.type.fill.background), 'f')

    def test_symbols_type_fill_raise(self):
        with self.assertRaises(NotImplementedError):
            kicad.symbols.type.fill.from_str('')


    def test_symbols_type_representation_both(self):
        test = kicad.symbols.type.representation.from_str('0')
        self.assertEqual(test, kicad.symbols.type.representation.both)
        self.assertEqual(str(kicad.symbols.type.representation.both), '0')

    def test_symbols_type_representation_normal(self):
        test = kicad.symbols.type.representation.from_str('1')
        self.assertEqual(test, kicad.symbols.type.representation.normal)

    def test_symbols_type_representation_morgan(self):
        test = kicad.symbols.type.representation.from_str('2')
        self.assertEqual(test, kicad.symbols.type.representation.morgan)

    def test_symbols_type_representation_raise(self):
        with self.assertRaises(ValueError):
            kicad.symbols.type.representation.from_str('')

        with self.assertRaises(ValueError):
            kicad.symbols.type.representation.from_str('A')

        with self.assertRaises(NotImplementedError):
            kicad.symbols.type.representation.from_str('3')


    def test_symbols_type_fill_none(self):
        test = kicad.symbols.type.fill.from_str('N')
        self.assertEqual(test, kicad.symbols.type.fill.none)
        self.assertEqual(str(kicad.symbols.type.fill.none), 'N')

    def test_symbols_type_fill_foreground(self):
        test = kicad.symbols.type.fill.from_str('F')
        self.assertEqual(test, kicad.symbols.type.fill.foreground)
        self.assertEqual(str(kicad.symbols.type.fill.foreground), 'F')

    def test_symbols_type_fill_background(self):
        test = kicad.symbols.type.fill.from_str('f')
        self.assertEqual(test, kicad.symbols.type.fill.background)
        self.assertEqual(str(kicad.symbols.type.fill.background), 'f')

    def test_symbols_type_fill_raise(self):
        with self.assertRaises(NotImplementedError):
            kicad.symbols.type.fill.from_str('')


    def test_symbols_type_representation_both(self):
        test = kicad.symbols.type.representation.from_str('0')
        self.assertEqual(test, kicad.symbols.type.representation.both)
        self.assertEqual(str(kicad.symbols.type.representation.both), '0')

    def test_symbols_type_representation_normal(self):
        test = kicad.symbols.type.representation.from_str('1')
        self.assertEqual(test, kicad.symbols.type.representation.normal)
        self.assertEqual(str(kicad.symbols.type.representation.normal), '1')

    def test_symbols_type_representation_morgan(self):
        test = kicad.symbols.type.representation.from_str('2')
        self.assertEqual(test, kicad.symbols.type.representation.morgan)
        self.assertEqual(str(kicad.symbols.type.representation.morgan), '2')

    def test_symbols_type_representation_raise(self):
        with self.assertRaises(ValueError):
            kicad.symbols.type.representation.from_str('')

        with self.assertRaises(ValueError):
            kicad.symbols.type.representation.from_str('A')

        with self.assertRaises(NotImplementedError):
            kicad.symbols.type.representation.from_str('3')


    def test_symbols_type_italic_off(self):
        test = kicad.symbols.type.italic.from_str('Normal')
        self.assertEqual(test, kicad.symbols.type.italic.off)
        self.assertEqual(str(kicad.symbols.type.italic.off), 'Normal')

    def test_symbols_type_italic_on(self):
        test = kicad.symbols.type.italic.from_str('Italic')
        self.assertEqual(test, kicad.symbols.type.italic.on)
        self.assertEqual(str(kicad.symbols.type.italic.on), 'Italic')

    def test_symbols_type_italic_raise(self):
        with self.assertRaises(NotImplementedError):
            kicad.symbols.type.italic.from_str('')


    def test_symbols_type_bold_off(self):
        test = kicad.symbols.type.bold.from_str('0')
        self.assertEqual(test, kicad.symbols.type.bold.off)
        self.assertEqual(str(kicad.symbols.type.bold.off), '0')

    def test_symbols_type_bold_on(self):
        test = kicad.symbols.type.bold.from_str('1')
        self.assertEqual(test, kicad.symbols.type.bold.on)
        self.assertEqual(str(kicad.symbols.type.bold.on), '1')

    def test_symbols_type_bold_raise(self):
        with self.assertRaises(ValueError):
            kicad.symbols.type.bold.from_str('')

        with self.assertRaises(ValueError):
            kicad.symbols.type.bold.from_str('A')

        with self.assertRaises(NotImplementedError):
            kicad.symbols.type.bold.from_str('2')
