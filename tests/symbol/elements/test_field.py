# pylint: disable=too-few-public-methods
"""Test KiCAD symbol elements.

.. module:: test.symbol.elements
   :synopsis: Symbol elements test

.. moduleauthor:: Benjamin Füldner <benjamin@fueldner.net>
"""

import unittest
from pykicadlib.config import Symbol
from pykicadlib.symbol.elements.field import Field


class TestSymbolElementField(unittest.TestCase):
    """Test class pykicadlib.symbol.elements.Field."""

    def setUp(self):
        """Set-up element."""
        self.element = Field(Field.Type.name, 10, 20, "Text")

    def test_attributes(self):
        """Test attributes."""
        self.assertEqual(self.element.type, Field.Type.name)
        self.assertEqual(self.element.x, 10)
        self.assertEqual(self.element.y, 20)
        self.assertEqual(self.element.value, 'Text')
        self.assertEqual(self.element.size, Symbol.FIELD_TEXT_SIZE)
        self.assertEqual(self.element.orientation, Field.Orientation.horizontal)
        self.assertEqual(self.element.visibility, Field.Visibility.visible)
        self.assertEqual(self.element.hjustify, Field.HJustify.left)
        self.assertEqual(self.element.vjustify, Field.VJustify.center)
        self.assertEqual(self.element.style, Field.Style.none)

    def test_modification(self):
        """Test object modification."""
        self.element.x = 100
        self.element.y = 200
        self.element.size = 25
        self.assertEqual(str(self.element), 'F1 "Text" 100 200 25 H V L CNN "Name"')

    def test_str(self):
        """Test __str__ output."""
        self.assertEqual(str(self.element), 'F1 "Text" 10 20 60 H V L CNN "Name"')
