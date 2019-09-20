# pylint: disable=too-few-public-methods
"""
.. module:: test.symbol.types
   :synopsis: Symbol types test

.. moduleauthor:: Benjamin Füldner <benjamin@fueldner.net>
"""
import unittest
import pykicadlib


class TestSymbolTypeVisible(unittest.TestCase):
    """Test class pykicadlib.symbol.types.Visible"""

    def test_from_str(self):
        """Test static from_str function"""

        self.assertEqual(
            pykicadlib.symbol.types.Visible.from_str('N'),
            pykicadlib.symbol.types.Visible.no)
        self.assertEqual(
            pykicadlib.symbol.types.Visible.from_str('Y'),
            pykicadlib.symbol.types.Visible.yes)

    def test_str(self):
        """Test __str__ output"""

        self.assertEqual(str(pykicadlib.symbol.types.Visible.no), 'N')
        self.assertEqual(str(pykicadlib.symbol.types.Visible.yes), 'Y')

    def test_exception(self):
        """Test exception"""

        with self.assertRaises(NotImplementedError):
            pykicadlib.symbol.types.Visible.from_str('')


class TestSymbolTypeUnits(unittest.TestCase):
    """Test class pykicadlib.symbol.types.Units"""

    def test_from_str(self):
        """Test static from_str function"""

        self.assertEqual(
            pykicadlib.symbol.types.Units.from_str('L'),
            pykicadlib.symbol.types.Units.locked)
        self.assertEqual(
            pykicadlib.symbol.types.Units.from_str('F'),
            pykicadlib.symbol.types.Units.swappable)

    def test_str(self):
        """Test __str__ output"""

        self.assertEqual(str(pykicadlib.symbol.types.Units.locked), 'L')
        self.assertEqual(str(pykicadlib.symbol.types.Units.swappable), 'F')

    def test_exception(self):
        """Test exception"""

        with self.assertRaises(NotImplementedError):
            pykicadlib.symbol.types.Units.from_str('')


class TestSymbolTypeFlag(unittest.TestCase):
    """Test class pykicadlib.symbol.types.Flag"""

    def test_from_str(self):
        """Test static from_str function"""

        self.assertEqual(
            pykicadlib.symbol.types.Flag.from_str('N'),
            pykicadlib.symbol.types.Flag.normal)
        self.assertEqual(
            pykicadlib.symbol.types.Flag.from_str('P'),
            pykicadlib.symbol.types.Flag.power)

    def test_str(self):
        """Test __str__ output"""

        self.assertEqual(str(pykicadlib.symbol.types.Flag.normal), 'N')
        self.assertEqual(str(pykicadlib.symbol.types.Flag.power), 'P')

    def test_exception(self):
        """Test exception"""

        with self.assertRaises(NotImplementedError):
            pykicadlib.symbol.types.Flag.from_str('')


class TestSymbolTypeField(unittest.TestCase):
    """Test class pykicadlib.symbol.types.Field"""

    def test_from_str(self):
        """Test classmethod from_str"""

        self.assertEqual(
            pykicadlib.symbol.types.Field.from_str('0'),
            pykicadlib.symbol.types.Field.reference)
        self.assertEqual(
            pykicadlib.symbol.types.Field.from_str('1'),
            pykicadlib.symbol.types.Field.name)
        self.assertEqual(
            pykicadlib.symbol.types.Field.from_str('2'),
            pykicadlib.symbol.types.Field.footprint)
        self.assertEqual(
            pykicadlib.symbol.types.Field.from_str('3'),
            pykicadlib.symbol.types.Field.document)
        self.assertEqual(
            pykicadlib.symbol.types.Field.from_str('4'),
            pykicadlib.symbol.types.Field.manufacturer)
        self.assertEqual(
            pykicadlib.symbol.types.Field.from_str('5'),
            pykicadlib.symbol.types.Field.value)
        self.assertEqual(
            pykicadlib.symbol.types.Field.from_str('6'),
            pykicadlib.symbol.types.Field.tolerance)
        self.assertEqual(
            pykicadlib.symbol.types.Field.from_str('7'),
            pykicadlib.symbol.types.Field.temperature)
        self.assertEqual(
            pykicadlib.symbol.types.Field.from_str('8'),
            pykicadlib.symbol.types.Field.model)
        self.assertEqual(
            pykicadlib.symbol.types.Field.from_str('9'),
            pykicadlib.symbol.types.Field.voltage)
        self.assertEqual(
            pykicadlib.symbol.types.Field.from_str('10'),
            pykicadlib.symbol.types.Field.power)

    def test_str(self):
        """Test __str__ output"""

        self.assertEqual(str(pykicadlib.symbol.types.Field.reference), 'Reference')
        self.assertEqual(str(pykicadlib.symbol.types.Field.name), 'Name')
        self.assertEqual(str(pykicadlib.symbol.types.Field.footprint), 'Footprint')
        self.assertEqual(str(pykicadlib.symbol.types.Field.document), 'Document')
        self.assertEqual(str(pykicadlib.symbol.types.Field.manufacturer), 'Manufacturer')
        self.assertEqual(str(pykicadlib.symbol.types.Field.value), 'Value')
        self.assertEqual(str(pykicadlib.symbol.types.Field.tolerance), 'Tolerance')
        self.assertEqual(str(pykicadlib.symbol.types.Field.temperature), 'Temperature')
        self.assertEqual(str(pykicadlib.symbol.types.Field.model), 'Model')
        self.assertEqual(str(pykicadlib.symbol.types.Field.voltage), 'Voltage')
        self.assertEqual(str(pykicadlib.symbol.types.Field.power), 'Power')

    def test_exception(self):
        """Test exception"""

        with self.assertRaises(ValueError):
            pykicadlib.symbol.types.Field.from_str('')

        with self.assertRaises(ValueError):
            pykicadlib.symbol.types.Field.from_str('A')

        with self.assertRaises(NotImplementedError):
            pykicadlib.symbol.types.Field.from_str('11')


