import unittest

import kicad.footprint.type
import kicad.footprint.layer

class case(unittest.TestCase):

    def test_footprint_type_name(self):
        self.assertEqual(str(kicad.footprint.type.name('Text')), '"Text"')
        self.assertEqual(str(kicad.footprint.type.name('Text "with" double quote')), '"Text \"\"with\"\" double quote"')

        test = kicad.footprint.type.name('abc')
        self.assertEqual(str(test), '"abc"')

        test.value = '123'
        self.assertEqual(str(test), '"123"')

    def test_footprint_type_value(self):
        test = kicad.footprint.type.value(000.000)
        self.assertEqual(str(test), '0.0')

        test.value = 123.456
        self.assertEqual(str(test), '123.456')


    def test_footprint_type_point2d(self):
        test = kicad.footprint.type.point2d(0.0, 0.0)
        self.assertEqual(str(test), '0.0 0.0')

        test.x = 1000000.0
        test.y = -0.000001
        self.assertEqual(str(test), '1000000.0 -0.000001')

    def test_footprint_type_point3d(self):
        test = kicad.footprint.type.point3d(0.0, 0.0, 0.0)
        self.assertEqual(str(test), '0.0 0.0 0.0')

        test.x = 1000000.0
        test.y = 1.000001
        test.z = -0.000001
        self.assertEqual(str(test), '1000000.0 1.000001 -0.000001')

    def test_footprint_type_area(self):
        test = kicad.footprint.type.area(-1.0, -2.0, 1.0, 2.0)
        self.assertEqual(str(test), '-1.0 -2.0 1.0 2.0')

        test.x1 = -20.0
        test.y1 = -10.0
        test.x2 = 20.0
        test.y2 = 10.0
        self.assertEqual(str(test), '-20.0 -10.0 20.0 10.0')

    def test_footprint_type_key_data(self):
        self.assertEqual(str(kicad.footprint.type.key_data('name', kicad.footprint.type.name('abc'))), '(name "abc")')
        self.assertEqual(str(kicad.footprint.type.key_data('size', kicad.footprint.type.value(0.0))), '(size 0.0)')
        self.assertEqual(str(kicad.footprint.type.key_data('pos', kicad.footprint.type.point2d(1.0, 2.0))), '(pos 1.0 2.0)')
        self.assertEqual(str(kicad.footprint.type.key_data('xyz', kicad.footprint.type.point3d(1.0, 2.0, 3.0))), '(xyz 1.0 2.0 3.0)')
        self.assertEqual(str(kicad.footprint.type.key_data('layer', kicad.footprint.layer.copper_top)), '(layer F.Cu)')
        self.assertEqual(str(kicad.footprint.type.key_data('layers', [kicad.footprint.layer.copper_top, kicad.footprint.layer.solderpaste_top, kicad.footprint.layer.soldermask_top])), '(layers F.Cu F.Paste F.Mask)')
