"""Test KiCAD symbol element point.

.. module:: test.symbol.element.point
   :synopsis: Symbol element point test

.. moduleauthor:: Benjamin Füldner <benjamin@fueldner.net>
"""

import unittest
from pykicadlib.symbol.elements.point import Point


class TestSymbolElementPoint(unittest.TestCase):
    """Test class pykicadlib.symbol.elements.Point."""

    def setUp(self):
        """Set-up element."""
        self.element = Point(-100, 100)

    def test_attributes(self):
        """Test attributes."""
        self.assertEqual(self.element.x, -100)
        self.assertEqual(self.element.y, 100)

    def test_modification(self):
        """Test object modification."""
        self.element.x = 10
        self.element.y = 20
        self.assertEqual(str(self.element), '10 20')

    def test_compare(self):
        """Test object compare."""
        self.assertNotEqual(self.element, Point(0, 0))
        self.assertEqual(self.element, Point(-100, 100))

        with self.assertRaises(TypeError):
            self.assertNotEqual(self.element, 123)

    def test_str(self):
        """Test __str__ output."""
        self.assertEqual(str(self.element), '-100 100')
