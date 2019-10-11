"""Test KiCAD symbol base element.

.. module:: test.symbol.elements
   :synopsis: Symbol elements test

.. moduleauthor:: Benjamin Füldner <benjamin@fueldner.net>
"""

import unittest
from pykicadlib.symbol.element import Element


class TestSymbolElement(unittest.TestCase):
    """Test class pykicadlib.symbol.elements.Element."""

    def setUp(self):
        """Set-up element."""
        self.element = Element()

    def test_attributes(self):
        """Test attributes."""
        self.assertEqual(self.element.unit, 0)
        self.assertEqual(self.element.representation, Element.Representation.normal)
        self.assertEqual(self.element.order, 0)

    def test_priority(self):
        """Test priority."""
        self.assertEqual(self.element.priority, 0)

    def test_bounds(self):
        """Test boundary."""
        self.assertEqual(self.element.bounds, Element.Boundary(0, 0, 0, 0))
