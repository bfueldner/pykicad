"""Test KiCAD symbol types.

.. module:: test.symbol.types
   :synopsis: Symbol types test

.. moduleauthor:: Benjamin Füldner <benjamin@fueldner.net>
"""

import unittest

from pykicadlib.symbol.types import Flag, Visible, Units
from pykicadlib.symbol.types import Field, Fill, HJustify, Orientation, \
    Representation, Style, Visibility, VJustify
from pykicadlib.symbol.types import Direction, Electric, Shape
from pykicadlib.symbol.types import Bold, Italic


# Symbol

class TestSymbolTypeFlag(unittest.TestCase):
    """Test class pykicadlib.symbol.types.Flag."""

    def test_from_str(self):
        """Test classmethod from_str."""
        self.assertEqual(Flag.from_str('N'), Flag.normal)
        self.assertEqual(Flag.from_str('P'), Flag.power)

    def test_str(self):
        """Test __str__ output."""
        self.assertEqual(str(Flag.normal), 'N')
        self.assertEqual(str(Flag.power), 'P')

    def test_exception(self):
        """Test exception."""
        with self.assertRaises(NotImplementedError):
            Flag.from_str('')


class TestSymbolTypeVisible(unittest.TestCase):
    """Test class pykicadlib.symbol.types.Visible."""

    def test_from_str(self):
        """Test classmethod from_str."""
        self.assertEqual(Visible.from_str('N'), Visible.no)
        self.assertEqual(Visible.from_str('Y'), Visible.yes)

    def test_str(self):
        """Test __str__ output."""
        self.assertEqual(str(Visible.no), 'N')
        self.assertEqual(str(Visible.yes), 'Y')

    def test_exception(self):
        """Test exception."""
        with self.assertRaises(NotImplementedError):
            Visible.from_str('')


class TestSymbolTypeUnits(unittest.TestCase):
    """Test class pykicadlib.symbol.types.Units."""

    def test_from_str(self):
        """Test classmethod from_str."""
        self.assertEqual(Units.from_str('L'), Units.locked)
        self.assertEqual(Units.from_str('F'), Units.swappable)

    def test_str(self):
        """Test __str__ output."""
        self.assertEqual(str(Units.locked), 'L')
        self.assertEqual(str(Units.swappable), 'F')

    def test_exception(self):
        """Test exception."""
        with self.assertRaises(NotImplementedError):
            Units.from_str('')


# Element

class TestSymbolTypeField(unittest.TestCase):
    """Test class pykicadlib.symbol.types.Field."""

    def test_from_str(self):
        """Test classmethod from_str."""
        self.assertEqual(Field.from_str('0'), Field.reference)
        self.assertEqual(Field.from_str('1'), Field.name)
        self.assertEqual(Field.from_str('2'), Field.footprint)
        self.assertEqual(Field.from_str('3'), Field.document)
        self.assertEqual(Field.from_str('4'), Field.manufacturer)
        self.assertEqual(Field.from_str('5'), Field.value)
        self.assertEqual(Field.from_str('6'), Field.tolerance)
        self.assertEqual(Field.from_str('7'), Field.temperature)
        self.assertEqual(Field.from_str('8'), Field.model)
        self.assertEqual(Field.from_str('9'), Field.voltage)
        self.assertEqual(Field.from_str('10'), Field.power)

    def test_str(self):
        """Test __str__ output."""
        self.assertEqual(str(Field.reference), 'Reference')
        self.assertEqual(str(Field.name), 'Name')
        self.assertEqual(str(Field.footprint), 'Footprint')
        self.assertEqual(str(Field.document), 'Document')
        self.assertEqual(str(Field.manufacturer), 'Manufacturer')
        self.assertEqual(str(Field.value), 'Value')
        self.assertEqual(str(Field.tolerance), 'Tolerance')
        self.assertEqual(str(Field.temperature), 'Temperature')
        self.assertEqual(str(Field.model), 'Model')
        self.assertEqual(str(Field.voltage), 'Voltage')
        self.assertEqual(str(Field.power), 'Power')

    def test_exception(self):
        """Test exception."""
        with self.assertRaises(ValueError):
            Field.from_str('')

        with self.assertRaises(ValueError):
            Field.from_str('A')

        with self.assertRaises(NotImplementedError):
            Field.from_str('11')


