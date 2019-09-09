import unittest
import pykicad.symbols.type


class TestSymbolTypeVisible(unittest.TestCase):

    def test_visible_no(self):
        test = pykicad.symbols.type.visible.from_str('N')
        self.assertEqual(test, pykicad.symbols.type.visible.no)
        self.assertEqual(str(pykicad.symbols.type.visible.no), 'N')

    def test_visible_yes(self):
        test = pykicad.symbols.type.visible.from_str('Y')
        self.assertEqual(test, pykicad.symbols.type.visible.yes)
        self.assertEqual(str(pykicad.symbols.type.visible.yes), 'Y')

    def test_exception(self):
        with self.assertRaises(NotImplementedError):
            pykicad.symbols.type.visible.from_str('')


class TestSymbolTypeUnits(unittest.TestCase):
    def test_unitslocked(self):
        test = pykicad.symbols.type.units.from_str('L')
        self.assertEqual(test, pykicad.symbols.type.units.locked)
        self.assertEqual(str(pykicad.symbols.type.units.locked), 'L')

    def test_units_swappable(self):
        test = pykicad.symbols.type.units.from_str('F')
        self.assertEqual(test, pykicad.symbols.type.units.swappable)
        self.assertEqual(str(pykicad.symbols.type.units.swappable), 'F')

    def test_exception(self):
        with self.assertRaises(NotImplementedError):
            pykicad.symbols.type.units.from_str('')


class TestSymbolTypeFlag(unittest.TestCase):
    def test_flag_normal(self):
        test = pykicad.symbols.type.flag.from_str('N')
        self.assertEqual(test, pykicad.symbols.type.flag.normal)
        self.assertEqual(str(pykicad.symbols.type.flag.normal), 'N')

    def test_flag_power(self):
        test = pykicad.symbols.type.flag.from_str('P')
        self.assertEqual(test, pykicad.symbols.type.flag.power)
        self.assertEqual(str(pykicad.symbols.type.flag.power), 'P')

    def test_exception(self):
        with self.assertRaises(NotImplementedError):
            pykicad.symbols.type.flag.from_str('')


class TestSymbolTypeField(unittest.TestCase):
    def test_field_reference(self):
        test = pykicad.symbols.type.field.from_str('0')
        self.assertEqual(test, pykicad.symbols.type.field.reference)
        self.assertEqual(str(pykicad.symbols.type.field.reference), 'Reference')

    def test_field_name(self):
        test = pykicad.symbols.type.field.from_str('1')
        self.assertEqual(test, pykicad.symbols.type.field.name)
        self.assertEqual(str(pykicad.symbols.type.field.name), 'Name')

    def test_field_footprint(self):
        test = pykicad.symbols.type.field.from_str('2')
        self.assertEqual(test, pykicad.symbols.type.field.footprint)
        self.assertEqual(str(pykicad.symbols.type.field.footprint), 'Footprint')

    def test_field_document(self):
        test = pykicad.symbols.type.field.from_str('3')
        self.assertEqual(test, pykicad.symbols.type.field.document)
        self.assertEqual(str(pykicad.symbols.type.field.document), 'Document')

    def test_field_manufacturer(self):
        test = pykicad.symbols.type.field.from_str('4')
        self.assertEqual(test, pykicad.symbols.type.field.manufacturer)
        self.assertEqual(str(pykicad.symbols.type.field.manufacturer), 'Manufacturer')

    def test_field_value(self):
        test = pykicad.symbols.type.field.from_str('5')
        self.assertEqual(test, pykicad.symbols.type.field.value)
        self.assertEqual(str(pykicad.symbols.type.field.value), 'Value')

    def test_field_tolerance(self):
        test = pykicad.symbols.type.field.from_str('6')
        self.assertEqual(test, pykicad.symbols.type.field.tolerance)
        self.assertEqual(str(pykicad.symbols.type.field.tolerance), 'Tolerance')

    def test_field_temperature(self):
        test = pykicad.symbols.type.field.from_str('7')
        self.assertEqual(test, pykicad.symbols.type.field.temperature)
        self.assertEqual(str(pykicad.symbols.type.field.temperature), 'Temperature')

    def test_field_model(self):
        test = pykicad.symbols.type.field.from_str('8')
        self.assertEqual(test, pykicad.symbols.type.field.model)
        self.assertEqual(str(pykicad.symbols.type.field.model), 'Model')

    def test_field_voltage(self):
        test = pykicad.symbols.type.field.from_str('9')
        self.assertEqual(test, pykicad.symbols.type.field.voltage)
        self.assertEqual(str(pykicad.symbols.type.field.voltage), 'Voltage')

    def test_field_power(self):
        test = pykicad.symbols.type.field.from_str('10')
        self.assertEqual(test, pykicad.symbols.type.field.power)
        self.assertEqual(str(pykicad.symbols.type.field.power), 'Power')

    def test_exception(self):
        with self.assertRaises(ValueError):
            pykicad.symbols.type.field.from_str('')

        with self.assertRaises(ValueError):
            pykicad.symbols.type.field.from_str('A')

        with self.assertRaises(NotImplementedError):
            pykicad.symbols.type.field.from_str('11')


