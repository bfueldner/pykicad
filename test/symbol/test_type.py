import unittest
import pykicadlib.symbol.type


class TestSymbolTypeVisible(unittest.TestCase):

    def test_visible_no(self):
        test = pykicadlib.symbol.type.visible.from_str('N')
        self.assertEqual(test, pykicadlib.symbol.type.visible.no)
        self.assertEqual(str(pykicadlib.symbol.type.visible.no), 'N')

    def test_visible_yes(self):
        test = pykicadlib.symbol.type.visible.from_str('Y')
        self.assertEqual(test, pykicadlib.symbol.type.visible.yes)
        self.assertEqual(str(pykicadlib.symbol.type.visible.yes), 'Y')

    def test_exception(self):
        with self.assertRaises(NotImplementedError):
            pykicadlib.symbol.type.visible.from_str('')


class TestSymbolTypeUnits(unittest.TestCase):
    def test_unitslocked(self):
        test = pykicadlib.symbol.type.units.from_str('L')
        self.assertEqual(test, pykicadlib.symbol.type.units.locked)
        self.assertEqual(str(pykicadlib.symbol.type.units.locked), 'L')

    def test_units_swappable(self):
        test = pykicadlib.symbol.type.units.from_str('F')
        self.assertEqual(test, pykicadlib.symbol.type.units.swappable)
        self.assertEqual(str(pykicadlib.symbol.type.units.swappable), 'F')

    def test_exception(self):
        with self.assertRaises(NotImplementedError):
            pykicadlib.symbol.type.units.from_str('')


class TestSymbolTypeFlag(unittest.TestCase):
    def test_flag_normal(self):
        test = pykicadlib.symbol.type.flag.from_str('N')
        self.assertEqual(test, pykicadlib.symbol.type.flag.normal)
        self.assertEqual(str(pykicadlib.symbol.type.flag.normal), 'N')

    def test_flag_power(self):
        test = pykicadlib.symbol.type.flag.from_str('P')
        self.assertEqual(test, pykicadlib.symbol.type.flag.power)
        self.assertEqual(str(pykicadlib.symbol.type.flag.power), 'P')

    def test_exception(self):
        with self.assertRaises(NotImplementedError):
            pykicadlib.symbol.type.flag.from_str('')


class TestSymbolTypeField(unittest.TestCase):
    def test_field_reference(self):
        test = pykicadlib.symbol.type.field.from_str('0')
        self.assertEqual(test, pykicadlib.symbol.type.field.reference)
        self.assertEqual(str(pykicadlib.symbol.type.field.reference), 'Reference')

    def test_field_name(self):
        test = pykicadlib.symbol.type.field.from_str('1')
        self.assertEqual(test, pykicadlib.symbol.type.field.name)
        self.assertEqual(str(pykicadlib.symbol.type.field.name), 'Name')

    def test_field_footprint(self):
        test = pykicadlib.symbol.type.field.from_str('2')
        self.assertEqual(test, pykicadlib.symbol.type.field.footprint)
        self.assertEqual(str(pykicadlib.symbol.type.field.footprint), 'Footprint')

    def test_field_document(self):
        test = pykicadlib.symbol.type.field.from_str('3')
        self.assertEqual(test, pykicadlib.symbol.type.field.document)
        self.assertEqual(str(pykicadlib.symbol.type.field.document), 'Document')

    def test_field_manufacturer(self):
        test = pykicadlib.symbol.type.field.from_str('4')
        self.assertEqual(test, pykicadlib.symbol.type.field.manufacturer)
        self.assertEqual(str(pykicadlib.symbol.type.field.manufacturer), 'Manufacturer')

    def test_field_value(self):
        test = pykicadlib.symbol.type.field.from_str('5')
        self.assertEqual(test, pykicadlib.symbol.type.field.value)
        self.assertEqual(str(pykicadlib.symbol.type.field.value), 'Value')

    def test_field_tolerance(self):
        test = pykicadlib.symbol.type.field.from_str('6')
        self.assertEqual(test, pykicadlib.symbol.type.field.tolerance)
        self.assertEqual(str(pykicadlib.symbol.type.field.tolerance), 'Tolerance')

    def test_field_temperature(self):
        test = pykicadlib.symbol.type.field.from_str('7')
        self.assertEqual(test, pykicadlib.symbol.type.field.temperature)
        self.assertEqual(str(pykicadlib.symbol.type.field.temperature), 'Temperature')

    def test_field_model(self):
        test = pykicadlib.symbol.type.field.from_str('8')
        self.assertEqual(test, pykicadlib.symbol.type.field.model)
        self.assertEqual(str(pykicadlib.symbol.type.field.model), 'Model')

    def test_field_voltage(self):
        test = pykicadlib.symbol.type.field.from_str('9')
        self.assertEqual(test, pykicadlib.symbol.type.field.voltage)
        self.assertEqual(str(pykicadlib.symbol.type.field.voltage), 'Voltage')

    def test_field_power(self):
        test = pykicadlib.symbol.type.field.from_str('10')
        self.assertEqual(test, pykicadlib.symbol.type.field.power)
        self.assertEqual(str(pykicadlib.symbol.type.field.power), 'Power')

    def test_exception(self):
        with self.assertRaises(ValueError):
            pykicadlib.symbol.type.field.from_str('')

        with self.assertRaises(ValueError):
            pykicadlib.symbol.type.field.from_str('A')

        with self.assertRaises(NotImplementedError):
            pykicadlib.symbol.type.field.from_str('11')


