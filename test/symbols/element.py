import unittest

import kicad.symbols.element

class case(unittest.TestCase):

    def test_symbols_element_pin_value(self):
        self.assertEqual(kicad.symbols.element.pin_value('0'), 48)
        self.assertEqual(kicad.symbols.element.pin_value('9'), 48 + 9)
        self.assertEqual(kicad.symbols.element.pin_value('A0'), 8320 + 48)
        self.assertEqual(kicad.symbols.element.pin_value('A1'), 8320 + 48 + 1)

        with self.assertRaises(ValueError):
            kicad.symbols.element.pin_value('')

        with self.assertRaises(ValueError):
            kicad.symbols.element.pin_value('a0')

        with self.assertRaises(ValueError):
            kicad.symbols.element.pin_value('$0')

    def test_symbols_element_field(self):
        test = kicad.symbols.element.field(
            kicad.symbols.type.field.name,
            "Text",
            10,
            20,
            50,
            kicad.symbols.type.orientation.horizontal,
            kicad.symbols.type.visibility.visible,
            kicad.symbols.type.hjustify.center,
            kicad.symbols.type.vjustify.center,
            kicad.symbols.type.style.none
        )
        self.assertEqual(str(test), 'F1 "Text" 10 20 50 H V C CNN "Name"')

        test.x = 100
        test.y = 200
        test.size = 25
        self.assertEqual(str(test), 'F1 "Text" 100 200 25 H V C CNN "Name"')

    def test_symbols_element_point(self):
        test = kicad.symbols.element.point(
            -100,
            100
        )
        self.assertEqual(str(test), '-100 100')

        test.x = 10
        test.y = 20
        self.assertEqual(str(test), '10 20')

        self.assertFalse(test == int)
        self.assertFalse(test == kicad.symbols.element.point(0, 0))
        self.assertTrue(test == kicad.symbols.element.point(10, 20))

    def test_symbols_element_polygon(self):
        test = kicad.symbols.element.polygon(
            0,
            kicad.symbols.type.fill.foreground
        )
        test.add(kicad.symbols.element.point(-50, 50))
        test.add(kicad.symbols.element.point(50, 0))
        test.add(kicad.symbols.element.point(-50, -50))
        self.assertEqual(str(test), 'P 3 0 1 0 -50 50 50 0 -50 -50 F')

        test.fill = kicad.symbols.type.fill.none
        test.remove(1)
        test.points[0].x = 50
        test.points[1].x = 50
        self.assertEqual(str(test), 'P 2 0 1 0 50 50 50 -50 N')

        self.assertFalse(test == int)
        self.assertFalse(test == kicad.symbols.element.polygon(0, kicad.symbols.type.fill.none))

        test2 = kicad.symbols.element.polygon(0, kicad.symbols.type.fill.none)
        test2.add(kicad.symbols.element.point(50, 50))
        test2.add(kicad.symbols.element.point(50, -50))
        self.assertTrue(test == test2)

    def test_symbols_element_rectangle(self):
        test = kicad.symbols.element.rectangle(
            -10,
            -20,
            10,
            20,
            50,
            kicad.symbols.type.fill.background
        )
        self.assertEqual(str(test), 'S -10 -20 10 20 0 1 50 f')

        self.assertFalse(test == int)
        self.assertFalse(test == kicad.symbols.element.rectangle(0, 0, 0, 0, 0, kicad.symbols.type.fill.none))
        self.assertTrue(test == kicad.symbols.element.rectangle(-10, -20, 10, 20, 50, kicad.symbols.type.fill.none))

    def test_symbols_element_circle(self):
        test = kicad.symbols.element.circle(
            0,
            0,
            70,
            0,
            kicad.symbols.type.fill.foreground
        )
        self.assertEqual(str(test), 'C 0 0 70 0 1 0 F')

        test.radius = 20
        test.fill = kicad.symbols.type.fill.none
        self.assertEqual(str(test), 'C 0 0 20 0 1 0 N')

        self.assertFalse(test == int)
        self.assertFalse(test == kicad.symbols.element.circle(0, 0, 0, 0, kicad.symbols.type.fill.none))
        self.assertTrue(test == kicad.symbols.element.circle(0, 0, 20, 0, kicad.symbols.type.fill.none))

    def test_symbols_element_arc(self):
        test = kicad.symbols.element.arc(
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
            kicad.symbols.type.fill.none
        )
        self.assertEqual(str(test), 'A -1 -200 49 900 -11 0 1 0 N -50 -200 0 -150')

        test.x = 0
        test.y = -199
        test.startAngle = 0.0
        test.endAngle = -91.1
        test.startX = 0
        test.startY = -150
        test.endX = 50
        test.endY = -200
        self.assertEqual(str(test), 'A 0 -199 49 0 -911 0 1 0 N 0 -150 50 -200')

        self.assertFalse(test == int)
        self.assertFalse(test == kicad.symbols.element.arc(0, 0, 0, 0, 0, 0, 0.0, 0.0, 0, 0, kicad.symbols.type.fill.none))
        self.assertTrue(test == kicad.symbols.element.arc(0, -199, 0, -150, 50, -200, 0.0, -91.1, 49, 0, kicad.symbols.type.fill.none))

    def test_symbols_element_text(self):
        test = kicad.symbols.element.text(
            200,
            100,
            'Text with space',
            50,
            0.0
        )
        self.assertEqual(str(test), 'T 0 200 100 50 0 0 1 "Text with space" Normal 0 C C')

        test.value = 'A"B'
        test.angle = 45.0
        test.x = 10
        test.y = 20
        self.assertEqual(str(test), 'T 450 10 20 50 0 0 1 "A\'\'B" Normal 0 C C')

        test.value = 'Test'
        test.hjustify = kicad.symbols.type.hjustify.left
        test.vjustify = kicad.symbols.type.vjustify.top
        self.assertEqual(str(test), 'T 450 10 20 50 0 0 1 "Test" Normal 0 L T')

        test.hjustify = kicad.symbols.type.hjustify.right
        test.vjustify = kicad.symbols.type.vjustify.bottom
        self.assertEqual(str(test), 'T 450 10 20 50 0 0 1 "Test" Normal 0 R B')

        test.bold = kicad.symbols.type.bold.on
        test.italic = kicad.symbols.type.italic.on
        self.assertEqual(str(test), 'T 450 10 20 50 0 0 1 "Test" Italic 1 R B')

        self.assertFalse(test == int)
        self.assertFalse(test == kicad.symbols.element.text(0, 0, "", 0, 0.0))
        self.assertTrue(test == kicad.symbols.element.text(10, 20, "Test", 50, 45.0, 0, kicad.symbols.type.representation.normal, kicad.symbols.type.bold.on, kicad.symbols.type.italic.on, kicad.symbols.type.hjustify.right, kicad.symbols.type.vjustify.bottom))

    def test_symbols_element_pin(self):
        test = kicad.symbols.element.pin(
            -200,
            0,
            'TO',
            '1',
            150,
            kicad.symbols.type.direction.left,
            40,
            40
        )
        self.assertEqual(str(test), 'X TO 1 -200 0 150 R 40 40 0 1 I')

        test = kicad.symbols.element.pin(
            -200,
            0,
            'TO',
            '1',
            150,
            kicad.symbols.type.direction.left,
            40,
            40,
            kicad.symbols.type.electric.passive,
            kicad.symbols.type.shape.line,
            True,
            1
        )
        self.assertEqual(str(test), 'X TO 1 -200 0 150 R 40 40 1 1 P')

        test.visible = False
        self.assertEqual(str(test), 'X TO 1 -200 0 150 R 40 40 1 1 P N')

        test.shape = kicad.symbols.type.shape.clock
        self.assertEqual(str(test), 'X TO 1 -200 0 150 R 40 40 1 1 P NC')

        self.assertFalse(test == int)
        self.assertFalse(test == kicad.symbols.element.pin(0, 0, 'A', '1', 150, kicad.symbols.type.direction.left, 40, 40))