class TestSymbolTypeOrientation(unittest.TestCase):
    def test_orientation_horizontal(self):
        test = pykicad.symbols.type.orientation.from_str('H')
        self.assertEqual(test, pykicad.symbols.type.orientation.horizontal)
        self.assertEqual(str(pykicad.symbols.type.orientation.horizontal), 'H')

    def test_orientation_vertical(self):
        test = pykicad.symbols.type.orientation.from_str('V')
        self.assertEqual(test, pykicad.symbols.type.orientation.vertical)
        self.assertEqual(str(pykicad.symbols.type.orientation.vertical), 'V')

    def test_exception(self):
        with self.assertRaises(NotImplementedError):
            pykicad.symbols.type.orientation.from_str('')


class TestSymbolTypeVisibility(unittest.TestCase):
    def test_visibility_visible(self):
        test = pykicad.symbols.type.visibility.from_str('V')
        self.assertEqual(test, pykicad.symbols.type.visibility.visible)
        self.assertEqual(str(pykicad.symbols.type.visibility.visible), 'V')

    def test_visibility_invisible(self):
        test = pykicad.symbols.type.visibility.from_str('I')
        self.assertEqual(test, pykicad.symbols.type.visibility.invisible)
        self.assertEqual(str(pykicad.symbols.type.visibility.invisible), 'I')

    def test_exception(self):
        with self.assertRaises(NotImplementedError):
            pykicad.symbols.type.visibility.from_str('')


class TestSymbolTypeHJustify(unittest.TestCase):
    def test_hjustify_left(self):
        test = pykicad.symbols.type.hjustify.from_str('L')
        self.assertEqual(test, pykicad.symbols.type.hjustify.left)
        self.assertEqual(str(pykicad.symbols.type.hjustify.left), 'L')

    def test_hjustify_center(self):
        test = pykicad.symbols.type.hjustify.from_str('C')
        self.assertEqual(test, pykicad.symbols.type.hjustify.center)
        self.assertEqual(str(pykicad.symbols.type.hjustify.center), 'C')

    def test_hjustify_right(self):
        test = pykicad.symbols.type.hjustify.from_str('R')
        self.assertEqual(test, pykicad.symbols.type.hjustify.right)
        self.assertEqual(str(pykicad.symbols.type.hjustify.right), 'R')

    def test_exception(self):
        with self.assertRaises(NotImplementedError):
            pykicad.symbols.type.hjustify.from_str('')


class TestSymbolTypeVJustify(unittest.TestCase):
    def test_vjustify_top(self):
        test = pykicad.symbols.type.vjustify.from_str('T')
        self.assertEqual(test, pykicad.symbols.type.vjustify.top)
        self.assertEqual(str(pykicad.symbols.type.vjustify.top), 'T')

    def test_vjustify_center(self):
        test = pykicad.symbols.type.vjustify.from_str('C')
        self.assertEqual(test, pykicad.symbols.type.vjustify.center)
        self.assertEqual(str(pykicad.symbols.type.vjustify.center), 'C')

    def test_vjustify_bottom(self):
        test = pykicad.symbols.type.vjustify.from_str('B')
        self.assertEqual(test, pykicad.symbols.type.vjustify.bottom)
        self.assertEqual(str(pykicad.symbols.type.vjustify.bottom), 'B')

    def test_exception(self):
        with self.assertRaises(NotImplementedError):
            pykicad.symbols.type.vjustify.from_str('X')


