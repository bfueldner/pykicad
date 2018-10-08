import unittest

import kicad.pcb.type
import kicad.pcb.layer

class case(unittest.TestCase):

    def test_pcb_type_text(self):
        self.assertEqual(str(kicad.pcb.type.text('Text')), '"Text"')
        self.assertEqual(str(kicad.pcb.type.text('Text "with" double quote')), '"Text \"\"with\"\" double quote"')

        test = kicad.pcb.type.text('abc')
        self.assertEqual(str(test), '"abc"')

        test.value = '123'
        self.assertEqual(str(test), '"123"')

    def test_pcb_type_value(self):
        test = kicad.pcb.type.value(000.000)
        self.assertEqual(str(test), '0.0')

        test.value = 123.456
        self.assertEqual(str(test), '123.456')


    def test_pcb_type_point2d(self):
        test = kicad.pcb.type.point2d(0.0, 0.0)
        self.assertEqual(str(test), '0.0 0.0')

        test.x = 1000000.0
        test.y = -0.000001
        self.assertEqual(str(test), '1000000.0 -0.000001')

    def test_pcb_type_point3d(self):
        test = kicad.pcb.type.point3d(0.0, 0.0, 0.0)
        self.assertEqual(str(test), '0.0 0.0 0.0')

        test.x = 1000000.0
        test.y = 1.000001
        test.z = -0.000001
        self.assertEqual(str(test), '1000000.0 1.000001 -0.000001')

    def test_pcb_type_area(self):
        test = kicad.pcb.type.area(-1.0, -2.0, 1.0, 2.0)
        self.assertEqual(str(test), '-1.0 -2.0 1.0 2.0')

        test.x1 = -20.0
        test.y1 = -10.0
        test.x2 = 20.0
        test.y2 = 10.0
        self.assertEqual(str(test), '-20.0 -10.0 20.0 10.0')

    def test_pcb_type_key_data(self):
        self.assertEqual(str(kicad.pcb.type.key_data('name', kicad.pcb.type.text('abc'))), '(name "abc")')
        self.assertEqual(str(kicad.pcb.type.key_data('size', kicad.pcb.type.value(0.0))), '(size 0.0)')
        self.assertEqual(str(kicad.pcb.type.key_data('pos', kicad.pcb.type.point2d(1.0, 2.0))), '(pos 1.0 2.0)')
        self.assertEqual(str(kicad.pcb.type.key_data('xyz', kicad.pcb.type.point3d(1.0, 2.0, 3.0))), '(xyz 1.0 2.0 3.0)')
        self.assertEqual(str(kicad.pcb.type.key_data('layer', kicad.pcb.layer.copper_top)), '(layer F.Cu)')
        self.assertEqual(str(kicad.pcb.type.key_data('layers', [kicad.pcb.layer.copper_top, kicad.pcb.layer.solderpaste_top, kicad.pcb.layer.soldermask_top])), '(layers F.Cu F.Paste F.Mask)')
