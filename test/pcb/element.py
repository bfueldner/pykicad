import unittest

import kicad.pcb.element

class case(unittest.TestCase):

    def test_pcb_element_line(self):
        test = kicad.pcb.element.line(kicad.pcb.layer.fabrication_top, 0.0, 0.0, 10.0, 20.0, 0.5)
        self.assertEqual(str(test), '(fp_line (start 0.0 0.0) (end 10.0 20.0) (layer F.Fab) (width 0.5))')
