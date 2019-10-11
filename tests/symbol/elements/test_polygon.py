"""Test KiCAD symbol polygon element.

.. module:: test.symbol.elements
   :synopsis: Symbol elements test

.. moduleauthor:: Benjamin Füldner <benjamin@fueldner.net>
"""

import unittest
from pykicadlib.config import Symbol
from pykicadlib.symbol.elements.polygon import Polygon


class TestSymbolElementPolygon(unittest.TestCase):
    """Test class pykicadlib.symbol.elements.Polygon."""

    def setUp(self):
        """Set-up element."""
        self.element = Polygon()
        self.element.add(Polygon.Point(-50, 50))
        self.element.add(Polygon.Point(50, 0))
        self.element.add(Polygon.Point(-50, -50))

    def test_attributes(self):
        """Test attributes."""
        self.assertEqual(self.element.thickness, Symbol.ELEMENT_THICKNESS)
        self.assertEqual(self.element.fill, Polygon.Fill.none)
        self.assertEqual(len(self.element.points), 3)

    def test_priority(self):
        """Test priority."""
        self.assertEqual(self.element.priority, 0x10000 * Polygon.order + len(self.element.points))

    def test_bounds(self):
        """Test bounds."""
        self.assertEqual(self.element.bounds, Polygon.Boundary(-50, -50, 50, 50))

    def test_modification(self):
        """Test object modification."""
        self.element.fill = Polygon.Fill.background
        self.element.remove(1)
        self.element.points[0].x = 50
        self.element.points[1].x = 50
        self.assertEqual(str(self.element), 'P 2 0 1 20 50 50 50 -50 f')

    def test_compare(self):
        """Test object compare."""
        self.assertNotEqual(self.element, Polygon())

        test = Polygon()
        test.add(Polygon.Point(-50, -50))
        test.add(Polygon.Point(50, 0))
        test.add(Polygon.Point(-50, 50))
        self.assertNotEqual(self.element, test)

        test = Polygon()
        test.add(Polygon.Point(-50, 50))
        test.add(Polygon.Point(50, 0))
        test.add(Polygon.Point(-50, -50))
        self.assertEqual(self.element, test)

        with self.assertRaises(TypeError):
            self.assertNotEqual(self.element, 123)

    def test_str(self):
        """Test __str__ output."""
        self.assertEqual(str(self.element), 'P 3 0 1 20 -50 50 50 0 -50 -50 N')
