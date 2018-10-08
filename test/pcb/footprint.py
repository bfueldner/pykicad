import unittest

import kicad.pcb.footprint

class case(unittest.TestCase):

    def test_pcb_footprint_base(self):
        test = kicad.pcb.footprint.base(kicad.pcb.type.technology.smd, 'SOIC', None, 'SOIC Footprint', ['SO', 'SOIC', 'Cool'])
        print(test)

    #    self.assertEqual(kicad.pcb.helper.quote_str('Text'), '"Text"')
