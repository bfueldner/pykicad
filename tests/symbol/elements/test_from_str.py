# pylint: disable=too-few-public-methods
"""Test KiCAD symbol element from_str.

.. module:: test.symbol.elements
   :synopsis: Symbol elements "from_str" test

.. moduleauthor:: Benjamin Füldner <benjamin@fueldner.net>
"""

import unittest
from pykicadlib.config import Symbol
from pykicadlib.symbol.elements import Arc, Circle, Field, Pin, Polygon, Rectangle, Text
from pykicadlib.symbol.elements.from_str import from_str


class TestSymbolElementFromStrField(unittest.TestCase):
    """Test function from_str for pykicadlib.symbol.elements.Field"""

    def test_from_str(self):
        """Test from_str function with Field example"""

        test = from_str('F1 "Text" 10 20 50 H V C CNN "Name"', True)
        self.assertIsInstance(test, Field)
        self.assertEqual(test.type, Field.Type.name)
        self.assertEqual(test.value, 'Text')
        self.assertEqual(test.x, 10)
        self.assertEqual(test.y, 20)
        self.assertEqual(test.size, Symbol.FIELD_TEXT_SIZE)
        self.assertEqual(test.orientation, Field.Orientation.horizontal)
        self.assertEqual(test.visibility, Field.Visibility.visible)
        self.assertEqual(test.hjustify, Field.HJustify.center)
        self.assertEqual(test.vjustify, Field.VJustify.center)
        self.assertEqual(test.style, Field.Style.none)

    def test_exception(self):
        """Test value exception."""
        with self.assertRaises(ValueError):
            from_str('F1')


class TestSymbolElementFromStrPolygon(unittest.TestCase):
    """Test function from_str for pykicadlib.symbol.elements.Polygon"""

    def test_from_str_1(self):
        """Test from_str function with Polygon example 1"""

        test = from_str('P 3 0 1 0 -50 50 50 0 -50 -50 F')
        self.assertIsInstance(test, Polygon)
        self.assertEqual(test.unit, 0)
        self.assertEqual(test.representation, Polygon.Representation.normal)
        self.assertEqual(test.fill, Polygon.Fill.foreground)

        self.assertEqual(len(test.points), 3)
        self.assertEqual(str(test.points[0]), '-50 50')
        self.assertEqual(str(test.points[1]), '50 0')
        self.assertEqual(str(test.points[2]), '-50 -50')

    def test_from_str_2(self):
        """Test from_str function with Polygon example 2"""

        test = from_str('P 2 0 1 0 50 50 50 -50 N')
        self.assertIsInstance(test, Polygon)
        self.assertEqual(test.unit, 0)
        self.assertEqual(test.representation, Polygon.Representation.normal)
        self.assertEqual(test.fill, Polygon.Fill.none)

        self.assertEqual(len(test.points), 2)
        self.assertEqual(str(test.points[0]), '50 50')
        self.assertEqual(str(test.points[1]), '50 -50')

    def test_exception(self):
        """Test value exception."""
        with self.assertRaises(ValueError):
            from_str('P')


class TestSymbolElementFromStrRectangle(unittest.TestCase):
    """Test function from_str for pykicadlib.symbol.elements.Rectangle"""

    def test_from_str(self):
        """Test from_str function with Rectangle example"""

        test = from_str('S 0 50 900 900 0 1 0 f')
        self.assertIsInstance(test, Rectangle)
        self.assertEqual(test.x1, 0)
        self.assertEqual(test.y1, 50)
        self.assertEqual(test.x2, 900)
        self.assertEqual(test.y2, 900)
        self.assertEqual(test.unit, 0)
        self.assertEqual(test.representation, Rectangle.Representation.normal)
        self.assertEqual(test.thickness, 0)
        self.assertEqual(test.fill, Rectangle.Fill.background)

    def test_exception(self):
        """Test value exception."""
        with self.assertRaises(ValueError):
            from_str('S')


