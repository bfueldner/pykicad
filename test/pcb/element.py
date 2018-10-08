import unittest

import kicad.pcb.element

class case(unittest.TestCase):

    def test_pcb_element_arc(self):
        test = kicad.pcb.element.arc(kicad.pcb.layer.fabrication_top, 5.0, 3.0, -5.0, -3.0, 90.0, 0.8)
        self.assertEqual(str(test), '(fp_arc (start 5.0 3.0) (end -5.0 -3.0) (angle 90.0) (layer F.Fab) (width 0.8))')

    def test_pcb_element_circle(self):
        test = kicad.pcb.element.circle(kicad.pcb.layer.fabrication_top, 10.0, 20.0, -10.0, -20.0, 0.75)
        self.assertEqual(str(test), '(fp_circle (center 10.0 20.0) (end -10.0 -20.0) (layer F.Fab) (width 0.75))')

    def test_pcb_element_line(self):
        test = kicad.pcb.element.line(kicad.pcb.layer.fabrication_top, 0.0, 0.0, 10.0, 20.0, 0.5)
        self.assertEqual(str(test), '(fp_line (start 0.0 0.0) (end 10.0 20.0) (layer F.Fab) (width 0.5))')
