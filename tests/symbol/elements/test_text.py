"""Test KiCAD symbol text element.

.. module:: test.symbol.elements
   :synopsis: Symbol elements test

.. moduleauthor:: Benjamin Füldner <benjamin@fueldner.net>
"""

import unittest
from pykicadlib.symbol.elements.text import Text


class TestSymbolElementText(unittest.TestCase):
    """Test class pykicadlib.symbol.elements.Text."""

    def setUp(self):
        """Set-up element."""
        self.element = Text(200, 100, 'Text with space', 50)

    def test_attributes(self):
        """Test attributes."""
        self.assertEqual(self.element.x, 200)
        self.assertEqual(self.element.y, 100)
        self.assertEqual(self.element.value, 'Text with space')
        self.assertEqual(self.element.size, 50)
        self.assertEqual(self.element.angle, 0)
        self.assertEqual(self.element.italic, Text.Italic.off)
        self.assertEqual(self.element.bold, Text.Bold.off)
        self.assertEqual(self.element.hjustify, Text.HJustify.center)
        self.assertEqual(self.element.vjustify, Text.VJustify.center)

    def test_priority(self):
        """Test priority."""
        self.assertEqual(self.element.priority, 0x10000 * Text.order)

    def test_bounds(self):
        """Test bounds."""
        self.assertEqual(self.element.bounds, Text.Boundary(200, 100, 200, 100))

    def test_modification(self):
        """Test object modification."""
        self.element.value = 'A"B'
        self.element.angle = 45.0
        self.element.x = 10
        self.element.y = 20
        self.assertEqual(str(self.element), 'T 450 10 20 50 0 0 1 "A\'\'B" Normal 0 C C')

        self.element.value = 'Test'
        self.element.hjustify = Text.HJustify.left
        self.element.vjustify = Text.VJustify.top
        self.assertEqual(str(self.element), 'T 450 10 20 50 0 0 1 "Test" Normal 0 L T')

        self.element.hjustify = Text.HJustify.right
        self.element.vjustify = Text.VJustify.bottom
        self.assertEqual(str(self.element), 'T 450 10 20 50 0 0 1 "Test" Normal 0 R B')

        self.element.bold = Text.Bold.on
        self.element.italic = Text.Italic.on
        self.assertEqual(str(self.element), 'T 450 10 20 50 0 0 1 "Test" Italic 1 R B')

    def test_compare(self):
        """Test object compare."""
        self.assertNotEqual(self.element, Text(0, 0, "", 0))
        self.assertEqual(self.element, Text(200, 100, "Text with space", 50))

        with self.assertRaises(TypeError):
            self.assertNotEqual(self.element, 123)

    def test_str(self):
        """Test __str__ output."""
        self.assertEqual(str(self.element), 'T 0 200 100 50 0 0 1 "Text with space" Normal 0 C C')
