import unittest

import kicad.footprint.footprint

class case(unittest.TestCase):

    def test_footprint_footprint_base(self):
        test = kicad.footprint.footprint.base(kicad.footprint.type.technology.smd, 'SOIC', 'soic/soic_8_narrow', 'SOIC Footprint', ['SO', 'SOIC', 'Cool'])
        print(test)

    #    self.assertEqual(kicad.footprint.helper.quote_str('Text'), '"Text"')