class TestSymbolTypeOrientation(unittest.TestCase):
    """Test class pykicadlib.symbol.types.Orientation"""

    def test_from_str(self):
        """Test classmethod from_str"""

        self.assertEqual(
            pykicadlib.symbol.types.Orientation.from_str('H'),
            pykicadlib.symbol.types.Orientation.horizontal)
        self.assertEqual(
            pykicadlib.symbol.types.Orientation.from_str('V'),
            pykicadlib.symbol.types.Orientation.vertical)

    def test_str(self):
        """Test __str__ output"""

        self.assertEqual(str(pykicadlib.symbol.types.Orientation.horizontal), 'H')
        self.assertEqual(str(pykicadlib.symbol.types.Orientation.vertical), 'V')

    def test_exception(self):
        """Test exception"""

        with self.assertRaises(NotImplementedError):
            pykicadlib.symbol.types.Orientation.from_str('')


class TestSymbolTypeVisibility(unittest.TestCase):
    """Test class pykicadlib.symbol.types.Visibility"""

    def test_from_str(self):
        """Test classmethod from_str"""

        self.assertEqual(
            pykicadlib.symbol.types.Visibility.from_str('V'),
            pykicadlib.symbol.types.Visibility.visible)
        self.assertEqual(
            pykicadlib.symbol.types.Visibility.from_str('I'),
            pykicadlib.symbol.types.Visibility.invisible)

    def test_str(self):
        """Test __str__ output"""

        self.assertEqual(str(pykicadlib.symbol.types.Visibility.visible), 'V')
        self.assertEqual(str(pykicadlib.symbol.types.Visibility.invisible), 'I')

    def test_exception(self):
        """Test exception"""

        with self.assertRaises(NotImplementedError):
            pykicadlib.symbol.types.Visibility.from_str('')


class TestSymbolTypeHJustify(unittest.TestCase):
    """Test class pykicadlib.symbol.types.HJustify"""

    def test_from_str(self):
        """Test classmethod from_str"""

        self.assertEqual(
            pykicadlib.symbol.types.HJustify.from_str('L'),
            pykicadlib.symbol.types.HJustify.left)
        self.assertEqual(
            pykicadlib.symbol.types.HJustify.from_str('C'),
            pykicadlib.symbol.types.HJustify.center)
        self.assertEqual(
            pykicadlib.symbol.types.HJustify.from_str('R'),
            pykicadlib.symbol.types.HJustify.right)

    def test_str(self):
        """Test __str__ output"""

        self.assertEqual(str(pykicadlib.symbol.types.HJustify.left), 'L')
        self.assertEqual(str(pykicadlib.symbol.types.HJustify.center), 'C')
        self.assertEqual(str(pykicadlib.symbol.types.HJustify.right), 'R')

    def test_exception(self):
        """Test exception"""

        with self.assertRaises(NotImplementedError):
            pykicadlib.symbol.types.HJustify.from_str('')


