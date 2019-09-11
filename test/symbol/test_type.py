"""
.. module:: symbol.type
   :synopsis: Symbol types test

.. moduleauthor:: Benjamin Füldner <benjamin@fueldner.net>
"""
import unittest
import pykicadlib


class TestSymbolTypeVisible(unittest.TestCase):
    """Test class pykicadlib.symbol.type.Visible"""

    def test_from_str(self):
        """Test static from_str function"""

        self.assertEqual(
            pykicadlib.symbol.type.Visible.from_str('N'),
            pykicadlib.symbol.type.Visible.no)
        self.assertEqual(
            pykicadlib.symbol.type.Visible.from_str('Y'),
            pykicadlib.symbol.type.Visible.yes)

    def test_str(self):
        """Test __str__ output"""

        self.assertEqual(str(pykicadlib.symbol.type.Visible.no), 'N')
        self.assertEqual(str(pykicadlib.symbol.type.Visible.yes), 'Y')

    def test_exception(self):
        """Test exception"""

        with self.assertRaises(NotImplementedError):
            pykicadlib.symbol.type.Visible.from_str('')


class TestSymbolTypeUnits(unittest.TestCase):
    """Test class pykicadlib.symbol.type.Units"""

    def test_from_str(self):
        """Test static from_str function"""

        self.assertEqual(
            pykicadlib.symbol.type.Units.from_str('L'),
            pykicadlib.symbol.type.Units.locked)
        self.assertEqual(
            pykicadlib.symbol.type.Units.from_str('F'),
            pykicadlib.symbol.type.Units.swappable)

    def test_str(self):
        """Test __str__ output"""

        self.assertEqual(str(pykicadlib.symbol.type.Units.locked), 'L')
        self.assertEqual(str(pykicadlib.symbol.type.Units.swappable), 'F')

    def test_exception(self):
        """Test exception"""

        with self.assertRaises(NotImplementedError):
            pykicadlib.symbol.type.Units.from_str('')


class TestSymbolTypeFlag(unittest.TestCase):
    """Test class pykicadlib.symbol.type.Flag"""

    def test_from_str(self):
        """Test static from_str function"""

        self.assertEqual(
            pykicadlib.symbol.type.Flag.from_str('N'),
            pykicadlib.symbol.type.Flag.normal)
        self.assertEqual(
            pykicadlib.symbol.type.Flag.from_str('P'),
            pykicadlib.symbol.type.Flag.power)

    def test_str(self):
        """Test __str__ output"""

        self.assertEqual(str(pykicadlib.symbol.type.Flag.normal), 'N')
        self.assertEqual(str(pykicadlib.symbol.type.Flag.power), 'P')

    def test_exception(self):
        """Test exception"""

        with self.assertRaises(NotImplementedError):
            pykicadlib.symbol.type.Flag.from_str('')


class TestSymbolTypeField(unittest.TestCase):
    """Test class pykicadlib.symbol.type.Field"""

    def test_from_str(self):
        """Test classmethod from_str"""

        self.assertEqual(
            pykicadlib.symbol.type.Field.from_str('0'),
            pykicadlib.symbol.type.Field.reference)
        self.assertEqual(
            pykicadlib.symbol.type.Field.from_str('1'),
            pykicadlib.symbol.type.Field.name)
        self.assertEqual(
            pykicadlib.symbol.type.Field.from_str('2'),
            pykicadlib.symbol.type.Field.footprint)
        self.assertEqual(
            pykicadlib.symbol.type.Field.from_str('3'),
            pykicadlib.symbol.type.Field.document)
        self.assertEqual(
            pykicadlib.symbol.type.Field.from_str('4'),
            pykicadlib.symbol.type.Field.manufacturer)
        self.assertEqual(
            pykicadlib.symbol.type.Field.from_str('5'),
            pykicadlib.symbol.type.Field.value)
        self.assertEqual(
            pykicadlib.symbol.type.Field.from_str('6'),
            pykicadlib.symbol.type.Field.tolerance)
        self.assertEqual(
            pykicadlib.symbol.type.Field.from_str('7'),
            pykicadlib.symbol.type.Field.temperature)
        self.assertEqual(
            pykicadlib.symbol.type.Field.from_str('8'),
            pykicadlib.symbol.type.Field.model)
        self.assertEqual(
            pykicadlib.symbol.type.Field.from_str('9'),
            pykicadlib.symbol.type.Field.voltage)
        self.assertEqual(
            pykicadlib.symbol.type.Field.from_str('10'),
            pykicadlib.symbol.type.Field.power)

    def test_str(self):
        """Test __str__ output"""

        self.assertEqual(str(pykicadlib.symbol.type.Field.reference), 'Reference')
        self.assertEqual(str(pykicadlib.symbol.type.Field.name), 'Name')
        self.assertEqual(str(pykicadlib.symbol.type.Field.footprint), 'Footprint')
        self.assertEqual(str(pykicadlib.symbol.type.Field.document), 'Document')
        self.assertEqual(str(pykicadlib.symbol.type.Field.manufacturer), 'Manufacturer')
        self.assertEqual(str(pykicadlib.symbol.type.Field.value), 'Value')
        self.assertEqual(str(pykicadlib.symbol.type.Field.tolerance), 'Tolerance')
        self.assertEqual(str(pykicadlib.symbol.type.Field.temperature), 'Temperature')
        self.assertEqual(str(pykicadlib.symbol.type.Field.model), 'Model')
        self.assertEqual(str(pykicadlib.symbol.type.Field.voltage), 'Voltage')
        self.assertEqual(str(pykicadlib.symbol.type.Field.power), 'Power')

    def test_exception(self):
        """Test exception"""

        with self.assertRaises(ValueError):
            pykicadlib.symbol.type.Field.from_str('')

        with self.assertRaises(ValueError):
            pykicadlib.symbol.type.Field.from_str('A')

        with self.assertRaises(NotImplementedError):
            pykicadlib.symbol.type.Field.from_str('11')