class TestSymbolTypeFill(unittest.TestCase):
    """Test class pykicadlib.symbol.types.Fill."""

    def test_from_str(self):
        """Test classmethod from_str."""
        self.assertEqual(Fill.from_str('N'), Fill.none)
        self.assertEqual(Fill.from_str('F'), Fill.foreground)
        self.assertEqual(Fill.from_str('f'), Fill.background)

    def test_str(self):
        """Test __str__ output."""
        self.assertEqual(str(Fill.none), 'N')
        self.assertEqual(str(Fill.foreground), 'F')
        self.assertEqual(str(Fill.background), 'f')

    def test_exception(self):
        """Test exception."""
        with self.assertRaises(NotImplementedError):
            Fill.from_str('')


class TestSymbolTypeHJustify(unittest.TestCase):
    """Test class pykicadlib.symbol.types.HJustify."""

    def test_from_str(self):
        """Test classmethod from_str."""
        self.assertEqual(HJustify.from_str('L'), HJustify.left)
        self.assertEqual(HJustify.from_str('C'), HJustify.center)
        self.assertEqual(HJustify.from_str('R'), HJustify.right)

    def test_str(self):
        """Test __str__ output."""
        self.assertEqual(str(HJustify.left), 'L')
        self.assertEqual(str(HJustify.center), 'C')
        self.assertEqual(str(HJustify.right), 'R')

    def test_exception(self):
        """Test exception."""
        with self.assertRaises(NotImplementedError):
            HJustify.from_str('')


class TestSymbolTypeOrientation(unittest.TestCase):
    """Test class pykicadlib.symbol.types.Orientation."""

    def test_from_str(self):
        """Test classmethod from_str."""
        self.assertEqual(Orientation.from_str('H'), Orientation.horizontal)
        self.assertEqual(Orientation.from_str('V'), Orientation.vertical)

    def test_str(self):
        """Test __str__ output."""
        self.assertEqual(str(Orientation.horizontal), 'H')
        self.assertEqual(str(Orientation.vertical), 'V')

    def test_exception(self):
        """Test exception."""
        with self.assertRaises(NotImplementedError):
            Orientation.from_str('')


class TestSymbolTypeRepresentation(unittest.TestCase):
    """Test class pykicadlib.symbol.types.Representation."""

    def test_from_str(self):
        """Test classmethod from_str."""
        self.assertEqual(Representation.from_str('0'), Representation.both)
        self.assertEqual(Representation.from_str('1'), Representation.normal)
        self.assertEqual(Representation.from_str('2'), Representation.morgan)

    def test_str(self):
        """Test __str__ output."""
        self.assertEqual(str(Representation.both), '0')
        self.assertEqual(str(Representation.normal), '1')
        self.assertEqual(str(Representation.morgan), '2')

    def test_exception(self):
        """Test exception."""
        with self.assertRaises(ValueError):
            Representation.from_str('')

        with self.assertRaises(ValueError):
            Representation.from_str('A')

        with self.assertRaises(NotImplementedError):
            Representation.from_str('3')


class TestSymbolTypeStyle(unittest.TestCase):
    """Test class pykicadlib.symbol.types.Style."""

    def test_from_str(self):
        """Test classmethod from_str."""
        self.assertEqual(Style.from_str('NN'), Style.none)
        self.assertEqual(Style.from_str('IN'), Style.italic)
        self.assertEqual(Style.from_str('NB'), Style.bold)
        self.assertEqual(Style.from_str('IB'), Style.italic_bold)

    def test_str(self):
        """Test __str__ output."""
        self.assertEqual(str(Style.none), 'NN')
        self.assertEqual(str(Style.italic), 'IN')
        self.assertEqual(str(Style.bold), 'NB')
        self.assertEqual(str(Style.italic_bold), 'IB')

    def test_exception(self):
        """Test exception."""
        with self.assertRaises(NotImplementedError):
            Style.from_str('')


class TestSymbolTypeVisibility(unittest.TestCase):
    """Test class pykicadlib.symbol.types.Visibility."""

    def test_from_str(self):
        """Test classmethod from_str."""
        self.assertEqual(Visibility.from_str('V'), Visibility.visible)
        self.assertEqual(Visibility.from_str('I'), Visibility.invisible)

    def test_str(self):
        """Test __str__ output."""
        self.assertEqual(str(Visibility.visible), 'V')
        self.assertEqual(str(Visibility.invisible), 'I')

    def test_exception(self):
        """Test exception."""
        with self.assertRaises(NotImplementedError):
            Visibility.from_str('')