class TestSymbolElementFromStrCirlce(unittest.TestCase):
    """Test function from_str for pykicadlib.symbol.elements.Circle"""

    def test_from_str_1(self):
        """Test from_str function with Circle example 1"""

        test = from_str('C 10 20 70 2 1 5 F')
        self.assertIsInstance(test, Circle)
        self.assertEqual(test.x, 10)
        self.assertEqual(test.y, 20)
        self.assertEqual(test.radius, 70)
        self.assertEqual(test.unit, 2)
        self.assertEqual(test.representation, Circle.Representation.normal)
        self.assertEqual(test.thickness, 5)
        self.assertEqual(test.fill, Circle.Fill.foreground)

    def test_from_str_2(self):
        """Test from_str function with Circle example 2"""

        test = from_str('C 0 0 20 0 1 0 N')
        self.assertIsInstance(test, Circle)
        self.assertEqual(test.x, 0)
        self.assertEqual(test.y, 0)
        self.assertEqual(test.radius, 20)
        self.assertEqual(test.unit, 0)
        self.assertEqual(test.representation, Circle.Representation.normal)
        self.assertEqual(test.thickness, 0)
        self.assertEqual(test.fill, Circle.Fill.none)

    def test_exception(self):
        """Test value exception."""
        with self.assertRaises(ValueError):
            from_str('C')


class TestSymbolElementFromStrArc(unittest.TestCase):
    """Test function from_str for pykicadlib.symbol.elements.Arc"""

    def test_from_str_1(self):
        """Test from_str function with Arc example 1"""

        test = from_str('A -1 -200 49 900 -11 0 1 0 N -50 -200 0 -150')
        self.assertIsInstance(test, Arc)
        self.assertEqual(test.x, -1)
        self.assertEqual(test.y, -200)
        self.assertEqual(test.radius, 49)
        self.assertEqual(test.start_angle, 90.0)
        self.assertEqual(test.end_angle, -1.1)
        self.assertEqual(test.unit, 0)
        self.assertEqual(test.representation, Arc.Representation.normal)
        self.assertEqual(test.thickness, 0)
        self.assertEqual(test.fill, Arc.Fill.none)
        self.assertEqual(test.start_x, -50)
        self.assertEqual(test.start_y, -200)
        self.assertEqual(test.end_x, 0)
        self.assertEqual(test.end_y, -150)

    def test_from_str_2(self):
        """Test from_str function with Arc example 2"""

        test = from_str('A 0 -199 49 0 -911 0 1 0 N 0 -150 50 -200')
        self.assertIsInstance(test, Arc)
        self.assertEqual(test.x, 0)
        self.assertEqual(test.y, -199)
        self.assertEqual(test.radius, 49)
        self.assertEqual(test.start_angle, 0.0)
        self.assertEqual(test.end_angle, -91.1)
        self.assertEqual(test.unit, 0)
        self.assertEqual(test.representation, Arc.Representation.normal)
        self.assertEqual(test.thickness, 0)
        self.assertEqual(test.fill, Arc.Fill.none)
        self.assertEqual(test.start_x, 0)
        self.assertEqual(test.start_y, -150)
        self.assertEqual(test.end_x, 50)
        self.assertEqual(test.end_y, -200)

    def test_exception(self):
        """Test value exception."""
        with self.assertRaises(ValueError):
            from_str('A')