class TestSymbolTypeOrientation(unittest.TestCase):
    """Test class pykicadlib.symbol.type.Orientation"""

    def test_from_str(self):
        """Test classmethod from_str"""

        self.assertEqual(
            pykicadlib.symbol.type.Orientation.from_str('H'),
            pykicadlib.symbol.type.Orientation.horizontal)
        self.assertEqual(
            pykicadlib.symbol.type.Orientation.from_str('V'),
            pykicadlib.symbol.type.Orientation.vertical)

    def test_str(self):
        """Test __str__ output"""

        self.assertEqual(str(pykicadlib.symbol.type.Orientation.horizontal), 'H')
        self.assertEqual(str(pykicadlib.symbol.type.Orientation.vertical), 'V')

    def test_exception(self):
        """Test exception"""

        with self.assertRaises(NotImplementedError):
            pykicadlib.symbol.type.Orientation.from_str('')


class TestSymbolTypeVisibility(unittest.TestCase):
    """Test class pykicadlib.symbol.type.Visibility"""

    def test_from_str(self):
        """Test classmethod from_str"""

        self.assertEqual(
            pykicadlib.symbol.type.Visibility.from_str('V'),
            pykicadlib.symbol.type.Visibility.visible)
        self.assertEqual(
            pykicadlib.symbol.type.Visibility.from_str('I'),
            pykicadlib.symbol.type.Visibility.invisible)

    def test_str(self):
        """Test __str__ output"""

        self.assertEqual(str(pykicadlib.symbol.type.Visibility.visible), 'V')
        self.assertEqual(str(pykicadlib.symbol.type.Visibility.invisible), 'I')

    def test_exception(self):
        """Test exception"""

        with self.assertRaises(NotImplementedError):
            pykicadlib.symbol.type.Visibility.from_str('')


class TestSymbolTypeHJustify(unittest.TestCase):
    """Test class pykicadlib.symbol.type.HJustify"""

    def test_from_str(self):
        """Test classmethod from_str"""

        self.assertEqual(
            pykicadlib.symbol.type.HJustify.from_str('L'),
            pykicadlib.symbol.type.HJustify.left)
        self.assertEqual(
            pykicadlib.symbol.type.HJustify.from_str('C'),
            pykicadlib.symbol.type.HJustify.center)
        self.assertEqual(
            pykicadlib.symbol.type.HJustify.from_str('R'),
            pykicadlib.symbol.type.HJustify.right)

    def test_str(self):
        """Test __str__ output"""

        self.assertEqual(str(pykicadlib.symbol.type.HJustify.left), 'L')
        self.assertEqual(str(pykicadlib.symbol.type.HJustify.center), 'C')
        self.assertEqual(str(pykicadlib.symbol.type.HJustify.right), 'R')

    def test_exception(self):
        """Test exception"""

        with self.assertRaises(NotImplementedError):
            pykicadlib.symbol.type.HJustify.from_str('')


