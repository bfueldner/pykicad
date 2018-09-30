import unittest

import kicad.symbol

class case(unittest.TestCase):

    def test_ctor(self):
        test = kicad.symbol.Field(kicad.type.field.value, 'value', 0, 0, 10)

        self.assertEqual(test.render(), 'F5 "value" 0 0 10 H V C CNN "ValueX"')

        x ='''
    def test_attributes(self):
        test = svd.classes.base(None)

        attr = {}
        attr['name'] = 'test'
        attr['enable'] = True
        attr['none'] = None
        test.add_attributes(attr)

        self.assertEqual(test.name, 'test')
        self.assertTrue(test.enable)
        with self.assertRaises(AttributeError):
            self.assertNone(test.none)
'''