class TestSymbolTypeOrientation(unittest.TestCase):
    def test_orientation_horizontal(self):
        test = pykicadlib.symbol.type.orientation.from_str('H')
        self.assertEqual(test, pykicadlib.symbol.type.orientation.horizontal)
        self.assertEqual(str(pykicadlib.symbol.type.orientation.horizontal), 'H')

    def test_orientation_vertical(self):
        test = pykicadlib.symbol.type.orientation.from_str('V')
        self.assertEqual(test, pykicadlib.symbol.type.orientation.vertical)
        self.assertEqual(str(pykicadlib.symbol.type.orientation.vertical), 'V')

    def test_exception(self):
        with self.assertRaises(NotImplementedError):
            pykicadlib.symbol.type.orientation.from_str('')


class TestSymbolTypeVisibility(unittest.TestCase):
    def test_visibility_visible(self):
        test = pykicadlib.symbol.type.visibility.from_str('V')
        self.assertEqual(test, pykicadlib.symbol.type.visibility.visible)
        self.assertEqual(str(pykicadlib.symbol.type.visibility.visible), 'V')

    def test_visibility_invisible(self):
        test = pykicadlib.symbol.type.visibility.from_str('I')
        self.assertEqual(test, pykicadlib.symbol.type.visibility.invisible)
        self.assertEqual(str(pykicadlib.symbol.type.visibility.invisible), 'I')

    def test_exception(self):
        with self.assertRaises(NotImplementedError):
            pykicadlib.symbol.type.visibility.from_str('')


class TestSymbolTypeHJustify(unittest.TestCase):
    def test_hjustify_left(self):
        test = pykicadlib.symbol.type.hjustify.from_str('L')
        self.assertEqual(test, pykicadlib.symbol.type.hjustify.left)
        self.assertEqual(str(pykicadlib.symbol.type.hjustify.left), 'L')

    def test_hjustify_center(self):
        test = pykicadlib.symbol.type.hjustify.from_str('C')
        self.assertEqual(test, pykicadlib.symbol.type.hjustify.center)
        self.assertEqual(str(pykicadlib.symbol.type.hjustify.center), 'C')

    def test_hjustify_right(self):
        test = pykicadlib.symbol.type.hjustify.from_str('R')
        self.assertEqual(test, pykicadlib.symbol.type.hjustify.right)
        self.assertEqual(str(pykicadlib.symbol.type.hjustify.right), 'R')

    def test_exception(self):
        with self.assertRaises(NotImplementedError):
            pykicadlib.symbol.type.hjustify.from_str('')


