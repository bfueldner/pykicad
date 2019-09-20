# pylint: disable=too-few-public-methods
"""
.. module:: test.symbol.elements
   :synopsis: Symbol elements "from_str" test

.. moduleauthor:: Benjamin Füldner <benjamin@fueldner.net>
"""
import unittest
import pykicadlib


class TestSymbolElementFromStrField(unittest.TestCase):
    """Test function from_str for pykicadlib.symbol.elements.Field"""

    def test_from_str(self):
        """Test from_str function with Field example"""

        test = pykicadlib.symbol.elements.from_str('F1 "Text" 10 20 50 H V C CNN "Name"')
        self.assertIsInstance(test, pykicadlib.symbol.elements.Field)
        self.assertEqual(test.type, pykicadlib.symbol.types.Field.name)
        self.assertEqual(test.value, 'Text')
        self.assertEqual(test.x, 10)
        self.assertEqual(test.y, 20)
        self.assertEqual(test.size, 50)
        self.assertEqual(test.orientation, pykicadlib.symbol.types.Orientation.horizontal)
        self.assertEqual(test.visibility, pykicadlib.symbol.types.Visibility.visible)
        self.assertEqual(test.hjustify, pykicadlib.symbol.types.HJustify.center)
        self.assertEqual(test.vjustify, pykicadlib.symbol.types.VJustify.center)
        self.assertEqual(test.style, pykicadlib.symbol.types.Style.none)


class TestSymbolElementFromStrPolygon(unittest.TestCase):
    """Test function from_str for pykicadlib.symbol.elements.Polygon"""

    def test_from_str_1(self):
        """Test from_str function with Polygon example 1"""

        test = pykicadlib.symbol.elements.from_str('P 3 0 1 0 -50 50 50 0 -50 -50 F')
        self.assertIsInstance(test, pykicadlib.symbol.elements.Polygon)
        self.assertEqual(len(test.points), 3)
        self.assertEqual(str(test.points[0]), '-50 50')
        self.assertEqual(str(test.points[1]), '50 0')
        self.assertEqual(str(test.points[2]), '-50 -50')
        self.assertEqual(test.unit, 0)
        self.assertEqual(test.representation, pykicadlib.symbol.types.Representation.normal)
        self.assertEqual(test.fill, pykicadlib.symbol.types.Fill.foreground)

    def test_from_str_2(self):
        """Test from_str function with Polygon example 2"""

        test = pykicadlib.symbol.elements.from_str('P 2 0 1 0 50 50 50 -50 N')
        self.assertIsInstance(test, pykicadlib.symbol.elements.Polygon)
        self.assertEqual(len(test.points), 2)
        self.assertEqual(str(test.points[0]), '50 50')
        self.assertEqual(str(test.points[1]), '50 -50')
        self.assertEqual(test.unit, 0)
        self.assertEqual(test.representation, pykicadlib.symbol.types.Representation.normal)
        self.assertEqual(test.fill, pykicadlib.symbol.types.Fill.none)


class TestSymbolElementFromStrRectangle(unittest.TestCase):
    """Test function from_str for pykicadlib.symbol.elements.Rectangle"""

    def test_from_str(self):
        """Test from_str function with Rectangle example"""

        test = pykicadlib.symbol.elements.from_str('S 0 50 900 900 0 1 0 f')
        self.assertIsInstance(test, pykicadlib.symbol.elements.Rectangle)
        self.assertEqual(test.x1, 0)
        self.assertEqual(test.y1, 50)
        self.assertEqual(test.x2, 900)
        self.assertEqual(test.y2, 900)
        self.assertEqual(test.unit, 0)
        self.assertEqual(test.representation, pykicadlib.symbol.types.Representation.normal)
        self.assertEqual(test.thickness, 0)
        self.assertEqual(test.fill, pykicadlib.symbol.types.Fill.background)


class TestSymbolElementFromStrCirlce(unittest.TestCase):
    """Test function from_str for pykicadlib.symbol.elements.Circle"""

    def test_from_str_1(self):
        """Test from_str function with Circle example 1"""

        test = pykicadlib.symbol.elements.from_str('C 10 20 70 2 1 5 F')
        self.assertIsInstance(test, pykicadlib.symbol.elements.Circle)
        self.assertEqual(test.x, 10)
        self.assertEqual(test.y, 20)
        self.assertEqual(test.radius, 70)
        self.assertEqual(test.unit, 2)
        self.assertEqual(test.representation, pykicadlib.symbol.types.Representation.normal)
        self.assertEqual(test.thickness, 5)
        self.assertEqual(test.fill, pykicadlib.symbol.types.Fill.foreground)

    def test_from_str_2(self):
        """Test from_str function with Circle example 2"""

        test = pykicadlib.symbol.elements.from_str('C 0 0 20 0 1 0 N')
        self.assertIsInstance(test, pykicadlib.symbol.elements.Circle)
        self.assertEqual(test.x, 0)
        self.assertEqual(test.y, 0)
        self.assertEqual(test.radius, 20)
        self.assertEqual(test.unit, 0)
        self.assertEqual(test.representation, pykicadlib.symbol.types.Representation.normal)
        self.assertEqual(test.thickness, 0)
        self.assertEqual(test.fill, pykicadlib.symbol.types.Fill.none)


