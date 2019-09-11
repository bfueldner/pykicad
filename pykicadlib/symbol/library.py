import re
import csv
from enum import Enum

import pykicadlib
import pykicadlib.config


class symbol(object):
    '''KiCAD symbol class'''

    def __init__(self, name, reference, footprint, document, alias = ''): #, offset = 0, fields = [], elements = []):
        self.name = name
        self.reference = reference
        self.footprint = footprint
        self.document = document
        self.alias = alias.split()
        self.offset = 0
        self.pinnumber = pykicadlib.symbol.type.visible.no
        self.pinname = pykicadlib.symbol.type.visible.no
        self.fields = []
        self.elements = []

        self.templates = 0
        self.tables = 0
        self.decorated = False

    def optimize(self):
        '''Merge duplicate graphical elements into unit = 0'''

        # We need at least two elements to optimize
        if len(self.elements) < 2:
            return

        # First: Compare all elements agains each other and mark same elements with a id
        # Parallel count max used units
        id = 1
        unit = 0
        for base in range(len(self.elements) - 1):
            unit = max(unit, self.elements[base].unit)
            for compare in range(base + 1, len(self.elements)):
                if self.elements[base] == self.elements[compare]:
                    if self.elements[base].id is not None:
                        self.elements[compare].id = self.elements[base].id
                    else:
                        self.elements[base].id = id
                        self.elements[compare].id = id
                        id += 1

        # Second: Count equal elements
        for id in range(1, id):
            count = 1
            for index in range(len(self.elements)):
                if self.elements[index].id == id:
                    self.elements[index].count = count
                    count += 1

         # Correct values after loop
        id += 1

        # Third: Delete all elements with id that get counter to max units
        for id in range(1, id):
            unique = False
            for index in range(len(self.elements) - 1, -1, -1):
                if self.elements[index].id == id:
                    if unique:
                        del self.elements[index]
                    elif self.elements[index].count >= unit:
                        self.elements[index].unit = 0
                        unique = True

    def sort(self):
        '''Sort fields and elements according to their priority'''

        self.fields.sort(key = lambda field: field.type.value)
        self.elements.sort(key = lambda element: element.priority)

    def from_map(self, map, unit = 0):
        '''Add fields from map'''

        # Take fields only for unit zero or one
        if unit <= 1:
            # Iterate over fields and add field element, if found in map
            for field in pykicadlib.symbol.type.field:
                if field.name in map:
                    self.fields.append(
                        pykicadlib.symbol.element.field(
                            field,
                            map[field.name],
                            0,
                            0,
                            pykicadlib.config.symbol.FIELD_TEXT_SIZE,
                            pykicadlib.symbol.type.orientation.horizontal,
                            pykicadlib.symbol.type.visibility.invisible if field == pykicadlib.symbol.type.field.footprint or field == pykicadlib.symbol.type.field.document else pykicadlib.symbol.type.visibility.visible,
                            pykicadlib.symbol.type.hjustify.center,
                            pykicadlib.symbol.type.vjustify.center,
                            pykicadlib.symbol.type.style.none
                        )
                    )

    def from_file(self, filename, map, unit = 0, unify = True):
        '''Read symbol from file, replace "$key" text with value from map and unify text sizes if required'''

        file = open(filename, 'r')
        self.from_str(file.read(), map, unit, unify)
        file.close()

    def from_str(self, text, map, unit = 0, unify = True):
        '''Read symbol from string, replace "$key" text with value from map and unify text sizes if required'''

        # Strings are templates, so we increment
        self.templates += 1

        class position(Enum):
            unknown = 0
            definition = 1
            drawing = 2

        # Remove comment lines
        text = re.sub(r'^#.*$\s*', '', text, flags = re.MULTILINE)

        # Replace $KEYWORD with mapped value
        for key, value in map.items():
            if not isinstance(value, str):
                map[key] = str(value)
        text = re.sub(r"$(\w+)", lambda match: map[match.group(1).lower()] if match.group(1).lower() in map else match.group(1), text)

        # Parse library file
        parser = position.unknown
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
                    raise ValueError('Currently only EESchema Library with major version 2 supported!')
                if version[1] > 4:
                    print('WARNING: We only know EESchema Library until version 2.4. Upper versions are experimental!')

            elif key == 'DEF':
                part = line.split()
                if len(part) != 10:
                    raise ValueError('DEF line has too less parts')

                # Only use symbol properties and fields, if unit is global (0) or first unit
                if unit == 0 or unit == 1:
                #   self.name = part[1]
                #   self.reference = part[2]
                    self.offset = int(part[4])
                    self.pinnumber = pykicadlib.symbol.type.visible.from_str(part[5])
                    self.pinname = pykicadlib.symbol.type.visible.from_str(part[6])
                #   self.units = pykicadlib.symbol.type.units.from_str(part[8])
                #   self.flag = pykicadlib.symbol.type.flag.from_str(part[9])
                    parser = position.definition
            elif key == 'ALIAS':
                pass
            elif key == 'DRAW':
                parser = position.drawing
            elif key == 'ENDDRAW':
                parser = position.unknown
            elif key == 'ENDDEF':
                parser = position.unknown
            elif parser == position.drawing:
                # Elements, fields are ignored!
                element = pykicadlib.symbol.element.from_str(line, unify)
                element.unit = unit
                self.elements.append(element)

    def from_csv(self, filename, map, unit = 0): #, section = '', centered = True):
        # Increment table counter
        self.tables += 1

        def create_pins(x, y, step_x, step_y, data, direction):
            result = []

            name = None
            length = 0
            last_x = 0
            last_y = 0

            if direction == pykicadlib.symbol.type.direction.left or direction == pykicadlib.symbol.type.direction.right:
                pin_offset_x = -pykicadlib.config.symbol.PIN_LENGTH
                pin_offset_y = 0
                line_offset_x = int(pykicadlib.config.symbol.PIN_OFFSET * 0.75)
                line_offset_y = 0
            elif direction == pykicadlib.symbol.type.direction.up or direction == pykicadlib.symbol.type.direction.down:
                pin_offset_x = 0
                pin_offset_y = pykicadlib.config.symbol.PIN_LENGTH
                line_offset_x = 0
                line_offset_y = -int(pykicadlib.config.symbol.PIN_OFFSET * 0.75)

            if direction == pykicadlib.symbol.type.direction.right or direction == pykicadlib.symbol.type.direction.down:
                pin_offset_x = -pin_offset_x
                pin_offset_y = -pin_offset_y
                line_offset_x = -line_offset_x
                line_offset_y = -line_offset_y

            for item in data:
                # Check for same pin names
                if len(item['name']) and item['name'] != '~' and name == item['name']:
                    length += 1
                else:
                    # Draw line if equal pins follow each other
                    if length:
                        start_x = int(last_x + step_x * (length + 0.25))
                        start_y = int(last_y + step_y * (length + 0.25))
                        end_x = int(last_x - step_x * 0.25)
                        end_y = int(last_y - step_y * 0.25)

                        line = pykicadlib.symbol.element.polygon(
                            pykicadlib.config.symbol.DECORATION_THICKNESS,
                            pykicadlib.symbol.type.fill.none,
                            unit
                        )
                        line.add(pykicadlib.symbol.element.point(start_x + line_offset_x, start_y + line_offset_y))
                        line.add(pykicadlib.symbol.element.point(end_x + line_offset_x, end_y + line_offset_y))
                        result.append(line)

                    name = item['name']
                    length = 0
                    last_x = x
                    last_y = y

                if len(item['name']):
                    electric = pykicadlib.symbol.type.electric.from_name(item['electric'])
                    shape = pykicadlib.symbol.type.shape.from_name(item['shape'])

                    result.append(
                        pykicadlib.symbol.element.pin(
                            x + pin_offset_x,
                            y + pin_offset_y,
                            item['name'] if length == 0 else '~',
                            item['number'],
                            pykicadlib.config.symbol.PIN_LENGTH,
                            direction,
                            pykicadlib.config.symbol.PIN_NAME_SIZE,
                            pykicadlib.config.symbol.PIN_NUMBER_SIZE,
                            electric,
                            shape,
                            True,
                            unit
                        )
                    )

                x += step_x
                y += step_y

            # Draw line if equal pins follow each other
            if length:
                start_x = int(last_x + step_x * (length + 0.25))
                start_y = int(last_y + step_y * (length + 0.25))
                end_x = int(last_x - step_x * 0.25)
                end_y = int(last_y - step_y * 0.25)

                line = pykicadlib.symbol.element.polygon(
                    pykicadlib.config.symbol.DECORATION_THICKNESS,
                    pykicadlib.symbol.type.fill.none,
                    unit
                )
                line.add(pykicadlib.symbol.element.point(start_x + line_offset_x, start_y + line_offset_y))
                line.add(pykicadlib.symbol.element.point(end_x + line_offset_x, end_y + line_offset_y))
                result.append(line)
            return result

        # Load pins and pinname size and order them by direction
        pins = {}
        size = {}
        for direction in pykicadlib.symbol.type.direction:
            pins[direction] = []
            size[direction] = 0

        with open(filename, 'r') as csvfile:
            table = csv.reader(csvfile, delimiter = ',', quotechar = '\"')

            first_row = True
            for row in table:
                if first_row == True:
                    header = row
                    first_row = False
                else:
                    data = dict(zip(header, row))

                    # Order pins by direction
                    direction = pykicadlib.symbol.type.direction.from_name(data['direction'])
                    pins[direction].append(data)
                    if len(data['name']) and data['name'] != '~':
                        size[direction] = max(size[direction], pykicadlib.config.symbol.PIN_OFFSET + len(data['name'].replace('~', '')) * pykicadlib.config.symbol.PIN_NAME_SIZE)

        # Set default size
        for direction in pykicadlib.symbol.type.direction:
            if len(pins[direction]):
                if direction == pykicadlib.symbol.type.direction.left or pykicadlib.symbol.type.direction.right:
                    size[direction] = max(size[direction], pykicadlib.config.symbol.PIN_GRID * 2)
                else:
                    size[direction] = max(size[direction], int(pykicadlib.config.symbol.PIN_GRID * 1.5))

        # Adjust left and right pin count to satisfy zip function
        if len(pins[pykicadlib.symbol.type.direction.left]) > len(pins[pykicadlib.symbol.type.direction.right]):
            pins[pykicadlib.symbol.type.direction.right].extend([{'name': ''}] * (len(pins[pykicadlib.symbol.type.direction.left]) - len(pins[pykicadlib.symbol.type.direction.right])))
        elif len(pins[pykicadlib.symbol.type.direction.right]) > len(pins[pykicadlib.symbol.type.direction.left]):
            pins[pykicadlib.symbol.type.direction.left].extend([{'name': ''}] * (len(pins[pykicadlib.symbol.type.direction.right]) - len(pins[pykicadlib.symbol.type.direction.left])))

        # Two grid spaces above first pin and below last pin
        height = (max(len(pins[pykicadlib.symbol.type.direction.left]), len(pins[pykicadlib.symbol.type.direction.right])) + 1) * pykicadlib.config.symbol.PIN_GRID
        height = max(height, pykicadlib.config.symbol.PIN_GRID * 3)
        if len(pins[pykicadlib.symbol.type.direction.up]) and len(pins[pykicadlib.symbol.type.direction.down]):
            height = max(height, pykicadlib.config.symbol.PIN_GRID * 4)

        width = size[pykicadlib.symbol.type.direction.left] + size[pykicadlib.symbol.type.direction.right]
        if len(map['section']):
            width = max(width, pykicadlib.config.symbol.PIN_GRID + len(map['section']) * pykicadlib.config.symbol.FIELD_TEXT_SIZE)
        if width == 0:
            width = (max(len(pins[pykicadlib.symbol.type.direction.up]), len(pins[pykicadlib.symbol.type.direction.down])) + 1) * pykicadlib.config.symbol.PIN_GRID

        # Round up to next grid
        width = (((width + (pykicadlib.config.symbol.PIN_GRID - 1)) // (pykicadlib.config.symbol.PIN_GRID)) * pykicadlib.config.symbol.PIN_GRID)

        center_x = 0
        center_y = 0
        width_half = width // 2
        height_half = height // 2

        self.elements.append(
            pykicadlib.symbol.element.rectangle(
                center_x - width_half,
                center_y - height_half,
                center_x + width_half,
                center_y + height_half,
                pykicadlib.config.symbol.ELEMENT_THICKNESS,
                pykicadlib.symbol.type.fill.background,
                unit
            )
        )

        if len(pins[pykicadlib.symbol.type.direction.up]) > 1:
            up_x = (len(pins[pykicadlib.symbol.type.direction.up]) - 1) * pykicadlib.config.symbol.PIN_GRID // 2
        else:
            up_x = 0

        if len(pins[pykicadlib.symbol.type.direction.down]) > 1:
            down_x = (len(pins[pykicadlib.symbol.type.direction.down]) - 1) * pykicadlib.config.symbol.PIN_GRID // 2
        else:
            down_x = 0

        self.elements.extend(create_pins(center_x - width_half, center_y + height_half - pykicadlib.config.symbol.PIN_GRID, 0, -pykicadlib.config.symbol.PIN_GRID, pins[pykicadlib.symbol.type.direction.left], pykicadlib.symbol.type.direction.left))
        self.elements.extend(create_pins(center_x + width_half, center_y + height_half - pykicadlib.config.symbol.PIN_GRID, 0, -pykicadlib.config.symbol.PIN_GRID, pins[pykicadlib.symbol.type.direction.right], pykicadlib.symbol.type.direction.right))
        self.elements.extend(create_pins(center_x - up_x, center_y + height_half, pykicadlib.config.symbol.PIN_GRID, 0, pins[pykicadlib.symbol.type.direction.up], pykicadlib.symbol.type.direction.up))
        self.elements.extend(create_pins(center_x - down_x, center_y - height_half, pykicadlib.config.symbol.PIN_GRID, 0, pins[pykicadlib.symbol.type.direction.down], pykicadlib.symbol.type.direction.down))

        # Add decoration
        for direction in pykicadlib.symbol.type.direction.left, pykicadlib.symbol.type.direction.right:
            y = center_y + height_half - pykicadlib.config.symbol.PIN_GRID
            for item in pins[direction]:
                if 'decoration' in item and len(item['decoration']):
                    if item['decoration'] in pykicadlib.symbol.decorator.registry.keys():
                        sign = -1 if direction == pykicadlib.symbol.type.direction.left else 1
                        decorator = pykicadlib.symbol.decorator.registry[item['decoration']](center_x + sign * width_half, y, direction, unit)
                        self.elements.extend(decorator.elements)
                        self.decorated = True
                    else:
                        print("Warning: Unknown decorator '{}'".format(item['decoration']))
                y -= pykicadlib.config.symbol.PIN_GRID

        # Add line between empty pin slots on left and right side
        y = center_y + height_half - pykicadlib.config.symbol.PIN_GRID
        for left, right in zip(pins[pykicadlib.symbol.type.direction.left], pins[pykicadlib.symbol.type.direction.right]):
            if len(left['name']) == 0 and len(right['name']) == 0:
                line = pykicadlib.symbol.element.polygon(
                    pykicadlib.config.symbol.DECORATION_THICKNESS,
                    pykicadlib.symbol.type.fill.none,
                    unit
                )
                line.add(pykicadlib.symbol.element.point(center_x - width_half, y))
                line.add(pykicadlib.symbol.element.point(center_x + width_half, y))
                self.elements.append(line)
            y -= pykicadlib.config.symbol.PIN_GRID

        # Section name right top corner
        if len(map['section']):
            self.elements.append(
                pykicadlib.symbol.element.text(
                    center_x + width_half - pykicadlib.config.symbol.PIN_GRID // 2,
                    center_y + height_half - pykicadlib.config.symbol.PIN_GRID // 2,
                    map['section'],
                    pykicadlib.config.symbol.FIELD_TEXT_SIZE,
                    0.0,
                    pykicadlib.symbol.type.italic.off,
                    pykicadlib.symbol.type.bold.off,
                    pykicadlib.symbol.type.hjustify.right,
                    pykicadlib.symbol.type.vjustify.top,
                    unit
                )
            )

    def __str__(self):
        '''Render symbol into string with some automatics'''

        # Count device pins
        direction_pins = {}
        for direction in pykicadlib.symbol.type.direction:
            direction_pins[direction] = 0

        # Collect number of units and their pins used in symbol
        unit_pins = {}
        unit_count = 1
        bounds = pykicadlib.symbol.element.boundary(0, 0, 0, 0)
        pinname = pykicadlib.symbol.type.visible.no
        for element in self.elements:
            unit_count = max(unit_count, element.unit)
            bounds = pykicadlib.symbol.element.boundary.add(bounds, element.bounds)
            if isinstance(element, pykicadlib.symbol.element.pin):
                if element.name != '~':
                    pinname = pykicadlib.symbol.type.visible.yes

                if element.unit in unit_pins:
                    unit_pins[element.unit] += 1
                else:
                    unit_pins[element.unit] = 1
                direction_pins[element.direction] += 1

        # Override pinname visibility on table based symbol
        if self.tables:
            self.pinname = pinname

        # Table generated symbol have their pin names inside, if pin names exists and no decorators are used
        if self.tables and self.decorated == False and self.pinname == pykicadlib.symbol.type.visible.yes:
            self.offset = pykicadlib.config.symbol.PIN_OFFSET

        # Set pin name offset to zero, if pin names not visible
        if self.pinname == pykicadlib.symbol.type.visible.no:
            self.offset = 0

        # Pin numbers are visible, if symbol has more than one unit or was table generated
        if (self.templates and unit_count > 1) or self.tables:
            self.pinnumber = pykicadlib.symbol.type.visible.yes

        # Check, if every unit has same number of pins. Then units should be swappable!
        units = pykicadlib.symbol.type.units.locked
        if len(unit_pins) and 0 not in unit_pins and min(unit_pins.values()) == max(unit_pins.values()):
            units = pykicadlib.symbol.type.units.swappable

        # If reference matches POWER_SYMBOL_REFERENCE, than we have a power symbol
        flag = pykicadlib.symbol.type.flag.power if self.reference in pykicadlib.config.symbol.POWER_SYMBOL_REFERENCE else pykicadlib.symbol.type.flag.normal

        # Overwrite fields with symbol parameters
        for field in self.fields:
            if field.type == pykicadlib.symbol.type.field.name:
                field.value = self.name
            elif field.type == pykicadlib.symbol.type.field.reference:
                field.value = self.reference

                # Hide reference field, if reference starts with #
                if self.reference[0] == '#':
                    field.visibility = pykicadlib.symbol.type.visibility.invisible
            elif field.type == pykicadlib.symbol.type.field.footprint:
                field.value = self.footprint
            elif field.type == pykicadlib.symbol.type.field.document:
                field.value = self.document

        # Reposition visible fields
        y = bounds.y1
        for field in self.fields:
            if field.visibility == pykicadlib.symbol.type.visibility.visible:
                y -= pykicadlib.config.symbol.PIN_GRID
                field.x = 0
                field.y = y

        # Reposition invisible fields
        for field in self.fields:
            if field.visibility == pykicadlib.symbol.type.visibility.invisible:
                y -= pykicadlib.config.symbol.PIN_GRID
                field.x = 0
                field.y = y

        # Render symbol
        result = '#\n# {:s}\n#\n'.format(self.name)
        result += 'DEF {:s} {:s} 0 {:d} {:s} {:s} {:d} {:s} {:s}\n'.format(self.name, self.reference, self.offset, self.pinnumber, self.pinname, unit_count, units, flag)
        if len(self.alias):
            result += 'ALIAS {:s}\n'.format(' '.join(self.alias))

        for field in self.fields:
            if len(field.value):
                result += str(field) + '\n'

        result += 'DRAW\n'
        for element in self.elements:
            result += str(element) + '\n'
        result += 'ENDDRAW\nENDDEF\n'
        return result


class symbol(object):
    '''List of symbol'''

    def __init__(self):
        self.symbol = []

    def add(self, symbol):
        self.symbol.append(symbol)

    def __str__(self):
        result = pykicadlib.config.symbol.LIBRARY_START
        for symbol in self.symbol:
            result += str(symbol)
        result += pykicadlib.config.symbol.LIBRARY_END
        return result


class description(object):
    '''KiCAD symbol description class'''

    def __init__(self, name, description, keywords, document):
        self.name = name
        self.description = description.replace('\r', '').replace('\n', ' ')
        self.keywords = keywords.split()
        self.document = document

    def __str__(self):
        '''Render symbol description into string'''

        result = '#\n$CMP {}\n'.format(self.name)
        if len(self.description):
            result += 'D {}\n'.format(self.description)

        if len(self.keywords):
            result += 'K {}\n'.format(' '.join(self.keywords))

        if len(self.document):
            result += 'F {}\n'.format(self.document)
        result += '$ENDCMP\n'
        return result


class descriptions(object):
    '''List of symbol descriptions'''

    def __init__(self):
        self.descriptions = []

    def add(self, description):
        self.descriptions.append(description)

    def __str__(self):
        result = pykicadlib.config.symbol.DESCRIPTION_START
        for descriptions in self.descriptions:
            result += str(descriptions)
        result += pykicadlib.config.symbol.DESCRIPTION_END
        return result