class TestSymbolTypeVJustify(unittest.TestCase):
    def test_vjustify_top(self):
        test = pykicadlib.symbol.type.vjustify.from_str('T')
        self.assertEqual(test, pykicadlib.symbol.type.vjustify.top)
        self.assertEqual(str(pykicadlib.symbol.type.vjustify.top), 'T')

    def test_vjustify_center(self):
        test = pykicadlib.symbol.type.vjustify.from_str('C')
        self.assertEqual(test, pykicadlib.symbol.type.vjustify.center)
        self.assertEqual(str(pykicadlib.symbol.type.vjustify.center), 'C')

    def test_vjustify_bottom(self):
        test = pykicadlib.symbol.type.vjustify.from_str('B')
        self.assertEqual(test, pykicadlib.symbol.type.vjustify.bottom)
        self.assertEqual(str(pykicadlib.symbol.type.vjustify.bottom), 'B')

    def test_exception(self):
        with self.assertRaises(NotImplementedError):
            pykicadlib.symbol.type.vjustify.from_str('X')


class TestSymbolTypeStyle(unittest.TestCase):
    def test_style_none(self):
        test = pykicadlib.symbol.type.style.from_str('NN')
        self.assertEqual(test, pykicadlib.symbol.type.style.none)
        self.assertEqual(str(pykicadlib.symbol.type.style.none), 'NN')

    def test_style_italic(self):
        test = pykicadlib.symbol.type.style.from_str('IN')
        self.assertEqual(test, pykicadlib.symbol.type.style.italic)
        self.assertEqual(str(pykicadlib.symbol.type.style.italic), 'IN')

    def test_style_bold(self):
        test = pykicadlib.symbol.type.style.from_str('NB')
        self.assertEqual(test, pykicadlib.symbol.type.style.bold)
        self.assertEqual(str(pykicadlib.symbol.type.style.bold), 'NB')

    def test_style_italic_bold(self):
        test = pykicadlib.symbol.type.style.from_str('IB')
        self.assertEqual(test, pykicadlib.symbol.type.style.italic_bold)
        self.assertEqual(str(pykicadlib.symbol.type.style.italic_bold), 'IB')

    def test_exception(self):
        with self.assertRaises(NotImplementedError):
            pykicadlib.symbol.type.style.from_str('')


class TestSymbolTypeFill(unittest.TestCase):
    def test_fill_none(self):
        test = pykicadlib.symbol.type.fill.from_str('N')
        self.assertEqual(test, pykicadlib.symbol.type.fill.none)
        self.assertEqual(str(pykicadlib.symbol.type.fill.none), 'N')

    def test_fill_foreground(self):
        test = pykicadlib.symbol.type.fill.from_str('F')
        self.assertEqual(test, pykicadlib.symbol.type.fill.foreground)
        self.assertEqual(str(pykicadlib.symbol.type.fill.foreground), 'F')

    def test_fill_background(self):
        test = pykicadlib.symbol.type.fill.from_str('f')
        self.assertEqual(test, pykicadlib.symbol.type.fill.background)
        self.assertEqual(str(pykicadlib.symbol.type.fill.background), 'f')

    def test_exception(self):
        with self.assertRaises(NotImplementedError):
            pykicadlib.symbol.type.fill.from_str('')


class TestSymbolTypeRepresentation(unittest.TestCase):
    def test_representation_both(self):
        test = pykicadlib.symbol.type.representation.from_str('0')
        self.assertEqual(test, pykicadlib.symbol.type.representation.both)
        self.assertEqual(str(pykicadlib.symbol.type.representation.both), '0')

    def test_representation_normal(self):
        test = pykicadlib.symbol.type.representation.from_str('1')
        self.assertEqual(test, pykicadlib.symbol.type.representation.normal)

    def test_representation_morgan(self):
        test = pykicadlib.symbol.type.representation.from_str('2')
        self.assertEqual(test, pykicadlib.symbol.type.representation.morgan)

    def test_exception(self):
        with self.assertRaises(ValueError):
            pykicadlib.symbol.type.representation.from_str('')

        with self.assertRaises(ValueError):
            pykicadlib.symbol.type.representation.from_str('A')

        with self.assertRaises(NotImplementedError):
            pykicadlib.symbol.type.representation.from_str('3')


class TestSymbolTypeItalic(unittest.TestCase):
    def test_italic_off(self):
        test = pykicadlib.symbol.type.italic.from_str('Normal')
        self.assertEqual(test, pykicadlib.symbol.type.italic.off)
        self.assertEqual(str(pykicadlib.symbol.type.italic.off), 'Normal')

    def test_italic_on(self):
        test = pykicadlib.symbol.type.italic.from_str('Italic')
        self.assertEqual(test, pykicadlib.symbol.type.italic.on)
        self.assertEqual(str(pykicadlib.symbol.type.italic.on), 'Italic')

    def test_exception(self):
        with self.assertRaises(NotImplementedError):
            pykicadlib.symbol.type.italic.from_str('')


