# pylint: disable=too-many-instance-attributes, too-few-public-methods
"""KiCAD symbol library.

.. py::module:: pykicadlib.symbol.library
   :synopsis: KiCAD symbol library

.. moduleauthor:: Benjamin Füldner <benjamin@fueldner.net>
"""

import re
import csv
from enum import Enum

# import pykicadlib
from pykicadlib.config import Symbol as Config
from pykicadlib.symbol.elements import Field, Pin, Polygon, Rectangle, Text
from pykicadlib.symbol.boundary import Boundary
from pykicadlib.symbol.elements.from_str import from_str as elements_from_str
from pykicadlib.symbol.decorator import Registry


class Symbol():
    """KiCAD symbol class.

    :param str name:
        Symbol name
    :param str reference:
        Symbol reference designator
    :param str footprint:
        Symbol footprint
    :param str document:
        Symbol document or datasheet
    :param str alias:
        Symbol alias(es)
    """

    from pykicadlib.symbol.types import Flag, Units, Visible

    # pylint: disable=too-many-arguments
    def __init__(self, name, reference, footprint, document, alias=''):
        """Constructor."""
        self.name = name
        self.reference = reference
        self.footprint = footprint
        self.document = document
        self.alias = alias.split()
        self.offset = 0
        self.pinnumber = Symbol.Visible.no
        self.pinname = Symbol.Visible.no
        self.fields = []
        self.elements = []

        self.templates = 0
        self.tables = 0
        self.decorated = False

    # pylint: disable=too-many-branches
    def optimize(self):
        """Merge duplicate graphical elements into unit = 0."""
        # We need at least two elements to optimize
        if len(self.elements) < 2:
            return

        # First: Compare all elements agains each other and mark same elements with a id
        # Parallel count max used units
        id_ = 1
        unit = 0
        for base in range(len(self.elements) - 1):
            unit = max(unit, self.elements[base].unit)
            for compare in range(base + 1, len(self.elements)):
                if isinstance(self.elements[base], type(self.elements[compare])) and \
                              self.elements[base] == self.elements[compare]:
                    if self.elements[base].id is not None:
                        self.elements[compare].id = self.elements[base].id
                    else:
                        self.elements[base].id = id_
                        self.elements[compare].id = id_
                        id_ += 1

        # Second: Count equal elements
        for id_ in range(1, id_):
            count = 1
            for index in range(len(self.elements)):
                if self.elements[index].id == id_:
                    self.elements[index].count = count
                    count += 1

        # Correct values after loop
        id_ += 1

        # Third: Delete all elements with id that get counter to max units
        for id_ in range(1, id_):
            unique = False
            for index in range(len(self.elements) - 1, -1, -1):
                if self.elements[index].id == id_:
                    if unique:
                        del self.elements[index]
                    elif self.elements[index].count >= unit:
                        self.elements[index].unit = 0
                        unique = True

    def sort(self):
        """Sort fields and elements according to their priority."""
        self.fields.sort(key=lambda field: field.type.value)
        self.elements.sort(key=lambda element: element.priority)

    def from_map(self, mapping, unit=0):
        """Add fields from map."""
        # Take fields only for unit zero or one
        if unit in (0, 1):
            # Iterate over fields and add field element, if found in map
            for field_type in Field.Type:
                if field_type.name in mapping:
                    field = Field(field_type, mapping[field_type.name], 0, 0)
                    if field_type not in (Field.Type.footprint, Field.Type.document):
                        field.visibility = Field.Visibility.invisible

                    self.fields.append(field)

    def from_file(self, filename, mapping, unit=0, unify=True):
        """Read symbol from file.

        Replace "$key" text with value from map and unify text sizes if required.

        :param str filename:
            xxx
        :param ??? mapping:
            xxx
        :param int unit:
            Unit number for symbol
        :param bool unify:
            Unify symbol elements with pykicadlib.config
        """
        file = open(filename, 'r')
        self.from_str(file.read(), mapping, unit, unify)
        file.close()

    # pylint: disable=too-many-branches
    def from_str(self, text, mapping, unit=0, unify=True):
        """Read symbol from ``text``.

        Replace "$key" text with value from map and unify text sizes if required.

        :param str text:
            Text symbol is parsed from
        :param Dict mapping:
            Dictionary to replace ``$KEYs` with ``values``
        :param int unit:
            Unit number for symbol
        :param bool unify:
            Unify symbol elements with pykicadlib.config
        """
        # Strings are templates, so we increment
        self.templates += 1

        class Position(Enum):
            """Parser position."""

            unknown = 0
            definition = 1
            drawing = 2

        # Remove comment lines
        text = re.sub(r'^#.*$\s*', '', text, flags=re.MULTILINE)
        # print(text)

        # Replace $KEYWORD with mapped value
        for key, value in mapping.items():
            if not isinstance(value, str):
                mapping[key] = str(value)

        text = re.sub(
            r'\$(\w+)',
            lambda match: mapping[match.group(1).lower()]
            if match.group(1).lower() in mapping else match.group(1), text)

        # Parse library file
        parser = Position.unknown
        for line in text.splitlines():
            key = line.split(' ', 1)[0]

            # Start of library
            if key == 'EESchema-LIBRARY':
                part = line.split()
                if len(part) != 3 or part[1] != 'Version':
                    raise ValueError('File does not look like a EESchema Library')
                version = part[2].split('.')
                version = [int(value) for value in version]
                if version[0] != 2:
                    raise ValueError('Currently only EESchema Library with \
                                      major version 2 supported!')
                if version[1] > 4:
                    print('WARNING: We only know EESchema Library until version 2.4. Upper \
                           versions are experimental!')

            elif key == 'DEF':
                part = line.split()
                if len(part) != 10:
                    raise ValueError('DEF line has too less parts')

                # Only use symbol properties and fields, if unit is global (0) or first unit
                if unit in (0, 1):
                    # self.name = part[1]
                    # self.reference = part[2]
                    self.offset = int(part[4])
                    self.pinnumber = Symbol.Visible.from_str(part[5])
                    self.pinname = Symbol.Visible.from_str(part[6])
                    # self.units = pykicadlib.symbol.types.units.from_str(part[8])
                    # self.flag = pykicadlib.symbol.types.flag.from_str(part[9])
                    parser = Position.definition
            elif key == 'ALIAS':
                pass
            elif key == 'DRAW':
                parser = Position.drawing
            elif key == 'ENDDRAW':
                parser = Position.unknown
            elif key == 'ENDDEF':
                parser = Position.unknown
            elif parser == Position.drawing:
                # Elements, fields are ignored!
                element = elements_from_str(line, unify)
                element.unit = unit
                self.elements.append(element)

    # pylint: disable=too-many-locals, too-many-branches, too-many-statements
    def from_csv(self, filename, mapping, unit=0):
        """Create symbol from comma separated value table.

        :param str filename:
            Filename to CSV table
        :param Dict mapping:
            Dictionary to replace ``$KEYs` with ``values``
        :param int unit:
            Unit for symbol
        """
        # Increment table counter
        self.tables += 1

        def create_pins(x, y, step_x, step_y, data, direction):
            """Create array of pins for one direction."""
            result = []

            name = None
            length = 0
            last_x = 0
            last_y = 0

            # Calculate pin and line offsets
            if direction in (Pin.Direction.left, Pin.Direction.right):
                pin_offset_x = -Config.PIN_LENGTH
                pin_offset_y = 0
                line_offset_x = int(Config.PIN_OFFSET * 0.75)
                line_offset_y = 0
            elif direction in (Pin.Direction.up, Pin.Direction.down):
                pin_offset_x = 0
                pin_offset_y = Config.PIN_LENGTH
                line_offset_x = 0
                line_offset_y = -int(Config.PIN_OFFSET * 0.75)

            # Correct offset depending on pin direction
            if direction in (Pin.Direction.right, Pin.Direction.down):
                pin_offset_x = -pin_offset_x
                pin_offset_y = -pin_offset_y
                line_offset_x = -line_offset_x
                line_offset_y = -line_offset_y

            for item in data:
                # Check for same pin names
                if item['name'] and item['name'] != '~' and name == item['name']:
                    length += 1
                else:
                    # Draw line if equal pins follow each other
                    if length:
                        start_x = int(last_x + step_x * (length + 0.25))
                        start_y = int(last_y + step_y * (length + 0.25))
                        end_x = int(last_x - step_x * 0.25)
                        end_y = int(last_y - step_y * 0.25)

                        line = Polygon()
                        line.thickness = Config.DECORATION_THICKNESS
                        line.unit = unit
                        line.add(Polygon.Point(start_x + line_offset_x, start_y + line_offset_y))
                        line.add(Polygon.Point(end_x + line_offset_x, end_y + line_offset_y))
                        result.append(line)

                    name = item['name']
                    length = 0
                    last_x = x
                    last_y = y

                if item['name']:
                    pin = Pin(
                        x + pin_offset_x,
                        y + pin_offset_y,
                        item['name'] if length == 0 else '~',
                        item['number']
                    )
                    pin.length = Config.PIN_LENGTH
                    pin.direction = direction
                    pin.electric = Pin.Electric.from_name(item['electric'])
                    pin.shape = Pin.Shape.from_name(item['shape'])
                    pin.unit = unit

                    result.append(pin)

                x += step_x
                y += step_y

            # Draw line if equal pins follow each other
            if length:
                start_x = int(last_x + step_x * (length + 0.25))
                start_y = int(last_y + step_y * (length + 0.25))
                end_x = int(last_x - step_x * 0.25)
                end_y = int(last_y - step_y * 0.25)

                line = Polygon()
                line.thickness = Config.DECORATION_THICKNESS
                line.unit = unit
                line.add(Polygon.Point(start_x + line_offset_x, start_y + line_offset_y))
                line.add(Polygon.Point(end_x + line_offset_x, end_y + line_offset_y))
                result.append(line)
            return result

        # Load pins and pinname size and order them by direction
        pins = {}
        size = {}
        for direction in Pin.Direction:
            pins[direction] = []
            size[direction] = 0

        with open(filename, 'r') as csvfile:
            table = csv.reader(csvfile, delimiter=',', quotechar='\"')

            first_row = True
            for row in table:
                if first_row:
                    header = row
                    first_row = False
                else:
                    data = dict(zip(header, row))

                    # Order pins by direction
                    direction = Pin.Direction.from_name(data['direction'])
                    pins[direction].append(data)
                    if data['name'] and data['name'] != '~':
                        size[direction] = max(
                            size[direction],
                            Config.PIN_OFFSET +
                            len(data['name'].replace('~', '')) *
                            Config.PIN_NAME_SIZE)

        # Set default size
        for direction in Pin.Direction:
            if pins[direction]:
                if direction in (Pin.Direction.left, Pin.Direction.right):
                    size[direction] = max(size[direction], Config.PIN_GRID * 2)
                else:
                    size[direction] = max(size[direction], Config.PIN_GRID * 1.5)

        # Adjust left and right pin count to satisfy zip function
        left_right_diff = len(pins[Pin.Direction.left]) - len(pins[Pin.Direction.right])
        if left_right_diff > 0:
            pins[Pin.Direction.right].extend([{'name': ''}] * left_right_diff)
        elif left_right_diff < 0:
            pins[Pin.Direction.left].extend([{'name': ''}] * -left_right_diff)

        # Two grid spaces above first pin and below last pin
        height = (max(
            len(pins[Pin.Direction.left]),
            len(pins[Pin.Direction.right])) + 1) * Config.PIN_GRID
        height = max(height, Config.PIN_GRID * 3)
        if pins[Pin.Direction.up] and pins[Pin.Direction.down]:
            height = max(height, Config.PIN_GRID * 4)

        width = size[Pin.Direction.left] + size[Pin.Direction.right]
        if mapping['section']:
            width = max(
                width,
                Config.PIN_GRID + len(mapping['section']) *
                Config.FIELD_TEXT_SIZE)

        if width == 0:
            width = (max(
                len(pins[Pin.Direction.up]),
                len(pins[Pin.Direction.down])) + 1) * Config.PIN_GRID

        # Round up to next grid
        width = (((width + (Config.PIN_GRID - 1)) // (Config.PIN_GRID)) * Config.PIN_GRID)

        center_x = 0
        center_y = 0
        width_half = width // 2
        height_half = height // 2

        rectangle = Rectangle(
            center_x - width_half,
            center_y - height_half,
            center_x + width_half,
            center_y + height_half
        )
        rectangle.fill = Rectangle.Fill.background
        rectangle.unit = unit
        self.elements.append(rectangle)

        if len(pins[Pin.Direction.up]) > 1:
            up_x = (len(pins[Pin.Direction.up]) - 1) * \
                Config.PIN_GRID // 2
        else:
            up_x = 0

        if len(pins[Pin.Direction.down]) > 1:
            down_x = (len(pins[Pin.Direction.down]) - 1) * \
                Config.PIN_GRID // 2
        else:
            down_x = 0

        self.elements.extend(
            create_pins(
                center_x - width_half,
                center_y + height_half - Config.PIN_GRID,
                0,
                -Config.PIN_GRID,
                pins[Pin.Direction.left],
                Pin.Direction.left
            )
        )
        self.elements.extend(
            create_pins(
                center_x + width_half,
                center_y + height_half - Config.PIN_GRID,
                0,
                -Config.PIN_GRID,
                pins[Pin.Direction.right],
                Pin.Direction.right
            )
        )
        self.elements.extend(
            create_pins(
                center_x - up_x,
                center_y + height_half,
                Config.PIN_GRID,
                0,
                pins[Pin.Direction.up],
                Pin.Direction.up
            )
        )
        self.elements.extend(
            create_pins(
                center_x - down_x,
                center_y - height_half,
                Config.PIN_GRID,
                0,
                pins[Pin.Direction.down],
                Pin.Direction.down
            )
        )

        # Add decoration
        for direction in (Pin.Direction.left,
                          Pin.Direction.right):
            y = center_y + height_half - Config.PIN_GRID
            for item in pins[direction]:
                if 'decoration' in item and item['decoration']:
                    if item['decoration'] in Registry.decorator.keys():
                        sign = -1 if direction == Pin.Direction.left else 1
                        decorator = Registry.decorator[item['decoration']](
                            center_x + sign * width_half, y, direction, unit)
                        self.elements.extend(decorator.elements)
                        self.decorated = True
                    else:
                        print("Warning: Unknown decorator '{}'".format(item['decoration']))
                y -= Config.PIN_GRID

        # Add line between empty pin slots on left and right side
        y = center_y + height_half - Config.PIN_GRID
        for left, right in zip(pins[Pin.Direction.left], pins[Pin.Direction.right]):
            if not left['name'] and not right['name']:
                line = Polygon()
                line.thickness = Config.DECORATION_THICKNESS
                line.unit = unit
                line.add(Polygon.Point(center_x - width_half, y))
                line.add(Polygon.Point(center_x + width_half, y))
                self.elements.append(line)
            y -= Config.PIN_GRID

        # Section name right top corner
        if mapping['section']:
            text = Text(
                center_x + width_half - Config.PIN_GRID // 2,
                center_y + height_half - Config.PIN_GRID // 2,
                mapping['section'],
                Config.FIELD_TEXT_SIZE
            )
            text.hjustify = Text.HJustify.right
            text.vjustify = Text.VJustify.top
            text.unit = unit
            self.elements.append(text)

    def __str__(self):
        """Render symbol into string with some automatics."""
        # Count device pins
        direction_pins = {}
        for direction in Pin.Direction:
            direction_pins[direction] = 0

        # Collect number of units and their pins used in symbol
        unit_pins = {}
        unit_count = 1
        bounds = Boundary(0, 0, 0, 0)
        pinname = Symbol.Visible.no
        for element in self.elements:
            unit_count = max(unit_count, element.unit)
            bounds += element.bounds
            if isinstance(element, Pin):
                if element.name != '~':
                    pinname = Symbol.Visible.yes

                if element.unit in unit_pins:
                    unit_pins[element.unit] += 1
                else:
                    unit_pins[element.unit] = 1
                direction_pins[element.direction] += 1

        # Override pinname visibility on table based symbol
        if self.tables:
            self.pinname = pinname

        # Table generated symbol have their pin names inside,
        # if pin names exists and no decorators are used
        if self.tables and not self.decorated and \
           self.pinname == Symbol.Visible.yes:
            self.offset = Config.PIN_OFFSET

        # Set pin name offset to zero, if pin names not visible
        if self.pinname == Symbol.Visible.no:
            self.offset = 0

        # Pin numbers are visible, if symbol has more than one unit or was table generated
        if (self.templates and unit_count > 1) or self.tables:
            self.pinnumber = Symbol.Visible.yes

        # Check, if every unit has same number of pins. Then units should be swappable!
        units = Symbol.Units.locked
        if unit_pins and 0 not in unit_pins and min(unit_pins.values()) == max(unit_pins.values()):
            units = Symbol.Units.swappable

        # If reference matches POWER_SYMBOL_REFERENCE, than we have a power symbol
        flag = Symbol.Flag.normal
        if self.reference in Config.POWER_SYMBOL_REFERENCE:
            flag = Symbol.Flag.power

        # Overwrite fields with symbol parameters
        for field in self.fields:
            if field.type == Field.Type.name:
                field.value = self.name
            elif field.type == Field.Type.reference:
                field.value = self.reference

                # Hide reference field, if reference starts with #
                if self.reference[0] == '#':
                    field.visibility = Field.Visibility.invisible
            elif field.type == Field.Type.footprint:
                field.value = self.footprint
            elif field.type == Field.Type.document:
                field.value = self.document

        # Reposition visible fields
        y = bounds.y1
        for field in self.fields:
            if field.visibility == Field.Visibility.visible:
                y -= Config.PIN_GRID
                field.x = 0
                field.y = y

        # Reposition invisible fields
        for field in self.fields:
            if field.visibility == Field.Visibility.invisible:
                y -= Config.PIN_GRID
                field.x = 0
                field.y = y

        # Render symbol
        result = '#\n# {:s}\n#\n'.format(self.name)
        result += 'DEF {:s} {:s} 0 {:d} {:s} {:s} {:d} {:s} {:s}\n'.format(
            self.name, self.reference, self.offset, self.pinnumber, self.pinname,
            unit_count, units, flag)

        if self.alias:
            result += 'ALIAS {:s}\n'.format(' '.join(self.alias))

        for field in self.fields:
            if field.value:
                result += str(field) + '\n'

        result += 'DRAW\n'
        for element in self.elements:
            result += str(element) + '\n'
        result += 'ENDDRAW\nENDDEF\n'
        return result


class Symbols():
    """List of symbols."""

    def __init__(self):
        """Constructor."""
        self.symbol = []    #: List of :class:`Symbol`

    def add(self, symbol):
        """Add :class:`Symbol` to object.

        :param Symbol symbol:
            Symbol to add
        """
        self.symbol.append(symbol)

    def __str__(self):
        """Return :class:`Symbols` in KiCAD format."""
        result = Config.LIBRARY_START
        for symbol in self.symbol:
            result += str(symbol)
        result += Config.LIBRARY_END
        return result


class Description():
    """KiCAD symbol description class."""

    def __init__(self, name, description, keywords, document):
        """Constructor."""
        self.name = name                    #: Name
        self.description = description.replace('\r', '').replace('\n', ' ')     #: Description
        self.keywords = keywords.split()    #: Keyworkds
        self.document = document            #: Document

    def __str__(self):
        """Return :class:`Description` in KiCAD format."""
        result = '#\n$CMP {}\n'.format(self.name)
        if self.description:
            result += 'D {}\n'.format(self.description)

        if self.keywords:
            result += 'K {}\n'.format(' '.join(self.keywords))

        if self.document:
            result += 'F {}\n'.format(self.document)
        result += '$ENDCMP\n'
        return result


class Descriptions():
    """List of symbol descriptions."""

    def __init__(self):
        """Constructor."""
        self.descriptions = []  #: List of :class:`Description`

    def add(self, description):
        """Add :class:`Description` to object.

        :param Description description:
            Description to add
        """
        self.descriptions.append(description)

    def __str__(self):
        """Return :class:`Descriptions` in KiCAD format."""
        result = Config.DESCRIPTION_START
        for descriptions in self.descriptions:
            result += str(descriptions)
        result += Config.DESCRIPTION_END
        return result