class TestSymbolTypeVJustify(unittest.TestCase):
    """Test class pykicadlib.symbol.type.VJustify"""

    def test_from_str(self):
        """Test classmethod from_str"""
        self.assertEqual(
            pykicadlib.symbol.type.VJustify.from_str('T'),
            pykicadlib.symbol.type.VJustify.top)
        self.assertEqual(
            pykicadlib.symbol.type.VJustify.from_str('C'),
            pykicadlib.symbol.type.VJustify.center)
        self.assertEqual(
            pykicadlib.symbol.type.VJustify.from_str('B'),
            pykicadlib.symbol.type.VJustify.bottom)

    def test_str(self):
        """Test __str__ output"""

        self.assertEqual(str(pykicadlib.symbol.type.VJustify.top), 'T')
        self.assertEqual(str(pykicadlib.symbol.type.VJustify.center), 'C')
        self.assertEqual(str(pykicadlib.symbol.type.VJustify.bottom), 'B')

    def test_exception(self):
        """Test exception"""

        with self.assertRaises(NotImplementedError):
            pykicadlib.symbol.type.VJustify.from_str('X')


class TestSymbolTypeStyle(unittest.TestCase):
    """Test class pykicadlib.symbol.type.Style"""

    def test_from_str(self):
        """Test classmethod from_str"""

        self.assertEqual(
            pykicadlib.symbol.type.Style.from_str('NN'),
            pykicadlib.symbol.type.Style.none)
        self.assertEqual(
            pykicadlib.symbol.type.Style.from_str('IN'),
            pykicadlib.symbol.type.Style.italic)
        self.assertEqual(
            pykicadlib.symbol.type.Style.from_str('NB'),
            pykicadlib.symbol.type.Style.bold)
        self.assertEqual(
            pykicadlib.symbol.type.Style.from_str('IB'),
            pykicadlib.symbol.type.Style.italic_bold)

    def test_str(self):
        """Test __str__ output"""

        self.assertEqual(str(pykicadlib.symbol.type.Style.none), 'NN')
        self.assertEqual(str(pykicadlib.symbol.type.Style.italic), 'IN')
        self.assertEqual(str(pykicadlib.symbol.type.Style.bold), 'NB')
        self.assertEqual(str(pykicadlib.symbol.type.Style.italic_bold), 'IB')

    def test_exception(self):
        """Test exception"""

        with self.assertRaises(NotImplementedError):
            pykicadlib.symbol.type.Style.from_str('')


class TestSymbolTypeFill(unittest.TestCase):
    """Test class pykicadlib.symbol.type.Fill"""

    def test_from_str(self):
        """Test classmethod from_str"""

        self.assertEqual(
            pykicadlib.symbol.type.Fill.from_str('N'),
            pykicadlib.symbol.type.Fill.none)
        self.assertEqual(
            pykicadlib.symbol.type.Fill.from_str('F'),
            pykicadlib.symbol.type.Fill.foreground)
        self.assertEqual(
            pykicadlib.symbol.type.Fill.from_str('f'),
            pykicadlib.symbol.type.Fill.background)

    def test_str(self):
        """Test __str__ output"""

        self.assertEqual(str(pykicadlib.symbol.type.Fill.none), 'N')
        self.assertEqual(str(pykicadlib.symbol.type.Fill.foreground), 'F')
        self.assertEqual(str(pykicadlib.symbol.type.Fill.background), 'f')

    def test_exception(self):
        """Test exception"""

        with self.assertRaises(NotImplementedError):
            pykicadlib.symbol.type.Fill.from_str('')


class TestSymbolTypeRepresentation(unittest.TestCase):
    """Test class pykicadlib.symbol.type.Representation"""

    def test_from_str(self):
        """Test classmethod from_str"""

        self.assertEqual(
            pykicadlib.symbol.type.Representation.from_str('0'),
            pykicadlib.symbol.type.Representation.both)
        self.assertEqual(
            pykicadlib.symbol.type.Representation.from_str('1'),
            pykicadlib.symbol.type.Representation.normal)
        self.assertEqual(
            pykicadlib.symbol.type.Representation.from_str('2'),
            pykicadlib.symbol.type.Representation.morgan)

    def test_str(self):
        """Test __str__ output"""

        self.assertEqual(str(pykicadlib.symbol.type.Representation.both), '0')
        self.assertEqual(str(pykicadlib.symbol.type.Representation.normal), '1')
        self.assertEqual(str(pykicadlib.symbol.type.Representation.morgan), '2')

    def test_exception(self):
        """Test exception"""

        with self.assertRaises(ValueError):
            pykicadlib.symbol.type.Representation.from_str('')

        with self.assertRaises(ValueError):
            pykicadlib.symbol.type.Representation.from_str('A')

        with self.assertRaises(NotImplementedError):
            pykicadlib.symbol.type.Representation.from_str('3')