class TestSymbolElementFromStrArc(unittest.TestCase):
    """Test function from_str for pykicadlib.symbol.elements.Arc"""

    def test_from_str_1(self):
        """Test from_str function with Arc example 1"""

        test = pykicadlib.symbol.elements.from_str('A -1 -200 49 900 -11 0 1 0 N -50 -200 0 -150')
        self.assertIsInstance(test, pykicadlib.symbol.elements.Arc)
        self.assertEqual(test.x, -1)
        self.assertEqual(test.y, -200)
        self.assertEqual(test.radius, 49)
        self.assertEqual(test.start_angle, 90.0)
        self.assertEqual(test.end_angle, -1.1)
        self.assertEqual(test.unit, 0)
        self.assertEqual(test.representation, pykicadlib.symbol.types.Representation.normal)
        self.assertEqual(test.thickness, 0)
        self.assertEqual(test.fill, pykicadlib.symbol.types.Fill.none)
        self.assertEqual(test.start_x, -50)
        self.assertEqual(test.start_y, -200)
        self.assertEqual(test.end_x, 0)
        self.assertEqual(test.end_y, -150)

    def test_from_str_2(self):
        """Test from_str function with Arc example 2"""

        test = pykicadlib.symbol.elements.from_str('A 0 -199 49 0 -911 0 1 0 N 0 -150 50 -200')
        self.assertIsInstance(test, pykicadlib.symbol.elements.Arc)
        self.assertEqual(test.x, 0)
        self.assertEqual(test.y, -199)
        self.assertEqual(test.radius, 49)
        self.assertEqual(test.start_angle, 0.0)
        self.assertEqual(test.end_angle, -91.1)
        self.assertEqual(test.unit, 0)
        self.assertEqual(test.representation, pykicadlib.symbol.types.Representation.normal)
        self.assertEqual(test.thickness, 0)
        self.assertEqual(test.fill, pykicadlib.symbol.types.Fill.none)
        self.assertEqual(test.start_x, 0)
        self.assertEqual(test.start_y, -150)
        self.assertEqual(test.end_x, 50)
        self.assertEqual(test.end_y, -200)