class TestSymbolTypeVJustify(unittest.TestCase):
    """Test class pykicadlib.symbol.types.VJustify"""

    def test_from_str(self):
        """Test classmethod from_str"""
        self.assertEqual(
            pykicadlib.symbol.types.VJustify.from_str('T'),
            pykicadlib.symbol.types.VJustify.top)
        self.assertEqual(
            pykicadlib.symbol.types.VJustify.from_str('C'),
            pykicadlib.symbol.types.VJustify.center)
        self.assertEqual(
            pykicadlib.symbol.types.VJustify.from_str('B'),
            pykicadlib.symbol.types.VJustify.bottom)

    def test_str(self):
        """Test __str__ output"""

        self.assertEqual(str(pykicadlib.symbol.types.VJustify.top), 'T')
        self.assertEqual(str(pykicadlib.symbol.types.VJustify.center), 'C')
        self.assertEqual(str(pykicadlib.symbol.types.VJustify.bottom), 'B')

    def test_exception(self):
        """Test exception"""

        with self.assertRaises(NotImplementedError):
            pykicadlib.symbol.types.VJustify.from_str('X')


class TestSymbolTypeStyle(unittest.TestCase):
    """Test class pykicadlib.symbol.types.Style"""

    def test_from_str(self):
        """Test classmethod from_str"""

        self.assertEqual(
            pykicadlib.symbol.types.Style.from_str('NN'),
            pykicadlib.symbol.types.Style.none)
        self.assertEqual(
            pykicadlib.symbol.types.Style.from_str('IN'),
            pykicadlib.symbol.types.Style.italic)
        self.assertEqual(
            pykicadlib.symbol.types.Style.from_str('NB'),
            pykicadlib.symbol.types.Style.bold)
        self.assertEqual(
            pykicadlib.symbol.types.Style.from_str('IB'),
            pykicadlib.symbol.types.Style.italic_bold)

    def test_str(self):
        """Test __str__ output"""

        self.assertEqual(str(pykicadlib.symbol.types.Style.none), 'NN')
        self.assertEqual(str(pykicadlib.symbol.types.Style.italic), 'IN')
        self.assertEqual(str(pykicadlib.symbol.types.Style.bold), 'NB')
        self.assertEqual(str(pykicadlib.symbol.types.Style.italic_bold), 'IB')

    def test_exception(self):
        """Test exception"""

        with self.assertRaises(NotImplementedError):
            pykicadlib.symbol.types.Style.from_str('')


class TestSymbolTypeFill(unittest.TestCase):
    """Test class pykicadlib.symbol.types.Fill"""

    def test_from_str(self):
        """Test classmethod from_str"""

        self.assertEqual(
            pykicadlib.symbol.types.Fill.from_str('N'),
            pykicadlib.symbol.types.Fill.none)
        self.assertEqual(
            pykicadlib.symbol.types.Fill.from_str('F'),
            pykicadlib.symbol.types.Fill.foreground)
        self.assertEqual(
            pykicadlib.symbol.types.Fill.from_str('f'),
            pykicadlib.symbol.types.Fill.background)

    def test_str(self):
        """Test __str__ output"""

        self.assertEqual(str(pykicadlib.symbol.types.Fill.none), 'N')
        self.assertEqual(str(pykicadlib.symbol.types.Fill.foreground), 'F')
        self.assertEqual(str(pykicadlib.symbol.types.Fill.background), 'f')

    def test_exception(self):
        """Test exception"""

        with self.assertRaises(NotImplementedError):
            pykicadlib.symbol.types.Fill.from_str('')


class TestSymbolTypeRepresentation(unittest.TestCase):
    """Test class pykicadlib.symbol.types.Representation"""

    def test_from_str(self):
        """Test classmethod from_str"""

        self.assertEqual(
            pykicadlib.symbol.types.Representation.from_str('0'),
            pykicadlib.symbol.types.Representation.both)
        self.assertEqual(
            pykicadlib.symbol.types.Representation.from_str('1'),
            pykicadlib.symbol.types.Representation.normal)
        self.assertEqual(
            pykicadlib.symbol.types.Representation.from_str('2'),
            pykicadlib.symbol.types.Representation.morgan)

    def test_str(self):
        """Test __str__ output"""

        self.assertEqual(str(pykicadlib.symbol.types.Representation.both), '0')
        self.assertEqual(str(pykicadlib.symbol.types.Representation.normal), '1')
        self.assertEqual(str(pykicadlib.symbol.types.Representation.morgan), '2')

    def test_exception(self):
        """Test exception"""

        with self.assertRaises(ValueError):
            pykicadlib.symbol.types.Representation.from_str('')

        with self.assertRaises(ValueError):
            pykicadlib.symbol.types.Representation.from_str('A')

        with self.assertRaises(NotImplementedError):
            pykicadlib.symbol.types.Representation.from_str('3')