class TestSymbolTypeItalic(unittest.TestCase):
    """Test class pykicadlib.symbol.type.Italic"""

    def test_from_str(self):
        """Test classmethod from_str"""

        self.assertEqual(
            pykicadlib.symbol.type.Italic.from_str('Normal'),
            pykicadlib.symbol.type.Italic.off)
        self.assertEqual(
            pykicadlib.symbol.type.Italic.from_str('Italic'),
            pykicadlib.symbol.type.Italic.on)

    def test_str(self):
        """Test __str__ output"""

        self.assertEqual(str(pykicadlib.symbol.type.Italic.off), 'Normal')
        self.assertEqual(str(pykicadlib.symbol.type.Italic.on), 'Italic')

    def test_exception(self):
        """Test exception"""

        with self.assertRaises(NotImplementedError):
            pykicadlib.symbol.type.Italic.from_str('')


class TestSymbolTypeBold(unittest.TestCase):
    """Test class pykicadlib.symbol.type.Bold"""

    def test_from_str(self):
        """Test classmethod from_str"""

        self.assertEqual(
            pykicadlib.symbol.type.Bold.from_str('0'),
            pykicadlib.symbol.type.Bold.off)
        self.assertEqual(
            pykicadlib.symbol.type.Bold.from_str('1'),
            pykicadlib.symbol.type.Bold.on)

    def test_str(self):
        """Test __str__ output"""

        self.assertEqual(str(pykicadlib.symbol.type.Bold.off), '0')
        self.assertEqual(str(pykicadlib.symbol.type.Bold.on), '1')

    def test_exception(self):
        """Test exception"""

        with self.assertRaises(ValueError):
            pykicadlib.symbol.type.Bold.from_str('')

        with self.assertRaises(ValueError):
            pykicadlib.symbol.type.Bold.from_str('A')

        with self.assertRaises(NotImplementedError):
            pykicadlib.symbol.type.Bold.from_str('2')


class TestSymbolTypeDirection(unittest.TestCase):
    """Test class pykicadlib.symbol.type.Direction"""

    def test_from_str(self):
        """Test classmethod from_str"""

        # NOTE: Definition of directions in KiCAD is flipped! We test against corrected definition!
        self.assertEqual(
            pykicadlib.symbol.type.Direction.from_str('D'),
            pykicadlib.symbol.type.Direction.up)
        self.assertEqual(
            pykicadlib.symbol.type.Direction.from_str('U'),
            pykicadlib.symbol.type.Direction.down)
        self.assertEqual(
            pykicadlib.symbol.type.Direction.from_str('R'),
            pykicadlib.symbol.type.Direction.left)
        self.assertEqual(
            pykicadlib.symbol.type.Direction.from_str('L'),
            pykicadlib.symbol.type.Direction.right)

    def test_str(self):
        """Test __str__ output"""

        self.assertEqual(str(pykicadlib.symbol.type.Direction.up), 'D')
        self.assertEqual(str(pykicadlib.symbol.type.Direction.down), 'U')
        self.assertEqual(str(pykicadlib.symbol.type.Direction.left), 'R')
        self.assertEqual(str(pykicadlib.symbol.type.Direction.right), 'L')

    def test_exception(self):
        """Test exception"""

        with self.assertRaises(NotImplementedError):
            pykicadlib.symbol.type.Direction.from_str('')