class TestSymbolTypeVJustify(unittest.TestCase):
    """Test class pykicadlib.symbol.types.VJustify."""

    def test_from_str(self):
        """Test classmethod from_str."""
        self.assertEqual(VJustify.from_str('T'), VJustify.top)
        self.assertEqual(VJustify.from_str('C'), VJustify.center)
        self.assertEqual(VJustify.from_str('B'), VJustify.bottom)

    def test_str(self):
        """Test __str__ output."""
        self.assertEqual(str(VJustify.top), 'T')
        self.assertEqual(str(VJustify.center), 'C')
        self.assertEqual(str(VJustify.bottom), 'B')

    def test_exception(self):
        """Test exception."""
        with self.assertRaises(NotImplementedError):
            VJustify.from_str('X')


# Pin

class TestSymbolTypeDirection(unittest.TestCase):
    """Test class pykicadlib.symbol.types.Direction."""

    def test_from_str(self):
        """Test classmethod from_str."""
        # NOTE: Definition of directions in KiCAD is flipped! We test against corrected definition!
        self.assertEqual(Direction.from_str('D'), Direction.up)
        self.assertEqual(Direction.from_str('U'), Direction.down)
        self.assertEqual(Direction.from_str('R'), Direction.left)
        self.assertEqual(Direction.from_str('L'), Direction.right)

    def test_from_name(self):
        """Test classmethod from_name."""
        self.assertEqual(Direction.from_name('up'), Direction.up)
        self.assertEqual(Direction.from_name('down'), Direction.down)
        self.assertEqual(Direction.from_name('left'), Direction.left)
        self.assertEqual(Direction.from_name('right'), Direction.right)

    def test_str(self):
        """Test __str__ output."""
        self.assertEqual(str(Direction.up), 'D')
        self.assertEqual(str(Direction.down), 'U')
        self.assertEqual(str(Direction.left), 'R')
        self.assertEqual(str(Direction.right), 'L')

    def test_exception(self):
        """Test exception."""
        with self.assertRaises(NotImplementedError):
            Direction.from_str('')

        with self.assertRaises(NotImplementedError):
            Direction.from_name('')


class TestSymbolTypeElectric(unittest.TestCase):
    """Test class pykicadlib.symbol.types.Electric."""

    def test_from_str(self):
        """Test classmethod from_str."""
        self.assertEqual(Electric.from_str('I'), Electric.input)
        self.assertEqual(Electric.from_str('O'), Electric.output)
        self.assertEqual(Electric.from_str('B'), Electric.bidirectional)
        self.assertEqual(Electric.from_str('T'), Electric.tristate)
        self.assertEqual(Electric.from_str('P'), Electric.passive)
        self.assertEqual(Electric.from_str('U'), Electric.unspecified)
        self.assertEqual(Electric.from_str('W'), Electric.power_input)
        self.assertEqual(Electric.from_str('w'), Electric.power_output)
        self.assertEqual(Electric.from_str('C'), Electric.open_collector)
        self.assertEqual(Electric.from_str('E'), Electric.open_emitter)
        self.assertEqual(Electric.from_str('N'), Electric.not_connected)

    def test_from_name(self):
        """Test classmethod from_name."""
        self.assertEqual(Electric.from_name('input'), Electric.input)
        self.assertEqual(Electric.from_name('output'), Electric.output)
        self.assertEqual(Electric.from_name('bidirectional'), Electric.bidirectional)
        self.assertEqual(Electric.from_name('tristate'), Electric.tristate)
        self.assertEqual(Electric.from_name('passive'), Electric.passive)
        self.assertEqual(Electric.from_name('unspecified'), Electric.unspecified)
        self.assertEqual(Electric.from_name('power_input'), Electric.power_input)
        self.assertEqual(Electric.from_name('power_output'), Electric.power_output)
        self.assertEqual(Electric.from_name('open_collector'), Electric.open_collector)
        self.assertEqual(Electric.from_name('open_emitter'), Electric.open_emitter)
        self.assertEqual(Electric.from_name('not_connected'), Electric.not_connected)

    def test_str(self):
        """Test __str__ output."""
        self.assertEqual(str(Electric.input), 'I')
        self.assertEqual(str(Electric.output), 'O')
        self.assertEqual(str(Electric.bidirectional), 'B')
        self.assertEqual(str(Electric.tristate), 'T')
        self.assertEqual(str(Electric.passive), 'P')
        self.assertEqual(str(Electric.unspecified), 'U')
        self.assertEqual(str(Electric.power_input), 'W')
        self.assertEqual(str(Electric.power_output), 'w')
        self.assertEqual(str(Electric.open_collector), 'C')
        self.assertEqual(str(Electric.open_emitter), 'E')
        self.assertEqual(str(Electric.not_connected), 'N')

    def test_exception(self):
        """Test exception."""
        with self.assertRaises(NotImplementedError):
            Electric.from_str('')

        with self.assertRaises(NotImplementedError):
            Electric.from_name('')


