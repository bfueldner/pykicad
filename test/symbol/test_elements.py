# pylint: disable=too-few-public-methods
"""
.. module:: test.symbol.elements
   :synopsis: Symbol elements test

.. moduleauthor:: Benjamin Füldner <benjamin@fueldner.net>
"""
import unittest
import pykicadlib


class TestSymbolElementPinValue(unittest.TestCase):
    """Test function pykicadlib.symbol.elements.pin_value"""

    def test_result(self):
        """Test result calculation"""

        self.assertEqual(pykicadlib.symbol.elements.pin_value('0'), 48)
        self.assertEqual(pykicadlib.symbol.elements.pin_value('9'), 48 + 9)
        self.assertEqual(pykicadlib.symbol.elements.pin_value('A0'), 8320 + 48)
        self.assertEqual(pykicadlib.symbol.elements.pin_value('A1'), 8320 + 48 + 1)

    def test_exception(self):
        """Test exception"""

        with self.assertRaises(ValueError):
            pykicadlib.symbol.elements.pin_value('')

        with self.assertRaises(ValueError):
            pykicadlib.symbol.elements.pin_value('a0')

        with self.assertRaises(ValueError):
            pykicadlib.symbol.elements.pin_value('$0')


class TestSymbolElementField(unittest.TestCase):
    """Test class pykicadlib.symbol.elements.Field"""

    def setUp(self):
        """Setup element"""

        self.element = pykicadlib.symbol.elements.Field(
            pykicadlib.symbol.types.Field.name,
            "Text",
            10,
            20,
            50,
            pykicadlib.symbol.types.Orientation.horizontal,
            pykicadlib.symbol.types.Visibility.visible,
            pykicadlib.symbol.types.HJustify.center,
            pykicadlib.symbol.types.VJustify.center,
            pykicadlib.symbol.types.Style.none
        )

    def test_str(self):
        """Test __str__ output"""

        self.assertEqual(str(self.element), 'F1 "Text" 10 20 50 H V C CNN "Name"')

    def test_modification(self):
        """Test object modification"""

        self.element.x = 100
        self.element.y = 200
        self.element.size = 25
        self.assertEqual(str(self.element), 'F1 "Text" 100 200 25 H V C CNN "Name"')


class TestSymbolElementPoint(unittest.TestCase):
    """Test class pykicadlib.symbol.elements.Point"""

    def setUp(self):
        """Setup element"""

        self.element = pykicadlib.symbol.elements.Point(
            -100,
            100
        )

    def test_str(self):
        """Test __str__ output"""

        self.assertEqual(str(self.element), '-100 100')

    def test_modification(self):
        """Test object modification"""

        self.element.x = 10
        self.element.y = 20
        self.assertEqual(str(self.element), '10 20')

    def test_compare(self):
        """Test object compare"""

        self.assertNotEqual(self.element, pykicadlib.symbol.elements.Point(0, 0))
        self.assertEqual(self.element, pykicadlib.symbol.elements.Point(-100, 100))


class TestSymbolElementPolygon(unittest.TestCase):
    """Test class pykicadlib.symbol.elements.Polygon"""

    def setUp(self):
        """Setup element"""

        self.element = pykicadlib.symbol.elements.Polygon(
            0,
            pykicadlib.symbol.types.Fill.foreground
        )
        self.element.add(pykicadlib.symbol.elements.Point(-50, 50))
        self.element.add(pykicadlib.symbol.elements.Point(50, 0))
        self.element.add(pykicadlib.symbol.elements.Point(-50, -50))

    def test_str(self):
        """Test __str__ output"""

        self.assertEqual(str(self.element), 'P 3 0 1 0 -50 50 50 0 -50 -50 F')

    def test_modification(self):
        """Test object modification"""

        self.element.fill = pykicadlib.symbol.types.Fill.none
        self.element.remove(1)
        self.element.points[0].x = 50
        self.element.points[1].x = 50
        self.assertEqual(str(self.element), 'P 2 0 1 0 50 50 50 -50 N')

    def test_compare(self):
        """Test object compare"""

        self.assertNotEqual(
            self.element,
            pykicadlib.symbol.elements.Polygon(0, pykicadlib.symbol.types.Fill.none))

        test = pykicadlib.symbol.elements.Polygon(0, pykicadlib.symbol.types.Fill.none)
        test.add(pykicadlib.symbol.elements.Point(-50, 50))
        test.add(pykicadlib.symbol.elements.Point(50, 0))
        test.add(pykicadlib.symbol.elements.Point(-50, -50))
        self.assertEqual(self.element, test)