class TestSymbolTypeItalic(unittest.TestCase):
    """Test class pykicadlib.symbol.types.Italic"""

    def test_from_str(self):
        """Test classmethod from_str"""

        self.assertEqual(
            pykicadlib.symbol.types.Italic.from_str('Normal'),
            pykicadlib.symbol.types.Italic.off)
        self.assertEqual(
            pykicadlib.symbol.types.Italic.from_str('Italic'),
            pykicadlib.symbol.types.Italic.on)

    def test_str(self):
        """Test __str__ output"""

        self.assertEqual(str(pykicadlib.symbol.types.Italic.off), 'Normal')
        self.assertEqual(str(pykicadlib.symbol.types.Italic.on), 'Italic')

    def test_exception(self):
        """Test exception"""

        with self.assertRaises(NotImplementedError):
            pykicadlib.symbol.types.Italic.from_str('')


class TestSymbolTypeBold(unittest.TestCase):
    """Test class pykicadlib.symbol.types.Bold"""

    def test_from_str(self):
        """Test classmethod from_str"""

        self.assertEqual(
            pykicadlib.symbol.types.Bold.from_str('0'),
            pykicadlib.symbol.types.Bold.off)
        self.assertEqual(
            pykicadlib.symbol.types.Bold.from_str('1'),
            pykicadlib.symbol.types.Bold.on)

    def test_str(self):
        """Test __str__ output"""

        self.assertEqual(str(pykicadlib.symbol.types.Bold.off), '0')
        self.assertEqual(str(pykicadlib.symbol.types.Bold.on), '1')

    def test_exception(self):
        """Test exception"""

        with self.assertRaises(ValueError):
            pykicadlib.symbol.types.Bold.from_str('')

        with self.assertRaises(ValueError):
            pykicadlib.symbol.types.Bold.from_str('A')

        with self.assertRaises(NotImplementedError):
            pykicadlib.symbol.types.Bold.from_str('2')


class TestSymbolTypeDirection(unittest.TestCase):
    """Test class pykicadlib.symbol.types.Direction"""

    def test_from_str(self):
        """Test classmethod from_str"""

        # NOTE: Definition of directions in KiCAD is flipped! We test against corrected definition!
        self.assertEqual(
            pykicadlib.symbol.types.Direction.from_str('D'),
            pykicadlib.symbol.types.Direction.up)
        self.assertEqual(
            pykicadlib.symbol.types.Direction.from_str('U'),
            pykicadlib.symbol.types.Direction.down)
        self.assertEqual(
            pykicadlib.symbol.types.Direction.from_str('R'),
            pykicadlib.symbol.types.Direction.left)
        self.assertEqual(
            pykicadlib.symbol.types.Direction.from_str('L'),
            pykicadlib.symbol.types.Direction.right)

    def test_str(self):
        """Test __str__ output"""

        self.assertEqual(str(pykicadlib.symbol.types.Direction.up), 'D')
        self.assertEqual(str(pykicadlib.symbol.types.Direction.down), 'U')
        self.assertEqual(str(pykicadlib.symbol.types.Direction.left), 'R')
        self.assertEqual(str(pykicadlib.symbol.types.Direction.right), 'L')

    def test_exception(self):
        """Test exception"""

        with self.assertRaises(NotImplementedError):
            pykicadlib.symbol.types.Direction.from_str('')