class TestSymbolElementFromStrText(unittest.TestCase):
    """Test function from_str for pykicadlib.symbol.elements.Text"""

    def test_from_str_old_format_1(self):
        """Test from_str function with Text example 1 (old format)"""

        test = from_str('T 0 -320 -10 100 0 0 1 VREF')
        self.assertIsInstance(test, Text)
        self.assertEqual(test.x, -320)
        self.assertEqual(test.y, -10)
        self.assertEqual(test.value, 'VREF')
        self.assertEqual(test.size, 100)
        self.assertEqual(test.angle, 0.0)
        self.assertEqual(test.unit, 0)
        self.assertEqual(test.representation, Text.Representation.normal)
        self.assertEqual(test.italic, Text.Italic.off)
        self.assertEqual(test.bold, Text.Bold.off)
        self.assertEqual(test.hjustify, Text.HJustify.center)
        self.assertEqual(test.vjustify, Text.VJustify.center)

    def test_from_str_old_format_2(self):
        """Test from_str function with Text example 2 (old format)"""

        test = from_str('T 1 20 10 50 0 2 0 TEXT~SPACE')
        self.assertIsInstance(test, Text)
        self.assertEqual(test.x, 20)
        self.assertEqual(test.y, 10)
        self.assertEqual(test.value, 'TEXT SPACE')
        self.assertEqual(test.size, 50)
        self.assertEqual(test.angle, 90.0)
        self.assertEqual(test.unit, 2)
        self.assertEqual(test.representation, Text.Representation.both)
        self.assertEqual(test.italic, Text.Italic.off)
        self.assertEqual(test.bold, Text.Bold.off)
        self.assertEqual(test.hjustify, Text.HJustify.center)
        self.assertEqual(test.vjustify, Text.VJustify.center)

    def test_from_str_new_format_1(self):
        """Test from_str function with Text example 1 (new format)"""

        test = from_str('T 0 200 100 50 0 0 1 "Text with space" Normal 0 C C')
        self.assertIsInstance(test, Text)
        self.assertEqual(test.x, 200)
        self.assertEqual(test.y, 100)
        self.assertEqual(test.value, 'Text with space')
        self.assertEqual(test.size, 50)
        self.assertEqual(test.angle, 0.0)
        self.assertEqual(test.unit, 0)
        self.assertEqual(test.representation, Text.Representation.normal)
        self.assertEqual(test.italic, Text.Italic.off)
        self.assertEqual(test.bold, Text.Bold.off)
        self.assertEqual(test.hjustify, Text.HJustify.center)
        self.assertEqual(test.vjustify, Text.VJustify.center)

    def test_from_str_new_format_2(self):
        """Test from_str function with Text example 2 (new format)"""

        test = from_str('T 450 10 20 50 0 0 1 "A\'\'B" Normal 0 C C')
        self.assertIsInstance(test, Text)
        self.assertEqual(test.x, 10)
        self.assertEqual(test.y, 20)
        self.assertEqual(test.value, 'A"B')
        self.assertEqual(test.size, 50)
        self.assertEqual(test.angle, 45.0)
        self.assertEqual(test.unit, 0)
        self.assertEqual(test.representation, Text.Representation.normal)
        self.assertEqual(test.italic, Text.Italic.off)
        self.assertEqual(test.bold, Text.Bold.off)
        self.assertEqual(test.hjustify, Text.HJustify.center)
        self.assertEqual(test.vjustify, Text.VJustify.center)

    def test_from_str_new_format_3(self):
        """Test from_str function with Text example 3 (new format)"""

        test = from_str('T 450 10 20 50 0 0 1 "Test" Normal 0 L T')
        self.assertIsInstance(test, Text)
        self.assertEqual(test.x, 10)
        self.assertEqual(test.y, 20)
        self.assertEqual(test.value, 'Test')
        self.assertEqual(test.size, 50)
        self.assertEqual(test.angle, 45.0)
        self.assertEqual(test.unit, 0)
        self.assertEqual(test.representation, Text.Representation.normal)
        self.assertEqual(test.italic, Text.Italic.off)
        self.assertEqual(test.bold, Text.Bold.off)
        self.assertEqual(test.hjustify, Text.HJustify.left)
        self.assertEqual(test.vjustify, Text.VJustify.top)

    def test_from_str_new_format_4(self):
        """Test from_str function with Text example 4 (new format)"""

        test = from_str('T 450 10 20 50 0 0 1 "Test" Normal 0 R B')
        self.assertIsInstance(test, Text)
        self.assertEqual(test.x, 10)
        self.assertEqual(test.y, 20)
        self.assertEqual(test.value, 'Test')
        self.assertEqual(test.size, 50)
        self.assertEqual(test.angle, 45.0)
        self.assertEqual(test.unit, 0)
        self.assertEqual(test.representation, Text.Representation.normal)
        self.assertEqual(test.italic, Text.Italic.off)
        self.assertEqual(test.bold, Text.Bold.off)
        self.assertEqual(test.hjustify, Text.HJustify.right)
        self.assertEqual(test.vjustify, Text.VJustify.bottom)

    def test_from_str_new_format_5(self):
        """Test from_str function with Text example 5 (new format)"""

        test = from_str('T 450 10 20 50 0 0 1 "Test" Italic 1 C C')
        self.assertIsInstance(test, Text)
        self.assertEqual(test.x, 10)
        self.assertEqual(test.y, 20)
        self.assertEqual(test.value, 'Test')
        self.assertEqual(test.size, 50)
        self.assertEqual(test.angle, 45.0)
        self.assertEqual(test.unit, 0)
        self.assertEqual(test.representation, Text.Representation.normal)
        self.assertEqual(test.italic, Text.Italic.on)
        self.assertEqual(test.bold, Text.Bold.on)
        self.assertEqual(test.hjustify, Text.HJustify.center)
        self.assertEqual(test.vjustify, Text.VJustify.center)

    def test_exception(self):
        """Test value exception."""
        with self.assertRaises(ValueError):
            from_str('T')