class TestSymbolTypeShape(unittest.TestCase):
    """Test class pykicadlib.symbol.types.Shape."""

    def test_from_str(self):
        """Test classmethod from_str."""
        self.assertEqual(Shape.from_str(''), Shape.line)
        self.assertEqual(Shape.from_str('N'), Shape.invisible)
        self.assertEqual(Shape.from_str('I'), Shape.inverted)
        self.assertEqual(Shape.from_str('C'), Shape.clock)
        self.assertEqual(Shape.from_str('CI'), Shape.inverted_clock)
        self.assertEqual(Shape.from_str('L'), Shape.input_low)
        self.assertEqual(Shape.from_str('CL'), Shape.clock_low)
        self.assertEqual(Shape.from_str('V'), Shape.output_low)
        self.assertEqual(Shape.from_str('F'), Shape.falling_edge_clock)
        self.assertEqual(Shape.from_str('X'), Shape.non_logic)

    def test_from_name(self):
        """Test classmethod from_name."""
        self.assertEqual(Shape.from_name('line'), Shape.line)
        self.assertEqual(Shape.from_name('invisible'), Shape.invisible)
        self.assertEqual(Shape.from_name('inverted'), Shape.inverted)
        self.assertEqual(Shape.from_name('clock'), Shape.clock)
        self.assertEqual(Shape.from_name('inverted_clock'), Shape.inverted_clock)
        self.assertEqual(Shape.from_name('input_low'), Shape.input_low)
        self.assertEqual(Shape.from_name('clock_low'), Shape.clock_low)
        self.assertEqual(Shape.from_name('output_low'), Shape.output_low)
        self.assertEqual(Shape.from_name('falling_edge_clock'), Shape.falling_edge_clock)
        self.assertEqual(Shape.from_name('non_logic'), Shape.non_logic)

    def test_str(self):
        """Test __str__ output."""
        self.assertEqual(str(Shape.line), '')
        self.assertEqual(str(Shape.invisible), 'N')
        self.assertEqual(str(Shape.inverted), 'I')
        self.assertEqual(str(Shape.clock), 'C')
        self.assertEqual(str(Shape.inverted_clock), 'CI')
        self.assertEqual(str(Shape.input_low), 'L')
        self.assertEqual(str(Shape.clock_low), 'CL')
        self.assertEqual(str(Shape.output_low), 'V')
        self.assertEqual(str(Shape.falling_edge_clock), 'F')
        self.assertEqual(str(Shape.non_logic), 'X')

    def test_exception(self):
        """Test exception."""
        with self.assertRaises(NotImplementedError):
            Shape.from_str('A')

        with self.assertRaises(NotImplementedError):
            Shape.from_name('')


# Text

class TestSymbolTypeBold(unittest.TestCase):
    """Test class pykicadlib.symbol.types.Bold."""

    def test_from_str(self):
        """Test classmethod from_str."""
        self.assertEqual(Bold.from_str('0'), Bold.off)
        self.assertEqual(Bold.from_str('1'), Bold.on)

    def test_str(self):
        """Test __str__ output."""
        self.assertEqual(str(Bold.off), '0')
        self.assertEqual(str(Bold.on), '1')

    def test_exception(self):
        """Test exception."""
        with self.assertRaises(ValueError):
            Bold.from_str('')

        with self.assertRaises(ValueError):
            Bold.from_str('A')

        with self.assertRaises(NotImplementedError):
            Bold.from_str('2')


class TestSymbolTypeItalic(unittest.TestCase):
    """Test class pykicadlib.symbol.types.Italic."""

    def test_from_str(self):
        """Test classmethod from_str."""
        self.assertEqual(Italic.from_str('Normal'), Italic.off)
        self.assertEqual(Italic.from_str('Italic'), Italic.on)

    def test_str(self):
        """Test __str__ output."""
        self.assertEqual(str(Italic.off), 'Normal')
        self.assertEqual(str(Italic.on), 'Italic')

    def test_exception(self):
        """Test exception."""
        with self.assertRaises(NotImplementedError):
            Italic.from_str('')
