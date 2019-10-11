"""Test KiCAD symbol arc element.

.. module:: test.symbol.elements
   :synopsis: Symbol elements test

.. moduleauthor:: Benjamin Füldner <benjamin@fueldner.net>
"""

import unittest
from pykicadlib.config import Symbol
from pykicadlib.symbol.elements.arc import Arc


class TestSymbolElementArc(unittest.TestCase):
    """Test class pykicadlib.symbol.elements.Arc."""

    def setUp(self):
        """Set-up element."""
        self.element = Arc(
            -1,
            -200,
            49,
            -50,
            -200,
            0,
            -150,
            90.0,
            -1.1,
        )

    def test_attributes(self):
        """Test attributes."""
        self.assertEqual(self.element.x, -1)
        self.assertEqual(self.element.y, -200)
        self.assertEqual(self.element.radius, 49)
        self.assertEqual(self.element.thickness, Symbol.ELEMENT_THICKNESS)
        self.assertEqual(self.element.fill, Arc.Fill.none)

    def test_priority(self):
        """Test priority."""
        self.assertEqual(self.element.priority, 0x10000 * Arc.order)

    def test_bounds(self):
        """Test bounds."""
        self.assertEqual(self.element.bounds, Arc.Boundary(-50, -249, 48, -151))

    def test_modification(self):
        """Test object modification."""
        self.element.x = 0
        self.element.y = -199
        self.element.start_angle = 0.0
        self.element.end_angle = -91.1
        self.element.start_x = 0
        self.element.start_y = -150
        self.element.end_x = 50
        self.element.end_y = -200
        self.assertEqual(str(self.element), 'A 0 -199 49 0 -911 0 1 20 N 0 -150 50 -200')

    def test_compare(self):
        """Test object compare."""
        self.assertNotEqual(self.element, Arc(0, 0, 0, 0, 0, 0, 0.0, 0.0, 0))
        self.assertEqual(self.element, Arc(-1, -200, 49, -50, -200, 0, -150, 90.0, -1.1))

        with self.assertRaises(TypeError):
            self.assertNotEqual(self.element, 123)

    def test_str(self):
        """Test __str__ output."""
        self.assertEqual(str(self.element), 'A -1 -200 49 900 -11 0 1 20 N -50 -200 0 -150')