class TestSymbolTypeBold(unittest.TestCase):
    def test_bold_off(self):
        test = pykicadlib.symbol.type.bold.from_str('0')
        self.assertEqual(test, pykicadlib.symbol.type.bold.off)
        self.assertEqual(str(pykicadlib.symbol.type.bold.off), '0')

    def test_bold_on(self):
        test = pykicadlib.symbol.type.bold.from_str('1')
        self.assertEqual(test, pykicadlib.symbol.type.bold.on)
        self.assertEqual(str(pykicadlib.symbol.type.bold.on), '1')

    def test_exception(self):
        with self.assertRaises(ValueError):
            pykicadlib.symbol.type.bold.from_str('')

        with self.assertRaises(ValueError):
            pykicadlib.symbol.type.bold.from_str('A')

        with self.assertRaises(NotImplementedError):
            pykicadlib.symbol.type.bold.from_str('2')


class TestSymbolTypeDirection(unittest.TestCase):
    def test_direction_up(self):
        # NOTE: Definition of directions in KiCAD is flipped! We test against corrected definition!
        test = pykicadlib.symbol.type.direction.from_str('D')
        self.assertEqual(test, pykicadlib.symbol.type.direction.up)
        self.assertEqual(str(pykicadlib.symbol.type.direction.up), 'D')

    def test_direction_down(self):
        test = pykicadlib.symbol.type.direction.from_str('U')
        self.assertEqual(test, pykicadlib.symbol.type.direction.down)
        self.assertEqual(str(pykicadlib.symbol.type.direction.down), 'U')

    def test_direction_left(self):
        test = pykicadlib.symbol.type.direction.from_str('R')
        self.assertEqual(test, pykicadlib.symbol.type.direction.left)
        self.assertEqual(str(pykicadlib.symbol.type.direction.left), 'R')

    def test_direction_right(self):
        test = pykicadlib.symbol.type.direction.from_str('L')
        self.assertEqual(test, pykicadlib.symbol.type.direction.right)
        self.assertEqual(str(pykicadlib.symbol.type.direction.right), 'L')

    def test_exception(self):
        with self.assertRaises(NotImplementedError):
            pykicadlib.symbol.type.direction.from_str('')


class TestSymbolTypeElectric(unittest.TestCase):
    def test_electric_input(self):
        test = pykicadlib.symbol.type.electric.from_str('I')
        self.assertEqual(test, pykicadlib.symbol.type.electric.input)
        self.assertEqual(str(pykicadlib.symbol.type.electric.input), 'I')

    def test_electric_output(self):
        test = pykicadlib.symbol.type.electric.from_str('O')
        self.assertEqual(test, pykicadlib.symbol.type.electric.output)
        self.assertEqual(str(pykicadlib.symbol.type.electric.output), 'O')

    def test_electric_bidirectional(self):
        test = pykicadlib.symbol.type.electric.from_str('B')
        self.assertEqual(test, pykicadlib.symbol.type.electric.bidirectional)
        self.assertEqual(str(pykicadlib.symbol.type.electric.bidirectional), 'B')

    def test_electric_tristate(self):
        test = pykicadlib.symbol.type.electric.from_str('T')
        self.assertEqual(test, pykicadlib.symbol.type.electric.tristate)
        self.assertEqual(str(pykicadlib.symbol.type.electric.tristate), 'T')

    def test_electric_passive(self):
        test = pykicadlib.symbol.type.electric.from_str('P')
        self.assertEqual(test, pykicadlib.symbol.type.electric.passive)
        self.assertEqual(str(pykicadlib.symbol.type.electric.passive), 'P')

    def test_electric_unspecified(self):
        test = pykicadlib.symbol.type.electric.from_str('U')
        self.assertEqual(test, pykicadlib.symbol.type.electric.unspecified)
        self.assertEqual(str(pykicadlib.symbol.type.electric.unspecified), 'U')

    def test_electric_power_input(self):
        test = pykicadlib.symbol.type.electric.from_str('W')
        self.assertEqual(test, pykicadlib.symbol.type.electric.power_input)
        self.assertEqual(str(pykicadlib.symbol.type.electric.power_input), 'W')

    def test_electric_power_output(self):
        test = pykicadlib.symbol.type.electric.from_str('w')
        self.assertEqual(test, pykicadlib.symbol.type.electric.power_output)
        self.assertEqual(str(pykicadlib.symbol.type.electric.power_output), 'w')

    def test_electric_open_collector(self):
        test = pykicadlib.symbol.type.electric.from_str('C')
        self.assertEqual(test, pykicadlib.symbol.type.electric.open_collector)
        self.assertEqual(str(pykicadlib.symbol.type.electric.open_collector), 'C')

    def test_electric_open_emitter(self):
        test = pykicadlib.symbol.type.electric.from_str('E')
        self.assertEqual(test, pykicadlib.symbol.type.electric.open_emitter)
        self.assertEqual(str(pykicadlib.symbol.type.electric.open_emitter), 'E')

    def test_electric_not_connected(self):
        test = pykicadlib.symbol.type.electric.from_str('N')
        self.assertEqual(test, pykicadlib.symbol.type.electric.not_connected)
        self.assertEqual(str(pykicadlib.symbol.type.electric.not_connected), 'N')

    def test_exception(self):
        with self.assertRaises(NotImplementedError):
            pykicadlib.symbol.type.electric.from_str('')