class TestSymbolTypeStyle(unittest.TestCase):
    def test_style_none(self):
        test = pykicad.symbols.type.style.from_str('NN')
        self.assertEqual(test, pykicad.symbols.type.style.none)
        self.assertEqual(str(pykicad.symbols.type.style.none), 'NN')

    def test_style_italic(self):
        test = pykicad.symbols.type.style.from_str('IN')
        self.assertEqual(test, pykicad.symbols.type.style.italic)
        self.assertEqual(str(pykicad.symbols.type.style.italic), 'IN')

    def test_style_bold(self):
        test = pykicad.symbols.type.style.from_str('NB')
        self.assertEqual(test, pykicad.symbols.type.style.bold)
        self.assertEqual(str(pykicad.symbols.type.style.bold), 'NB')

    def test_style_italic_bold(self):
        test = pykicad.symbols.type.style.from_str('IB')
        self.assertEqual(test, pykicad.symbols.type.style.italic_bold)
        self.assertEqual(str(pykicad.symbols.type.style.italic_bold), 'IB')

    def test_exception(self):
        with self.assertRaises(NotImplementedError):
            pykicad.symbols.type.style.from_str('')


class TestSymbolTypeFill(unittest.TestCase):
    def test_fill_none(self):
        test = pykicad.symbols.type.fill.from_str('N')
        self.assertEqual(test, pykicad.symbols.type.fill.none)
        self.assertEqual(str(pykicad.symbols.type.fill.none), 'N')

    def test_fill_foreground(self):
        test = pykicad.symbols.type.fill.from_str('F')
        self.assertEqual(test, pykicad.symbols.type.fill.foreground)
        self.assertEqual(str(pykicad.symbols.type.fill.foreground), 'F')

    def test_fill_background(self):
        test = pykicad.symbols.type.fill.from_str('f')
        self.assertEqual(test, pykicad.symbols.type.fill.background)
        self.assertEqual(str(pykicad.symbols.type.fill.background), 'f')

    def test_exception(self):
        with self.assertRaises(NotImplementedError):
            pykicad.symbols.type.fill.from_str('')


class TestSymbolTypeRepresentation(unittest.TestCase):
    def test_representation_both(self):
        test = pykicad.symbols.type.representation.from_str('0')
        self.assertEqual(test, pykicad.symbols.type.representation.both)
        self.assertEqual(str(pykicad.symbols.type.representation.both), '0')

    def test_representation_normal(self):
        test = pykicad.symbols.type.representation.from_str('1')
        self.assertEqual(test, pykicad.symbols.type.representation.normal)

    def test_representation_morgan(self):
        test = pykicad.symbols.type.representation.from_str('2')
        self.assertEqual(test, pykicad.symbols.type.representation.morgan)

    def test_exception(self):
        with self.assertRaises(ValueError):
            pykicad.symbols.type.representation.from_str('')

        with self.assertRaises(ValueError):
            pykicad.symbols.type.representation.from_str('A')

        with self.assertRaises(NotImplementedError):
            pykicad.symbols.type.representation.from_str('3')


class TestSymbolTypeItalic(unittest.TestCase):
    def test_italic_off(self):
        test = pykicad.symbols.type.italic.from_str('Normal')
        self.assertEqual(test, pykicad.symbols.type.italic.off)
        self.assertEqual(str(pykicad.symbols.type.italic.off), 'Normal')

    def test_italic_on(self):
        test = pykicad.symbols.type.italic.from_str('Italic')
        self.assertEqual(test, pykicad.symbols.type.italic.on)
        self.assertEqual(str(pykicad.symbols.type.italic.on), 'Italic')

    def test_exception(self):
        with self.assertRaises(NotImplementedError):
            pykicad.symbols.type.italic.from_str('')