class TestSymbolTypeElectric(unittest.TestCase):
    """Test class pykicadlib.symbol.types.Electric"""

    def test_from_str(self):
        """Test classmethod from_str"""

        self.assertEqual(
            pykicadlib.symbol.types.Electric.from_str('I'),
            pykicadlib.symbol.types.Electric.input)
        self.assertEqual(
            pykicadlib.symbol.types.Electric.from_str('O'),
            pykicadlib.symbol.types.Electric.output)
        self.assertEqual(
            pykicadlib.symbol.types.Electric.from_str('B'),
            pykicadlib.symbol.types.Electric.bidirectional)
        self.assertEqual(
            pykicadlib.symbol.types.Electric.from_str('T'),
            pykicadlib.symbol.types.Electric.tristate)
        self.assertEqual(
            pykicadlib.symbol.types.Electric.from_str('P'),
            pykicadlib.symbol.types.Electric.passive)
        self.assertEqual(
            pykicadlib.symbol.types.Electric.from_str('U'),
            pykicadlib.symbol.types.Electric.unspecified)
        self.assertEqual(
            pykicadlib.symbol.types.Electric.from_str('W'),
            pykicadlib.symbol.types.Electric.power_input)
        self.assertEqual(
            pykicadlib.symbol.types.Electric.from_str('w'),
            pykicadlib.symbol.types.Electric.power_output)
        self.assertEqual(
            pykicadlib.symbol.types.Electric.from_str('C'),
            pykicadlib.symbol.types.Electric.open_collector)
        self.assertEqual(
            pykicadlib.symbol.types.Electric.from_str('E'),
            pykicadlib.symbol.types.Electric.open_emitter)
        self.assertEqual(
            pykicadlib.symbol.types.Electric.from_str('N'),
            pykicadlib.symbol.types.Electric.not_connected)

    def test_str(self):
        """Test __str__ output"""

        self.assertEqual(str(pykicadlib.symbol.types.Electric.input), 'I')
        self.assertEqual(str(pykicadlib.symbol.types.Electric.output), 'O')
        self.assertEqual(str(pykicadlib.symbol.types.Electric.bidirectional), 'B')
        self.assertEqual(str(pykicadlib.symbol.types.Electric.tristate), 'T')
        self.assertEqual(str(pykicadlib.symbol.types.Electric.passive), 'P')
        self.assertEqual(str(pykicadlib.symbol.types.Electric.unspecified), 'U')
        self.assertEqual(str(pykicadlib.symbol.types.Electric.power_input), 'W')
        self.assertEqual(str(pykicadlib.symbol.types.Electric.power_output), 'w')
        self.assertEqual(str(pykicadlib.symbol.types.Electric.open_collector), 'C')
        self.assertEqual(str(pykicadlib.symbol.types.Electric.open_emitter), 'E')
        self.assertEqual(str(pykicadlib.symbol.types.Electric.not_connected), 'N')

    def test_exception(self):
        """Test exception"""

        with self.assertRaises(NotImplementedError):
            pykicadlib.symbol.types.Electric.from_str('')


class TestSymbolTypeShape(unittest.TestCase):
    """Test class pykicadlib.symbol.types.Shape"""

    def test_from_str(self):
        """Test classmethod from_str"""

        self.assertEqual(
            pykicadlib.symbol.types.Shape.from_str(''),
            pykicadlib.symbol.types.Shape.line)
        self.assertEqual(
            pykicadlib.symbol.types.Shape.from_str('N'),
            pykicadlib.symbol.types.Shape.invisible)
        self.assertEqual(
            pykicadlib.symbol.types.Shape.from_str('I'),
            pykicadlib.symbol.types.Shape.inverted)
        self.assertEqual(
            pykicadlib.symbol.types.Shape.from_str('C'),
            pykicadlib.symbol.types.Shape.clock)
        self.assertEqual(
            pykicadlib.symbol.types.Shape.from_str('CI'),
            pykicadlib.symbol.types.Shape.inverted_clock)
        self.assertEqual(
            pykicadlib.symbol.types.Shape.from_str('L'),
            pykicadlib.symbol.types.Shape.input_low)
        self.assertEqual(
            pykicadlib.symbol.types.Shape.from_str('CL'),
            pykicadlib.symbol.types.Shape.clock_low)
        self.assertEqual(
            pykicadlib.symbol.types.Shape.from_str('V'),
            pykicadlib.symbol.types.Shape.output_low)
        self.assertEqual(
            pykicadlib.symbol.types.Shape.from_str('F'),
            pykicadlib.symbol.types.Shape.falling_edge_clock)
        self.assertEqual(
            pykicadlib.symbol.types.Shape.from_str('X'),
            pykicadlib.symbol.types.Shape.non_logic)

    def test_str(self):
        """Test __str__ output"""

        self.assertEqual(str(pykicadlib.symbol.types.Shape.line), '')
        self.assertEqual(str(pykicadlib.symbol.types.Shape.invisible), 'N')
        self.assertEqual(str(pykicadlib.symbol.types.Shape.inverted), 'I')
        self.assertEqual(str(pykicadlib.symbol.types.Shape.clock), 'C')
        self.assertEqual(str(pykicadlib.symbol.types.Shape.inverted_clock), 'CI')
        self.assertEqual(str(pykicadlib.symbol.types.Shape.input_low), 'L')
        self.assertEqual(str(pykicadlib.symbol.types.Shape.clock_low), 'CL')
        self.assertEqual(str(pykicadlib.symbol.types.Shape.output_low), 'V')
        self.assertEqual(str(pykicadlib.symbol.types.Shape.falling_edge_clock), 'F')
        self.assertEqual(str(pykicadlib.symbol.types.Shape.non_logic), 'X')

    def test_exception(self):
        """Test exception"""

        with self.assertRaises(NotImplementedError):
            pykicadlib.symbol.types.Shape.from_str('A')