class TestSymbolElementRectangle(unittest.TestCase):
    """Test class pykicadlib.symbol.elements.Rectangle"""

    def setUp(self):
        """Setup element"""

        self.element = pykicadlib.symbol.elements.Rectangle(
            -10,
            -20,
            10,
            20,
            50,
            pykicadlib.symbol.types.Fill.background
        )

    def test_str(self):
        """Test __str__ output"""

        self.assertEqual(str(self.element), 'S -10 -20 10 20 0 1 50 f')

    def test_modification(self):
        """Test object modification"""

        self.element.x1 = 0
        self.element.y2 = 40
        self.element.fill = pykicadlib.symbol.types.Fill.foreground
        self.assertEqual(str(self.element), 'S 0 -20 10 40 0 1 50 F')

    def test_compare(self):
        """Test object compare"""

        self.assertNotEqual(
            self.element,
            pykicadlib.symbol.elements.Rectangle(0, 0, 0, 0, 0, pykicadlib.symbol.types.Fill.none))
        self.assertEqual(
            self.element,
            pykicadlib.symbol.elements.Rectangle(
                -10, -20, 10, 20, 50, pykicadlib.symbol.types.Fill.none))


class TestSymbolElementCircle(unittest.TestCase):
    """Test class pykicadlib.symbol.elements.Circle"""

    def setUp(self):
        """Setup element"""

        self.element = pykicadlib.symbol.elements.Circle(
            0,
            0,
            70,
            0,
            pykicadlib.symbol.types.Fill.foreground
        )

    def test_str(self):
        """Test __str__ output"""

        self.assertEqual(str(self.element), 'C 0 0 70 0 1 0 F')

    def test_modification(self):
        """Test object modification"""

        self.element.radius = 20
        self.element.fill = pykicadlib.symbol.types.Fill.none
        self.assertEqual(str(self.element), 'C 0 0 20 0 1 0 N')

    def test_compare(self):
        """Test object compare"""

        self.assertNotEqual(
            self.element,
            pykicadlib.symbol.elements.Circle(0, 0, 0, 0, pykicadlib.symbol.types.Fill.none))
        self.assertEqual(
            self.element,
            pykicadlib.symbol.elements.Circle(0, 0, 70, 0, pykicadlib.symbol.types.Fill.none))


class TestSymbolElementArc(unittest.TestCase):
    """Test class pykicadlib.symbol.elements.Arc"""

    def setUp(self):
        """Setup element"""

        self.element = pykicadlib.symbol.elements.Arc(
            -1,
            -200,
            -50,
            -200,
            0,
            -150,
            90.0,
            -1.1,
            49,
            0,
            pykicadlib.symbol.types.Fill.none
        )

    def test_str(self):
        """Test __str__ output"""

        self.assertEqual(str(self.element), 'A -1 -200 49 900 -11 0 1 0 N -50 -200 0 -150')

    def test_modification(self):
        """Test object modification"""

        self.element.x = 0
        self.element.y = -199
        self.element.start_angle = 0.0
        self.element.end_angle = -91.1
        self.element.start_x = 0
        self.element.start_y = -150
        self.element.end_x = 50
        self.element.end_y = -200
        self.assertEqual(str(self.element), 'A 0 -199 49 0 -911 0 1 0 N 0 -150 50 -200')

    def test_compare(self):
        """Test object compare"""

        self.assertNotEqual(
            self.element,
            pykicadlib.symbol.elements.Arc(
                0, 0, 0, 0, 0, 0, 0.0, 0.0, 0, 0, pykicadlib.symbol.types.Fill.none))
        self.assertEqual(
            self.element,
            pykicadlib.symbol.elements.Arc(
                -1, -200, -50, -200, 0, -150, 90.0, -1.1, 49, 0, pykicadlib.symbol.types.Fill.none))