class TestSymbolTypeShape(unittest.TestCase):
    def test_shape_line(self):
        test = pykicadlib.symbol.type.shape.from_str('')
        self.assertEqual(test, pykicadlib.symbol.type.shape.line)
        self.assertEqual(str(pykicadlib.symbol.type.shape.line), '')

    def test_shape_invisible(self):
        test = pykicadlib.symbol.type.shape.from_str('N')
        self.assertEqual(test, pykicadlib.symbol.type.shape.invisible)
        self.assertEqual(str(pykicadlib.symbol.type.shape.invisible), 'N')

    def test_shape_inverted(self):
        test = pykicadlib.symbol.type.shape.from_str('I')
        self.assertEqual(test, pykicadlib.symbol.type.shape.inverted)
        self.assertEqual(str(pykicadlib.symbol.type.shape.inverted), 'I')

    def test_shape_clock(self):
        test = pykicadlib.symbol.type.shape.from_str('C')
        self.assertEqual(test, pykicadlib.symbol.type.shape.clock)
        self.assertEqual(str(pykicadlib.symbol.type.shape.clock), 'C')

    def test_shape_inverted_clock(self):
        test = pykicadlib.symbol.type.shape.from_str('CI')
        self.assertEqual(test, pykicadlib.symbol.type.shape.inverted_clock)
        self.assertEqual(str(pykicadlib.symbol.type.shape.inverted_clock), 'CI')

    def test_shape_input_low(self):
        test = pykicadlib.symbol.type.shape.from_str('L')
        self.assertEqual(test, pykicadlib.symbol.type.shape.input_low)
        self.assertEqual(str(pykicadlib.symbol.type.shape.input_low), 'L')

    def test_shape_power_clock_low(self):
        test = pykicadlib.symbol.type.shape.from_str('CL')
        self.assertEqual(test, pykicadlib.symbol.type.shape.clock_low)
        self.assertEqual(str(pykicadlib.symbol.type.shape.clock_low), 'CL')

    def test_shape_power_output_low(self):
        test = pykicadlib.symbol.type.shape.from_str('V')
        self.assertEqual(test, pykicadlib.symbol.type.shape.output_low)
        self.assertEqual(str(pykicadlib.symbol.type.shape.output_low), 'V')

    def test_shape_open_falling_edge_clock(self):
        test = pykicadlib.symbol.type.shape.from_str('F')
        self.assertEqual(test, pykicadlib.symbol.type.shape.falling_edge_clock)
        self.assertEqual(str(pykicadlib.symbol.type.shape.falling_edge_clock), 'F')

    def test_shape_open_non_logic(self):
        test = pykicadlib.symbol.type.shape.from_str('X')
        self.assertEqual(test, pykicadlib.symbol.type.shape.non_logic)
        self.assertEqual(str(pykicadlib.symbol.type.shape.non_logic), 'X')

    def test_exception(self):
        with self.assertRaises(NotImplementedError):
            pykicadlib.symbol.type.shape.from_str('A')
