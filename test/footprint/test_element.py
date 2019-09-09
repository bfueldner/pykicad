import unittest
import pykicad.footprint


class TestFootprintElementText(unittest.TestCase):
    def test_text(self):
        test = pykicad.footprint.element.text(
            pykicad.footprint.layer.silkscreen_top,
            pykicad.footprint.type.text.reference,
            None,
            0.0, 0.0,
            1.5,
            0.1)
        self.assertEqual(str(test),
            '(fp_text reference REF** (at 0.0 0.0 0.0) (layer F.SilkS) (effects (font (size 1.5 1.5) (thickness 0.1))))')

        test = pykicad.footprint.element.text(
            pykicad.footprint.layer.silkscreen_top,
            pykicad.footprint.type.text.value,
            None,
            1.0, 2.0,
            1.0,
            0.15,
            90.0)
        self.assertEqual(str(test), '(fp_text value VAL** (at 1.0 2.0 90.0) (layer F.SilkS) (effects (font (size 1.0 1.0) (thickness 0.15))))')

        test = pykicad.footprint.element.text(
            pykicad.footprint.layer.fabrication_top,
            pykicad.footprint.type.text.user,
            'Text',
            0.0, 0.0,
            1.5,
            0.2,
            45.0,
            pykicad.footprint.type.style.italic)
        self.assertEqual(str(test), '(fp_text user "Text" (at 0.0 0.0 45.0) (layer F.Fab) (effects (font (size 1.5 1.5) (thickness 0.2) italic)))')


class TestFootprintElementArc(unittest.TestCase):
    def test_arc(self):
        test = pykicad.footprint.element.arc(pykicad.footprint.layer.fabrication_top, 5.0, 3.0, -5.0, -3.0, 90.0, 0.8)
        self.assertEqual(str(test), '(fp_arc (start 5.0 3.0) (end -5.0 -3.0) (angle 90.0) (layer F.Fab) (width 0.8))')


class TestFootprintElementCircle(unittest.TestCase):
    def test_circle(self):
        test = pykicad.footprint.element.circle(pykicad.footprint.layer.fabrication_top, 10.0, 20.0, -10.0, -20.0, 0.75)
        self.assertEqual(str(test), '(fp_circle (center 10.0 20.0) (end -10.0 -20.0) (layer F.Fab) (width 0.75))')


class TestFootprintElementLine(unittest.TestCase):
    def test_line(self):
        test = pykicad.footprint.element.line(pykicad.footprint.layer.fabrication_top, 0.0, 0.0, 10.0, 20.0, 0.5)
        self.assertEqual(str(test), '(fp_line (start 0.0 0.0) (end 10.0 20.0) (layer F.Fab) (width 0.5))')


class TestFootprintElementPad(unittest.TestCase):
    def test_pad(self):
        test = pykicad.footprint.element.pad(
            pykicad.footprint.layers.smd,
            '1',
            pykicad.footprint.type.technology.smd,
            pykicad.footprint.type.shape.rectangle,
            0.0, 0.0,
            2.0, 3.0
        )
        self.assertEqual(str(test), '(pad "1" smd rect (at 0.0 0.0 0.0) (size 2.0 3.0) (layers F.Cu F.Paste F.Mask))')

        test = pykicad.footprint.element.pad(
            pykicad.footprint.layers.smd,
            'A',
            pykicad.footprint.type.technology.smd,
            pykicad.footprint.type.shape.rectangle,
            0.0, 0.0,
            2.0, 3.0,
            None,
            45.0
        )
        self.assertEqual(str(test), '(pad "A" smd rect (at 0.0 0.0 45.0) (size 2.0 3.0) (layers F.Cu F.Paste F.Mask))')

        test = pykicad.footprint.element.pad(
            pykicad.footprint.layers.thru_hole,
            'A1',
            pykicad.footprint.type.technology.thru_hole,
            pykicad.footprint.type.shape.circle,
            -1.0, -2.0,
            2.0, 2.0,
            0.1
        )
        self.assertEqual(str(test), '(pad "A1" thru_hole circle (at -1.0 -2.0 0.0) (size 2.0 2.0) (drill 0.1) (layers *.Cu *.Mask))')

        test = pykicad.footprint.element.pad(
            pykicad.footprint.layers.thru_hole,
            'A1',
            pykicad.footprint.type.technology.np_thru_hole,
            pykicad.footprint.type.shape.oval,
            -2.0, -1.0,
            4.0, 2.0,
            0.5
        )
        self.assertEqual(str(test), '(pad "" np_thru_hole oval (at -2.0 -1.0 0.0) (size 4.0 2.0) (drill 0.5) (layers *.Cu *.Mask))')