class TestSymbolElementText(unittest.TestCase):
    """Test class pykicadlib.symbol.elements.Text"""

    def setUp(self):
        """Setup element"""

        self.element = pykicadlib.symbol.elements.Text(
            200,
            100,
            'Text with space',
            50,
            0.0
        )

    def test_str(self):
        """Test __str__ output"""

        self.assertEqual(str(self.element), 'T 0 200 100 50 0 0 1 "Text with space" Normal 0 C C')

    def test_modification(self):
        """Test object modification"""

        self.element.value = 'A"B'
        self.element.angle = 45.0
        self.element.x = 10
        self.element.y = 20
        self.assertEqual(str(self.element), 'T 450 10 20 50 0 0 1 "A\'\'B" Normal 0 C C')

        self.element.value = 'Test'
        self.element.hjustify = pykicadlib.symbol.types.HJustify.left
        self.element.vjustify = pykicadlib.symbol.types.VJustify.top
        self.assertEqual(str(self.element), 'T 450 10 20 50 0 0 1 "Test" Normal 0 L T')

        self.element.hjustify = pykicadlib.symbol.types.HJustify.right
        self.element.vjustify = pykicadlib.symbol.types.VJustify.bottom
        self.assertEqual(str(self.element), 'T 450 10 20 50 0 0 1 "Test" Normal 0 R B')

        self.element.bold = pykicadlib.symbol.types.Bold.on
        self.element.italic = pykicadlib.symbol.types.Italic.on
        self.assertEqual(str(self.element), 'T 450 10 20 50 0 0 1 "Test" Italic 1 R B')

    def test_compare(self):
        """Test object compare"""

        self.assertNotEqual(self.element, pykicadlib.symbol.elements.Text(0, 0, "", 0, 0.0))
        self.assertEqual(
            self.element,
            pykicadlib.symbol.elements.Text(
                200, 100, "Text with space", 50, 45.0, 0,
                pykicadlib.symbol.types.Representation.normal,
                pykicadlib.symbol.types.Bold.on,
                pykicadlib.symbol.types.Italic.on,
                pykicadlib.symbol.types.HJustify.right,
                pykicadlib.symbol.types.VJustify.bottom))


class TestSymbolElementPin(unittest.TestCase):
    """Test class pykicadlib.symbol.elements.Pin"""

    def setUp(self):
        """Setup element"""

        self.element = pykicadlib.symbol.elements.Pin(
            -200,
            0,
            'TO',
            '1',
            150,
            pykicadlib.symbol.types.Direction.left,
            40,
            40
        )

    def test_str(self):
        """Test __str__ output"""

        self.assertEqual(str(self.element), 'X TO 1 -200 0 150 R 40 40 0 1 I')

    def test_modification(self):
        """Test object modification"""

        self.element.electric = pykicadlib.symbol.types.Electric.passive
        self.element.shape = pykicadlib.symbol.types.Shape.line
        self.element.unit = 1
        self.assertEqual(str(self.element), 'X TO 1 -200 0 150 R 40 40 1 1 P')

        self.element.visible = False
        self.assertEqual(str(self.element), 'X TO 1 -200 0 150 R 40 40 1 1 P N')

        self.element.shape = pykicadlib.symbol.types.Shape.clock
        self.assertEqual(str(self.element), 'X TO 1 -200 0 150 R 40 40 1 1 P NC')

    def test_compare(self):
        """Test object compare"""

        self.assertNotEqual(
            self.element,
            pykicadlib.symbol.elements.Pin(
                -200, 0, 'TO', '1', 150, pykicadlib.symbol.types.Direction.left, 40, 40))
