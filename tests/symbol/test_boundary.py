"""Test KiCAD symbol base element.

.. module:: test.symbol.elements
   :synopsis: Symbol elements test

.. moduleauthor:: Benjamin Füldner <benjamin@fueldner.net>
"""

import unittest
from pykicadlib.symbol.boundary import Boundary


class TestSymbolBoundary(unittest.TestCase):
    """Test class pykicadlib.symbol.elements.Boundary."""

    def setUp(self):
        """Set-up boundary."""
        self.boundary = Boundary(-10, -20, 10, 20)

    def test_attributes(self):
        """Test attributes."""
        self.assertEqual(self.boundary.x1, -10)
        self.assertEqual(self.boundary.y1, -20)
        self.assertEqual(self.boundary.x2, 10)
        self.assertEqual(self.boundary.y2, 20)

    def test_add(self):
        """Test add."""
        self.boundary += Boundary(-20, -10, 20, 10)
        self.assertEqual(self.boundary, Boundary(-20, -20, 20, 20))

        with self.assertRaises(TypeError):
            self.boundary += 'something'

    def test_eq(self):
        """Test equal."""
        self.assertEqual(self.boundary, Boundary(-10, -20, 10, 20))
        self.assertNotEqual(self.boundary, Boundary(-20, -10, 20, 10))

        with self.assertRaises(TypeError):
            self.assertNotEqual(self.boundary, 123)
