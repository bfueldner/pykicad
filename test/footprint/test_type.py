import unittest
import pykicad.footprint


class TestFootprintTypeName(unittest.TestCase):
    def test_name(self):
        self.assertEqual(str(pykicad.footprint.type.name('Text')), '"Text"')
        self.assertEqual(str(pykicad.footprint.type.name('Text "with" double quote')), '"Text \"\"with\"\" double quote"')

        test = pykicad.footprint.type.name('abc')
        self.assertEqual(str(test), '"abc"')

        test.value = '123'
        self.assertEqual(str(test), '"123"')


class TestFootprintTypeValue(unittest.TestCase):
    def test_value(self):
        test = pykicad.footprint.type.value(000.000)
        self.assertEqual(str(test), '0.0')

        test.value = 123.456
        self.assertEqual(str(test), '123.456')


class TestFootprintTypePoint2d(unittest.TestCase):
    def test_point2d(self):
        test = pykicad.footprint.type.point2d(0.0, 0.0)
        self.assertEqual(str(test), '0.0 0.0')

        test.x = 1000000.0
        test.y = -0.000001
        self.assertEqual(str(test), '1000000.0 -0.000001')


class TestFootprintTypePoint3d(unittest.TestCase):
    def test_point3d(self):
        test = pykicad.footprint.type.point3d(0.0, 0.0, 0.0)
        self.assertEqual(str(test), '0.0 0.0 0.0')

        test.x = 1000000.0
        test.y = 1.000001
        test.z = -0.000001
        self.assertEqual(str(test), '1000000.0 1.000001 -0.000001')


class TestFootprintTypeArea(unittest.TestCase):
    def test_area(self):
        test = pykicad.footprint.type.area(-1.0, -2.0, 1.0, 2.0)
        self.assertEqual(str(test), '-1.0 -2.0 1.0 2.0')

        test.x1 = -20.0
        test.y1 = -10.0
        test.x2 = 20.0
        test.y2 = 10.0
        self.assertEqual(str(test), '-20.0 -10.0 20.0 10.0')


class TestFootprintTypeKeyData(unittest.TestCase):
    def test_key_data(self):
        self.assertEqual(str(pykicad.footprint.type.key_data('name', pykicad.footprint.type.name('abc'))), '(name "abc")')
        self.assertEqual(str(pykicad.footprint.type.key_data('size', pykicad.footprint.type.value(0.0))), '(size 0.0)')
        self.assertEqual(str(pykicad.footprint.type.key_data('pos', pykicad.footprint.type.point2d(1.0, 2.0))), '(pos 1.0 2.0)')
        self.assertEqual(str(pykicad.footprint.type.key_data('xyz', pykicad.footprint.type.point3d(1.0, 2.0, 3.0))), '(xyz 1.0 2.0 3.0)')
        self.assertEqual(str(pykicad.footprint.type.key_data('layer', pykicad.footprint.layer.copper_top)), '(layer F.Cu)')
        self.assertEqual(str(pykicad.footprint.type.key_data('layers', [
            pykicad.footprint.layer.copper_top,
            pykicad.footprint.layer.solderpaste_top,
            pykicad.footprint.layer.soldermask_top])), '(layers F.Cu F.Paste F.Mask)')