class TestSymbolTypeElectric(unittest.TestCase):
    """Test class pykicadlib.symbol.type.Electric"""

    def test_from_str(self):
        """Test classmethod from_str"""

        self.assertEqual(
            pykicadlib.symbol.type.Electric.from_str('I'),
            pykicadlib.symbol.type.Electric.input)
        self.assertEqual(
            pykicadlib.symbol.type.Electric.from_str('O'),
            pykicadlib.symbol.type.Electric.output)
        self.assertEqual(
            pykicadlib.symbol.type.Electric.from_str('B'),
            pykicadlib.symbol.type.Electric.bidirectional)
        self.assertEqual(
            pykicadlib.symbol.type.Electric.from_str('T'),
            pykicadlib.symbol.type.Electric.tristate)
        self.assertEqual(
            pykicadlib.symbol.type.Electric.from_str('P'),
            pykicadlib.symbol.type.Electric.passive)
        self.assertEqual(
            pykicadlib.symbol.type.Electric.from_str('U'),
            pykicadlib.symbol.type.Electric.unspecified)
        self.assertEqual(
            pykicadlib.symbol.type.Electric.from_str('W'),
            pykicadlib.symbol.type.Electric.power_input)
        self.assertEqual(
            pykicadlib.symbol.type.Electric.from_str('w'),
            pykicadlib.symbol.type.Electric.power_output)
        self.assertEqual(
            pykicadlib.symbol.type.Electric.from_str('C'),
            pykicadlib.symbol.type.Electric.open_collector)
        self.assertEqual(
            pykicadlib.symbol.type.Electric.from_str('E'),
            pykicadlib.symbol.type.Electric.open_emitter)
        self.assertEqual(
            pykicadlib.symbol.type.Electric.from_str('N'),
            pykicadlib.symbol.type.Electric.not_connected)

    def test_str(self):
        """Test __str__ output"""

        self.assertEqual(str(pykicadlib.symbol.type.Electric.input), 'I')
        self.assertEqual(str(pykicadlib.symbol.type.Electric.output), 'O')
        self.assertEqual(str(pykicadlib.symbol.type.Electric.bidirectional), 'B')
        self.assertEqual(str(pykicadlib.symbol.type.Electric.tristate), 'T')
        self.assertEqual(str(pykicadlib.symbol.type.Electric.passive), 'P')
        self.assertEqual(str(pykicadlib.symbol.type.Electric.unspecified), 'U')
        self.assertEqual(str(pykicadlib.symbol.type.Electric.power_input), 'W')
        self.assertEqual(str(pykicadlib.symbol.type.Electric.power_output), 'w')
        self.assertEqual(str(pykicadlib.symbol.type.Electric.open_collector), 'C')
        self.assertEqual(str(pykicadlib.symbol.type.Electric.open_emitter), 'E')
        self.assertEqual(str(pykicadlib.symbol.type.Electric.not_connected), 'N')

    def test_exception(self):
        """Test exception"""

        with self.assertRaises(NotImplementedError):
            pykicadlib.symbol.type.Electric.from_str('')


class TestSymbolTypeShape(unittest.TestCase):
    """Test class pykicadlib.symbol.type.Shape"""

    def test_from_str(self):
        """Test classmethod from_str"""

        self.assertEqual(
            pykicadlib.symbol.type.Shape.from_str(''),
            pykicadlib.symbol.type.Shape.line)
        self.assertEqual(
            pykicadlib.symbol.type.Shape.from_str('N'),
            pykicadlib.symbol.type.Shape.invisible)
        self.assertEqual(
            pykicadlib.symbol.type.Shape.from_str('I'),
            pykicadlib.symbol.type.Shape.inverted)
        self.assertEqual(
            pykicadlib.symbol.type.Shape.from_str('C'),
            pykicadlib.symbol.type.Shape.clock)
        self.assertEqual(
            pykicadlib.symbol.type.Shape.from_str('CI'),
            pykicadlib.symbol.type.Shape.inverted_clock)
        self.assertEqual(
            pykicadlib.symbol.type.Shape.from_str('L'),
            pykicadlib.symbol.type.Shape.input_low)
        self.assertEqual(
            pykicadlib.symbol.type.Shape.from_str('CL'),
            pykicadlib.symbol.type.Shape.clock_low)
        self.assertEqual(
            pykicadlib.symbol.type.Shape.from_str('V'),
            pykicadlib.symbol.type.Shape.output_low)
        self.assertEqual(
            pykicadlib.symbol.type.Shape.from_str('F'),
            pykicadlib.symbol.type.Shape.falling_edge_clock)
        self.assertEqual(
            pykicadlib.symbol.type.Shape.from_str('X'),
            pykicadlib.symbol.type.Shape.non_logic)

    def test_str(self):
        """Test __str__ output"""

        self.assertEqual(str(pykicadlib.symbol.type.Shape.line), '')
        self.assertEqual(str(pykicadlib.symbol.type.Shape.invisible), 'N')
        self.assertEqual(str(pykicadlib.symbol.type.Shape.inverted), 'I')
        self.assertEqual(str(pykicadlib.symbol.type.Shape.clock), 'C')
        self.assertEqual(str(pykicadlib.symbol.type.Shape.inverted_clock), 'CI')
        self.assertEqual(str(pykicadlib.symbol.type.Shape.input_low), 'L')
        self.assertEqual(str(pykicadlib.symbol.type.Shape.clock_low), 'CL')
        self.assertEqual(str(pykicadlib.symbol.type.Shape.output_low), 'V')
        self.assertEqual(str(pykicadlib.symbol.type.Shape.falling_edge_clock), 'F')
        self.assertEqual(str(pykicadlib.symbol.type.Shape.non_logic), 'X')

    def test_exception(self):
        """Test exception"""

        with self.assertRaises(NotImplementedError):
            pykicadlib.symbol.type.Shape.from_str('A')