class TestSymbolTypeBold(unittest.TestCase):
    def test_bold_off(self):
        test = pykicad.symbols.type.bold.from_str('0')
        self.assertEqual(test, pykicad.symbols.type.bold.off)
        self.assertEqual(str(pykicad.symbols.type.bold.off), '0')

    def test_bold_on(self):
        test = pykicad.symbols.type.bold.from_str('1')
        self.assertEqual(test, pykicad.symbols.type.bold.on)
        self.assertEqual(str(pykicad.symbols.type.bold.on), '1')

    def test_exception(self):
        with self.assertRaises(ValueError):
            pykicad.symbols.type.bold.from_str('')

        with self.assertRaises(ValueError):
            pykicad.symbols.type.bold.from_str('A')

        with self.assertRaises(NotImplementedError):
            pykicad.symbols.type.bold.from_str('2')


class TestSymbolTypeDirection(unittest.TestCase):
    def test_direction_up(self):
        # NOTE: Definition of directions in KiCAD is flipped! We test against corrected definition!
        test = pykicad.symbols.type.direction.from_str('D')
        self.assertEqual(test, pykicad.symbols.type.direction.up)
        self.assertEqual(str(pykicad.symbols.type.direction.up), 'D')

    def test_direction_down(self):
        test = pykicad.symbols.type.direction.from_str('U')
        self.assertEqual(test, pykicad.symbols.type.direction.down)
        self.assertEqual(str(pykicad.symbols.type.direction.down), 'U')

    def test_direction_left(self):
        test = pykicad.symbols.type.direction.from_str('R')
        self.assertEqual(test, pykicad.symbols.type.direction.left)
        self.assertEqual(str(pykicad.symbols.type.direction.left), 'R')

    def test_direction_right(self):
        test = pykicad.symbols.type.direction.from_str('L')
        self.assertEqual(test, pykicad.symbols.type.direction.right)
        self.assertEqual(str(pykicad.symbols.type.direction.right), 'L')

    def test_exception(self):
        with self.assertRaises(NotImplementedError):
            pykicad.symbols.type.direction.from_str('')


class TestSymbolTypeElectric(unittest.TestCase):
    def test_electric_input(self):
        test = pykicad.symbols.type.electric.from_str('I')
        self.assertEqual(test, pykicad.symbols.type.electric.input)
        self.assertEqual(str(pykicad.symbols.type.electric.input), 'I')

    def test_electric_output(self):
        test = pykicad.symbols.type.electric.from_str('O')
        self.assertEqual(test, pykicad.symbols.type.electric.output)
        self.assertEqual(str(pykicad.symbols.type.electric.output), 'O')

    def test_electric_bidirectional(self):
        test = pykicad.symbols.type.electric.from_str('B')
        self.assertEqual(test, pykicad.symbols.type.electric.bidirectional)
        self.assertEqual(str(pykicad.symbols.type.electric.bidirectional), 'B')

    def test_electric_tristate(self):
        test = pykicad.symbols.type.electric.from_str('T')
        self.assertEqual(test, pykicad.symbols.type.electric.tristate)
        self.assertEqual(str(pykicad.symbols.type.electric.tristate), 'T')

    def test_electric_passive(self):
        test = pykicad.symbols.type.electric.from_str('P')
        self.assertEqual(test, pykicad.symbols.type.electric.passive)
        self.assertEqual(str(pykicad.symbols.type.electric.passive), 'P')

    def test_electric_unspecified(self):
        test = pykicad.symbols.type.electric.from_str('U')
        self.assertEqual(test, pykicad.symbols.type.electric.unspecified)
        self.assertEqual(str(pykicad.symbols.type.electric.unspecified), 'U')

    def test_electric_power_input(self):
        test = pykicad.symbols.type.electric.from_str('W')
        self.assertEqual(test, pykicad.symbols.type.electric.power_input)
        self.assertEqual(str(pykicad.symbols.type.electric.power_input), 'W')

    def test_electric_power_output(self):
        test = pykicad.symbols.type.electric.from_str('w')
        self.assertEqual(test, pykicad.symbols.type.electric.power_output)
        self.assertEqual(str(pykicad.symbols.type.electric.power_output), 'w')

    def test_electric_open_collector(self):
        test = pykicad.symbols.type.electric.from_str('C')
        self.assertEqual(test, pykicad.symbols.type.electric.open_collector)
        self.assertEqual(str(pykicad.symbols.type.electric.open_collector), 'C')

    def test_electric_open_emitter(self):
        test = pykicad.symbols.type.electric.from_str('E')
        self.assertEqual(test, pykicad.symbols.type.electric.open_emitter)
        self.assertEqual(str(pykicad.symbols.type.electric.open_emitter), 'E')

    def test_electric_not_connected(self):
        test = pykicad.symbols.type.electric.from_str('N')
        self.assertEqual(test, pykicad.symbols.type.electric.not_connected)
        self.assertEqual(str(pykicad.symbols.type.electric.not_connected), 'N')

    def test_exception(self):
        with self.assertRaises(NotImplementedError):
            pykicad.symbols.type.electric.from_str('')


