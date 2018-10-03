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