class TestSymbolElementFromStrText(unittest.TestCase):
    """Test function from_str for pykicadlib.symbol.elements.Text"""

    def test_from_str_old_format_1(self):
        """Test from_str function with Text example 1 (old format)"""

        test = pykicadlib.symbol.elements.from_str('T 0 -320 -10 100 0 0 1 VREF')
        self.assertIsInstance(test, pykicadlib.symbol.elements.Text)
        self.assertEqual(test.x, -320)
        self.assertEqual(test.y, -10)
        self.assertEqual(test.value, 'VREF')
        self.assertEqual(test.size, 100)
        self.assertEqual(test.angle, 0.0)
        self.assertEqual(test.unit, 0)
        self.assertEqual(test.representation, pykicadlib.symbol.types.Representation.normal)
        self.assertEqual(test.italic, pykicadlib.symbol.types.Italic.off)
        self.assertEqual(test.bold, pykicadlib.symbol.types.Bold.off)
        self.assertEqual(test.hjustify, pykicadlib.symbol.types.HJustify.center)
        self.assertEqual(test.vjustify, pykicadlib.symbol.types.VJustify.center)

    def test_from_str_old_format_2(self):
        """Test from_str function with Text example 2 (old format)"""

        test = pykicadlib.symbol.elements.from_str('T 1 20 10 50 0 2 0 TEXT~SPACE')
        self.assertIsInstance(test, pykicadlib.symbol.elements.Text)
        self.assertEqual(test.x, 20)
        self.assertEqual(test.y, 10)
        self.assertEqual(test.value, 'TEXT SPACE')
        self.assertEqual(test.size, 50)
        self.assertEqual(test.angle, 90.0)
        self.assertEqual(test.unit, 2)
        self.assertEqual(test.representation, pykicadlib.symbol.types.Representation.both)
        self.assertEqual(test.italic, pykicadlib.symbol.types.Italic.off)
        self.assertEqual(test.bold, pykicadlib.symbol.types.Bold.off)
        self.assertEqual(test.hjustify, pykicadlib.symbol.types.HJustify.center)
        self.assertEqual(test.vjustify, pykicadlib.symbol.types.VJustify.center)

    def test_from_str_new_format_1(self):
        """Test from_str function with Text example 1 (new format)"""

        test = pykicadlib.symbol.elements.from_str(
            'T 0 200 100 50 0 0 1 "Text with space" Normal 0 C C')
        self.assertIsInstance(test, pykicadlib.symbol.elements.Text)
        self.assertEqual(test.x, 200)
        self.assertEqual(test.y, 100)
        self.assertEqual(test.value, 'Text with space')
        self.assertEqual(test.size, 50)
        self.assertEqual(test.angle, 0.0)
        self.assertEqual(test.unit, 0)
        self.assertEqual(test.representation, pykicadlib.symbol.types.Representation.normal)
        self.assertEqual(test.italic, pykicadlib.symbol.types.Italic.off)
        self.assertEqual(test.bold, pykicadlib.symbol.types.Bold.off)
        self.assertEqual(test.hjustify, pykicadlib.symbol.types.HJustify.center)
        self.assertEqual(test.vjustify, pykicadlib.symbol.types.VJustify.center)

    def test_from_str_new_format_2(self):
        """Test from_str function with Text example 2 (new format)"""

        test = pykicadlib.symbol.elements.from_str('T 450 10 20 50 0 0 1 "A\'\'B" Normal 0 C C')
        self.assertIsInstance(test, pykicadlib.symbol.elements.Text)
        self.assertEqual(test.x, 10)
        self.assertEqual(test.y, 20)
        self.assertEqual(test.value, 'A"B')
        self.assertEqual(test.size, 50)
        self.assertEqual(test.angle, 45.0)
        self.assertEqual(test.unit, 0)
        self.assertEqual(test.representation, pykicadlib.symbol.types.Representation.normal)
        self.assertEqual(test.italic, pykicadlib.symbol.types.Italic.off)
        self.assertEqual(test.bold, pykicadlib.symbol.types.Bold.off)
        self.assertEqual(test.hjustify, pykicadlib.symbol.types.HJustify.center)
        self.assertEqual(test.vjustify, pykicadlib.symbol.types.VJustify.center)

    def test_from_str_new_format_3(self):
        """Test from_str function with Text example 3 (new format)"""

        test = pykicadlib.symbol.elements.from_str('T 450 10 20 50 0 0 1 "Test" Normal 0 L T')
        self.assertIsInstance(test, pykicadlib.symbol.elements.Text)
        self.assertEqual(test.x, 10)
        self.assertEqual(test.y, 20)
        self.assertEqual(test.value, 'Test')
        self.assertEqual(test.size, 50)
        self.assertEqual(test.angle, 45.0)
        self.assertEqual(test.unit, 0)
        self.assertEqual(test.representation, pykicadlib.symbol.types.Representation.normal)
        self.assertEqual(test.italic, pykicadlib.symbol.types.Italic.off)
        self.assertEqual(test.bold, pykicadlib.symbol.types.Bold.off)
        self.assertEqual(test.hjustify, pykicadlib.symbol.types.HJustify.left)
        self.assertEqual(test.vjustify, pykicadlib.symbol.types.VJustify.top)

    def test_from_str_new_format_4(self):
        """Test from_str function with Text example 4 (new format)"""

        test = pykicadlib.symbol.elements.from_str('T 450 10 20 50 0 0 1 "Test" Normal 0 R B')
        self.assertIsInstance(test, pykicadlib.symbol.elements.Text)
        self.assertEqual(test.x, 10)
        self.assertEqual(test.y, 20)
        self.assertEqual(test.value, 'Test')
        self.assertEqual(test.size, 50)
        self.assertEqual(test.angle, 45.0)
        self.assertEqual(test.unit, 0)
        self.assertEqual(test.representation, pykicadlib.symbol.types.Representation.normal)
        self.assertEqual(test.italic, pykicadlib.symbol.types.Italic.off)
        self.assertEqual(test.bold, pykicadlib.symbol.types.Bold.off)
        self.assertEqual(test.hjustify, pykicadlib.symbol.types.HJustify.right)
        self.assertEqual(test.vjustify, pykicadlib.symbol.types.VJustify.bottom)

    def test_from_str_new_format_5(self):
        """Test from_str function with Text example 5 (new format)"""

        test = pykicadlib.symbol.elements.from_str('T 450 10 20 50 0 0 1 "Test" Italic 1 C C')
        self.assertIsInstance(test, pykicadlib.symbol.elements.Text)
        self.assertEqual(test.x, 10)
        self.assertEqual(test.y, 20)
        self.assertEqual(test.value, 'Test')
        self.assertEqual(test.size, 50)
        self.assertEqual(test.angle, 45.0)
        self.assertEqual(test.unit, 0)
        self.assertEqual(test.representation, pykicadlib.symbol.types.Representation.normal)
        self.assertEqual(test.italic, pykicadlib.symbol.types.Italic.on)
        self.assertEqual(test.bold, pykicadlib.symbol.types.Bold.on)
        self.assertEqual(test.hjustify, pykicadlib.symbol.types.HJustify.center)
        self.assertEqual(test.vjustify, pykicadlib.symbol.types.VJustify.center)