class TestSymbolTypeShape(unittest.TestCase):
    def test_shape_line(self):
        test = pykicad.symbols.type.shape.from_str('')
        self.assertEqual(test, pykicad.symbols.type.shape.line)
        self.assertEqual(str(pykicad.symbols.type.shape.line), '')

    def test_shape_invisible(self):
        test = pykicad.symbols.type.shape.from_str('N')
        self.assertEqual(test, pykicad.symbols.type.shape.invisible)
        self.assertEqual(str(pykicad.symbols.type.shape.invisible), 'N')

    def test_shape_inverted(self):
        test = pykicad.symbols.type.shape.from_str('I')
        self.assertEqual(test, pykicad.symbols.type.shape.inverted)
        self.assertEqual(str(pykicad.symbols.type.shape.inverted), 'I')

    def test_shape_clock(self):
        test = pykicad.symbols.type.shape.from_str('C')
        self.assertEqual(test, pykicad.symbols.type.shape.clock)
        self.assertEqual(str(pykicad.symbols.type.shape.clock), 'C')

    def test_shape_inverted_clock(self):
        test = pykicad.symbols.type.shape.from_str('CI')
        self.assertEqual(test, pykicad.symbols.type.shape.inverted_clock)
        self.assertEqual(str(pykicad.symbols.type.shape.inverted_clock), 'CI')

    def test_shape_input_low(self):
        test = pykicad.symbols.type.shape.from_str('L')
        self.assertEqual(test, pykicad.symbols.type.shape.input_low)
        self.assertEqual(str(pykicad.symbols.type.shape.input_low), 'L')

    def test_shape_power_clock_low(self):
        test = pykicad.symbols.type.shape.from_str('CL')
        self.assertEqual(test, pykicad.symbols.type.shape.clock_low)
        self.assertEqual(str(pykicad.symbols.type.shape.clock_low), 'CL')

    def test_shape_power_output_low(self):
        test = pykicad.symbols.type.shape.from_str('V')
        self.assertEqual(test, pykicad.symbols.type.shape.output_low)
        self.assertEqual(str(pykicad.symbols.type.shape.output_low), 'V')

    def test_shape_open_falling_edge_clock(self):
        test = pykicad.symbols.type.shape.from_str('F')
        self.assertEqual(test, pykicad.symbols.type.shape.falling_edge_clock)
        self.assertEqual(str(pykicad.symbols.type.shape.falling_edge_clock), 'F')

    def test_shape_open_non_logic(self):
        test = pykicad.symbols.type.shape.from_str('X')
        self.assertEqual(test, pykicad.symbols.type.shape.non_logic)
        self.assertEqual(str(pykicad.symbols.type.shape.non_logic), 'X')

    def test_exception(self):
        with self.assertRaises(NotImplementedError):
            pykicad.symbols.type.shape.from_str('A')
