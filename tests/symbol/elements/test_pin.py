"""Test KiCAD symbol pin element.

.. module:: test.symbol.elements
   :synopsis: Symbol elements test

.. moduleauthor:: Benjamin Füldner <benjamin@fueldner.net>
"""

import unittest
from pykicadlib.config import Symbol
from pykicadlib.symbol.elements.pin import Pin, _pin_value


class TestSymbolElementPinValue(unittest.TestCase):
    """Test function pykicadlib.symbol.elements.pin._pin_value."""

    def test_result(self):
        """Test result calculation."""
        self.assertEqual(_pin_value('0'), 48)
        self.assertEqual(_pin_value('9'), 48 + 9)
        self.assertEqual(_pin_value('A0'), 8320 + 48)
        self.assertEqual(_pin_value('A1'), 8320 + 48 + 1)

    def test_exception(self):
        """Test exception."""
        with self.assertRaises(ValueError):
            _pin_value('')

        with self.assertRaises(ValueError):
            _pin_value('a0')

        with self.assertRaises(ValueError):
            _pin_value('$0')


class TestSymbolElementPin(unittest.TestCase):
    """Test class pykicadlib.symbol.elements.pin.Pin."""

    def setUp(self):
        """Set-up element."""
        self.element = Pin(-200, 0, 'TO', '1')

    def test_attributes(self):
        """Test attributes."""
        self.assertEqual(self.element.x, -200)
        self.assertEqual(self.element.y, 0)
        self.assertEqual(self.element.name, 'TO')
        self.assertEqual(self.element.number, '1')
        self.assertEqual(self.element.length, Symbol.PIN_LENGTH)
        self.assertEqual(self.element.direction, Pin.Direction.down)
        self.assertEqual(self.element.name_size, Symbol.PIN_NAME_SIZE)
        self.assertEqual(self.element.number_size, Symbol.PIN_NUMBER_SIZE)
        self.assertEqual(self.element.electric, Pin.Electric.input)
        self.assertEqual(self.element.shape, Pin.Shape.line)
        self.assertTrue(self.element.visible)

    def test_priority(self):
        """Test priority."""
        self.assertEqual(self.element.priority, 0x10000 * Pin.order + ord('1'))

    def test_bounds(self):
        """Test bounds."""
        self.assertEqual(self.element.bounds, Pin.Boundary(-200, 0, -200, Symbol.PIN_LENGTH))

        self.element.direction = Pin.Direction.up
        self.assertEqual(self.element.bounds, Pin.Boundary(-200, -Symbol.PIN_LENGTH, -200, 0))

        self.element.direction = Pin.Direction.left
        self.assertEqual(self.element.bounds, Pin.Boundary(-200 - Symbol.PIN_LENGTH, 0, -200, 0))

        self.element.direction = Pin.Direction.right
        self.assertEqual(self.element.bounds, Pin.Boundary(-200, 0, -200 + Symbol.PIN_LENGTH, 0))

    def test_modification(self):
        """Test object modification."""
        self.element.electric = Pin.Electric.passive
        self.element.shape = Pin.Shape.line
        self.element.unit = 1
        self.assertEqual(str(self.element), 'X TO 1 -200 0 100 U 40 40 1 1 P')

        self.element.visible = False
        self.assertEqual(str(self.element), 'X TO 1 -200 0 100 U 40 40 1 1 P N')

        self.element.shape = Pin.Shape.clock
        self.assertEqual(str(self.element), 'X TO 1 -200 0 100 U 40 40 1 1 P NC')

    def test_compare(self):
        """Test object compare."""
        self.assertNotEqual(self.element, Pin(-200, 0, 'TO', '1'))

        with self.assertRaises(TypeError):
            self.assertNotEqual(self.element, 123)

    def test_str(self):
        """Test __str__ output."""
        self.assertEqual(str(self.element), 'X TO 1 -200 0 100 U 40 40 0 1 I')
