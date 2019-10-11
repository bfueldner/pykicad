"""Test KiCAD symbol rectangle element.

.. module:: test.symbol.elements.rectangle
   :synopsis: Symbol rectangle element test

.. moduleauthor:: Benjamin Füldner <benjamin@fueldner.net>
"""

import unittest
from pykicadlib.config import Symbol
from pykicadlib.symbol.elements.rectangle import Rectangle


class TestSymbolElementRectangle(unittest.TestCase):
    """Test class pykicadlib.symbol.elements.Rectangle."""

    def setUp(self):
        """Set-up element."""
        self.element = Rectangle(-10, -20, 10, 20)

    def test_attributes(self):
        """Test attributes."""
        self.assertEqual(self.element.x1, -10)
        self.assertEqual(self.element.y1, -20)
        self.assertEqual(self.element.x2, 10)
        self.assertEqual(self.element.y2, 20)
        self.assertEqual(self.element.thickness, Symbol.ELEMENT_THICKNESS)
        self.assertEqual(self.element.fill, Rectangle.Fill.none)

    def test_priority(self):
        """Test priority."""
        self.assertEqual(self.element.priority, 0x10000 * Rectangle.order)

    def test_bounds(self):
        """Test bounds."""
        self.assertEqual(self.element.bounds, Rectangle.Boundary(-10, -20, 10, 20))

    def test_modification(self):
        """Test object modification."""
        self.element.x1 = 0
        self.element.y2 = 40
        self.element.thickness = 50
        self.element.fill = Rectangle.Fill.foreground
        self.assertEqual(str(self.element), 'S 0 -20 10 40 0 1 50 F')

    def test_compare(self):
        """Test object compare."""
        self.assertNotEqual(self.element, Rectangle(0, 0, 0, 0))
        self.assertEqual(self.element, Rectangle(10, 20, -10, -20))

        with self.assertRaises(TypeError):
            self.assertNotEqual(self.element, 123)

    def test_str(self):
        """Test __str__ output."""
        self.assertEqual(str(self.element), 'S -10 -20 10 20 0 1 20 N')