class TestSymbolElementFromStrPin(unittest.TestCase):
    """Test function from_str for pykicadlib.symbol.elements.Pin"""

    def test_from_str_1(self):
        """Test from_str function with Pin example 1"""

        test = pykicadlib.symbol.elements.from_str('X TO 1 -200 0 150 R 40 40 1 1 P')
        self.assertIsInstance(test, pykicadlib.symbol.elements.Pin)
        self.assertEqual(test.x, -200)
        self.assertEqual(test.y, 0)
        self.assertEqual(test.name, 'TO')
        self.assertEqual(test.number, '1')
        self.assertEqual(test.length, 150)
        self.assertEqual(test.direction, pykicadlib.symbol.types.Direction.left)
        self.assertEqual(test.name_size, 40)
        self.assertEqual(test.number_size, 40)
        self.assertEqual(test.unit, 1)
        self.assertEqual(test.representation, pykicadlib.symbol.types.Representation.normal)
        self.assertEqual(test.electric, pykicadlib.symbol.types.Electric.passive)
        self.assertEqual(test.shape, pykicadlib.symbol.types.Shape.line)
        self.assertTrue(test.visible)

    def test_from_str_2(self):
        """Test from_str function with Pin example 2"""

        test = pykicadlib.symbol.elements.from_str('X K 2 200 0 150 L 40 40 1 1 P')
        self.assertIsInstance(test, pykicadlib.symbol.elements.Pin)
        self.assertEqual(test.x, 200)
        self.assertEqual(test.y, 0)
        self.assertEqual(test.name, 'K')
        self.assertEqual(test.number, '2')
        self.assertEqual(test.length, 150)
        self.assertEqual(test.direction, pykicadlib.symbol.types.Direction.right)
        self.assertEqual(test.name_size, 40)
        self.assertEqual(test.number_size, 40)
        self.assertEqual(test.unit, 1)
        self.assertEqual(test.representation, pykicadlib.symbol.types.Representation.normal)
        self.assertEqual(test.electric, pykicadlib.symbol.types.Electric.passive)
        self.assertEqual(test.shape, pykicadlib.symbol.types.Shape.line)
        self.assertTrue(test.visible)

    def test_from_str_3(self):
        """Test from_str function with Pin example 3"""

        test = pykicadlib.symbol.elements.from_str('X 0 1 0 0 0 R 40 40 1 1 W NC')
        self.assertIsInstance(test, pykicadlib.symbol.elements.Pin)
        self.assertEqual(test.x, 0)
        self.assertEqual(test.y, 0)
        self.assertEqual(test.name, '0')
        self.assertEqual(test.number, '1')
        self.assertEqual(test.length, 0)
        self.assertEqual(test.direction, pykicadlib.symbol.types.Direction.left)
        self.assertEqual(test.name_size, 40)
        self.assertEqual(test.number_size, 40)
        self.assertEqual(test.unit, 1)
        self.assertEqual(test.representation, pykicadlib.symbol.types.Representation.normal)
        self.assertEqual(test.electric, pykicadlib.symbol.types.Electric.power_input)
        self.assertEqual(test.shape, pykicadlib.symbol.types.Shape.clock)
        self.assertFalse(test.visible)

    def test_from_str_4(self):
        """Test from_str function with Pin example 4"""

        test = pykicadlib.symbol.elements.from_str('X ~ 2 0 -250 200 U 40 40 1 1 P')
        self.assertIsInstance(test, pykicadlib.symbol.elements.Pin)
        self.assertEqual(test.x, 0)
        self.assertEqual(test.y, -250)
        self.assertEqual(test.name, '~')
        self.assertEqual(test.number, '2')
        self.assertEqual(test.length, 200)
        self.assertEqual(test.direction, pykicadlib.symbol.types.Direction.down)
        self.assertEqual(test.name_size, 40)
        self.assertEqual(test.number_size, 40)
        self.assertEqual(test.unit, 1)
        self.assertEqual(test.representation, pykicadlib.symbol.types.Representation.normal)
        self.assertEqual(test.electric, pykicadlib.symbol.types.Electric.passive)
        self.assertEqual(test.shape, pykicadlib.symbol.types.Shape.line)
        self.assertTrue(test.visible)

    def test_exception(self):
        """Test exception"""

        with self.assertRaises(KeyError):
            pykicadlib.symbol.elements.from_str('Z')
