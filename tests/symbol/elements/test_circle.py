"""Test KiCAD symbol circle element.

.. module:: test.symbol.elements.circle
   :synopsis: Symbol circle element test

.. moduleauthor:: Benjamin Füldner <benjamin@fueldner.net>
"""

import unittest
from pykicadlib.config import Symbol
from pykicadlib.symbol.elements.circle import Circle


class TestSymbolElementCircle(unittest.TestCase):
    """Test class pykicadlib.symbol.elements.Circle."""

    def setUp(self):
        """Set-up element."""
        self.element = Circle(0, 0, 70)

    def test_attributes(self):
        """Test attributes."""
        self.assertEqual(self.element.x, 0)
        self.assertEqual(self.element.y, 0)
        self.assertEqual(self.element.radius, 70)
        self.assertEqual(self.element.thickness, Symbol.ELEMENT_THICKNESS)
        self.assertEqual(self.element.fill, Circle.Fill.none)

    def test_priority(self):
        """Test priority."""
        self.assertEqual(self.element.priority, 0x10000 * Circle.order)

    def test_bounds(self):
        """Test bounds."""
        self.assertEqual(self.element.bounds, Circle.Boundary(-70, -70, 70, 70))

    def test_modification(self):
        """Test object modification."""
        self.element.radius = 20
        self.element.fill = Circle.Fill.foreground
        self.assertEqual(str(self.element), 'C 0 0 20 0 1 20 F')

    def test_compare(self):
        """Test object compare."""
        self.assertNotEqual(self.element, Circle(0, 0, 0))
        self.assertEqual(self.element, Circle(0, 0, 70))

        with self.assertRaises(TypeError):
            self.assertNotEqual(self.element, 123)

    def test_str(self):
        """Test __str__ output."""
        self.assertEqual(str(self.element), 'C 0 0 70 0 1 20 N')