class TestSymbolElementFromStrPin(unittest.TestCase):
    """Test function from_str for pykicadlib.symbol.elements.Pin"""

    def test_from_str_1(self):
        """Test from_str function with Pin example 1"""

        test = from_str('X TO 1 -200 0 150 R 50 60 1 1 P')
        self.assertIsInstance(test, Pin)
        self.assertEqual(test.x, -200)
        self.assertEqual(test.y, 0)
        self.assertEqual(test.name, 'TO')
        self.assertEqual(test.number, '1')
        self.assertEqual(test.length, 150)
        self.assertEqual(test.direction, Pin.Direction.left)
        self.assertEqual(test.name_size, Symbol.PIN_NAME_SIZE)
        self.assertEqual(test.number_size, Symbol.PIN_NUMBER_SIZE)
        self.assertEqual(test.unit, 1)
        self.assertEqual(test.representation, Pin.Representation.normal)
        self.assertEqual(test.electric, Pin.Electric.passive)
        self.assertEqual(test.shape, Pin.Shape.line)
        self.assertTrue(test.visible)

    def test_from_str_2(self):
        """Test from_str function with Pin example 2"""

        test = from_str('X K 2 200 0 150 L 50 60 1 1 P')
        self.assertIsInstance(test, Pin)
        self.assertEqual(test.x, 200)
        self.assertEqual(test.y, 0)
        self.assertEqual(test.name, 'K')
        self.assertEqual(test.number, '2')
        self.assertEqual(test.length, 150)
        self.assertEqual(test.direction, Pin.Direction.right)
        self.assertEqual(test.name_size, Symbol.PIN_NAME_SIZE)
        self.assertEqual(test.number_size, Symbol.PIN_NUMBER_SIZE)
        self.assertEqual(test.unit, 1)
        self.assertEqual(test.representation, Pin.Representation.normal)
        self.assertEqual(test.electric, Pin.Electric.passive)
        self.assertEqual(test.shape, Pin.Shape.line)
        self.assertTrue(test.visible)

    def test_from_str_3(self):
        """Test from_str function with Pin example 3"""

        test = from_str('X 0 1 0 0 0 R 50 60 1 1 W NC')
        self.assertIsInstance(test, Pin)
        self.assertEqual(test.x, 0)
        self.assertEqual(test.y, 0)
        self.assertEqual(test.name, '0')
        self.assertEqual(test.number, '1')
        self.assertEqual(test.length, 0)
        self.assertEqual(test.direction, Pin.Direction.left)
        self.assertEqual(test.name_size, Symbol.PIN_NAME_SIZE)
        self.assertEqual(test.number_size, Symbol.PIN_NUMBER_SIZE)
        self.assertEqual(test.unit, 1)
        self.assertEqual(test.representation, Pin.Representation.normal)
        self.assertEqual(test.electric, Pin.Electric.power_input)
        self.assertEqual(test.shape, Pin.Shape.clock)
        self.assertFalse(test.visible)

    def test_from_str_4(self):
        """Test from_str function with Pin example 4"""

        test = from_str('X ~ 2 0 -250 200 U 50 60 1 1 P', False)
        self.assertIsInstance(test, Pin)
        self.assertEqual(test.x, 0)
        self.assertEqual(test.y, -250)
        self.assertEqual(test.name, '~')
        self.assertEqual(test.number, '2')
        self.assertEqual(test.length, 200)
        self.assertEqual(test.direction, Pin.Direction.down)
        self.assertEqual(test.name_size, 50)
        self.assertEqual(test.number_size, 60)
        self.assertEqual(test.unit, 1)
        self.assertEqual(test.representation, Pin.Representation.normal)
        self.assertEqual(test.electric, Pin.Electric.passive)
        self.assertEqual(test.shape, Pin.Shape.line)
        self.assertTrue(test.visible)

    def test_exception(self):
        """Test exception"""

        with self.assertRaises(ValueError):
            from_str('X')

        with self.assertRaises(KeyError):
            from_str('Z')
