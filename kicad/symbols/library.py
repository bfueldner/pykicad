import re
import csv
from enum import Enum
from math import floor, ceil

import kicad.config
import kicad.symbols.element
import kicad.symbols.decorator

class symbol(object):
    '''KiCAD symbol class'''

    def __init__(self, name, reference, footprint, document, alias = ''): #, offset = 0, fields = [], elements = []):
        self.name = name
        self.reference = reference
        self.footprint = footprint
        self.document = document
        self.alias = alias.split()
        self.offset = 0
        self.pinnumber = kicad.symbols.type.visible.no
        self.pinname = kicad.symbols.type.visible.no
        self.fields = []
        self.elements = []

        self.templates = 0
        self.tables = 0

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
            for field in kicad.symbols.type.field:
                if field.name in map:
                    self.fields.append(
                        kicad.symbols.element.field(
                            field,
                            map[field.name],
                            0,
                            0,
                            kicad.config.symbols.FIELD_TEXT_SIZE,
                            kicad.symbols.type.orientation.horizontal,
                            kicad.symbols.type.visibility.invisible if field == kicad.symbols.type.field.footprint or field == kicad.symbols.type.field.document else kicad.symbols.type.visibility.visible,
                            kicad.symbols.type.hjustify.center,
                            kicad.symbols.type.vjustify.center,
                            kicad.symbols.type.style.none
                        )
                    )

    def from_file(self, filename, map, unit = 0, unify = True):
        '''Read symbol from file, replace "$key" text with value from map and unify text sizes if required'''

        file = open(filename, "r")
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
        text = re.sub('^#.*$\s*', '', text, flags = re.MULTILINE)

        # Replace $KEYWORD with mapped value
        for key, value in map.items():
            if not isinstance(value, str):
                map[key] = str(value)
        text = re.sub("\$(\w+)", lambda match: map[match.group(1).lower()] if match.group(1).lower() in map else match.group(0), text)

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
                    self.pinnumber = kicad.symbols.type.visible.from_str(part[5])
                    self.pinname = kicad.symbols.type.visible.from_str(part[6])
                #   self.units = kicad.symbols.type.units.from_str(part[8])
                #   self.flag = kicad.symbols.type.flag.from_str(part[9])
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
                element = kicad.symbols.element.from_str(line, unify)
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

            if direction == kicad.symbols.type.direction.left or direction == kicad.symbols.type.direction.right:
                pin_offset_x = -kicad.config.symbols.PIN_LENGTH
                pin_offset_y = 0
                line_offset_x = int(kicad.config.symbols.PIN_OFFSET * 0.75)
                line_offset_y = 0
            elif direction == kicad.symbols.type.direction.up or direction == kicad.symbols.type.direction.down:
                pin_offset_x = 0
                pin_offset_y = kicad.config.symbols.PIN_LENGTH
                line_offset_x = 0
                line_offset_y = -int(kicad.config.symbols.PIN_OFFSET * 0.75)

            if direction == kicad.symbols.type.direction.right or direction == kicad.symbols.type.direction.down:
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

                        line = kicad.symbols.element.polygon(
                            kicad.config.symbols.DECORATION_THICKNESS,
                            kicad.symbols.type.fill.none,
                            unit
                        )
                        line.add(kicad.symbols.element.point(start_x + line_offset_x, start_y + line_offset_y))
                        line.add(kicad.symbols.element.point(end_x + line_offset_x, end_y + line_offset_y))
                        result.append(line)

                    name = item['name']
                    length = 0
                    last_x = x
                    last_y = y

                if len(item['name']):
                    electric = kicad.symbols.type.electric.from_name(item['electric'])
                    shape = kicad.symbols.type.shape.from_name(item['shape'])

                    result.append(
                        kicad.symbols.element.pin(
                            x + pin_offset_x,
                            y + pin_offset_y,
                            item['name'] if length == 0 else '~',
                            item['number'],
                            kicad.config.symbols.PIN_LENGTH,
                            direction,
                            kicad.config.symbols.PIN_NAME_SIZE,
                            kicad.config.symbols.PIN_NUMBER_SIZE,
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

                line = kicad.symbols.element.polygon(
                    kicad.config.symbols.DECORATION_THICKNESS,
                    kicad.symbols.type.fill.none,
                    unit
                )
                line.add(kicad.symbols.element.point(start_x + line_offset_x, start_y + line_offset_y))
                line.add(kicad.symbols.element.point(end_x + line_offset_x, end_y + line_offset_y))
                result.append(line)
            return result

        # Load pins and order by direction
        pins = {}
        decoration = {}
        for direction in kicad.symbols.type.direction:
            pins[direction] = []
            decoration[direction] = 0

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
                    direction = kicad.symbols.type.direction.from_name(data['direction'])
                    pins[direction].append(data)
                    if 'decoration' in data and len(data['decoration']):
                        decoration[direction] += 1

        # Adjust left and right pin count to satisfy zip
        if len(pins[kicad.symbols.type.direction.left]) > len(pins[kicad.symbols.type.direction.right]):
            pins[kicad.symbols.type.direction.right].extend([{'name': ''}] * (len(pins[kicad.symbols.type.direction.left]) - len(pins[kicad.symbols.type.direction.right])))
        elif len(pins[kicad.symbols.type.direction.right]) > len(pins[kicad.symbols.type.direction.left]):
            pins[kicad.symbols.type.direction.left].extend([{'name': ''}] * (len(pins[kicad.symbols.type.direction.right]) - len(pins[kicad.symbols.type.direction.left])))

        # Two grid spaces above first pin and below last pin
        height = (max(len(pins[kicad.symbols.type.direction.left]), len(pins[kicad.symbols.type.direction.right])) + 1) * kicad.config.symbols.PIN_GRID
        height = max(height, kicad.config.symbols.PIN_GRID * 3)

        # Fixed width if decorators used
        width_left = kicad.config.symbols.PIN_GRID * 2 if decoration[kicad.symbols.type.direction.left] else 0
        width_right = kicad.config.symbols.PIN_GRID * 2 if decoration[kicad.symbols.type.direction.right] else 0

        # Otherwise take text for width
        if width_left == 0 and width_right == 0:
            for left, right in zip(pins[kicad.symbols.type.direction.left], pins[kicad.symbols.type.direction.right]):
                width_left = kicad.config.symbols.PIN_OFFSET + len(left['name']) * kicad.config.symbols.PIN_NAME_SIZE
                width_right = kicad.config.symbols.PIN_OFFSET + len(right['name']) * kicad.config.symbols.PIN_NAME_SIZE

            width_left = (((width_left + (kicad.config.symbols.PIN_GRID - 1)) // (kicad.config.symbols.PIN_GRID)) * kicad.config.symbols.PIN_GRID)
            width_right = (((width_right + (kicad.config.symbols.PIN_GRID - 1)) // (kicad.config.symbols.PIN_GRID)) * kicad.config.symbols.PIN_GRID)

            # Symetric
            width_left = max(width_left, kicad.config.symbols.PIN_GRID * 2)
            width_left = max(width_left, width_right)
            width_right = width_left

        abc = '''
        # Calculate device width from device name and pin names (not really exact!)
        width = len(self.name) * kicad.config.symbols.FIELD_TEXT_SIZE
        for left, right in zip(pins[kicad.symbols.type.direction.left], pins[kicad.symbols.type.direction.right]):
            left_width = kicad.config.symbols.PIN_OFFSET + len(left['name']) * kicad.config.symbols.PIN_NAME_SIZE
            right_width = kicad.config.symbols.PIN_OFFSET + len(right['name']) * kicad.config.symbols.PIN_NAME_SIZE
            width = max(width, 3 * kicad.config.symbols.PIN_OFFSET + left_width + right_width)

        # Round up to next grid
        width = (((width + (kicad.config.symbols.PIN_GRID - 1)) // (kicad.config.symbols.PIN_GRID)) * kicad.config.symbols.PIN_GRID)'''

        center_x = 0
        center_y = 0
    #    width_half = width // 2
        width_half = max(width_left, width_right)
        height_half = height // 2
    #   if height_half % kicad.config.symbols.PIN_GRID:
    #       center_y = height_half % kicad.config.symbols.PIN_GRID

        self.elements.append(
            kicad.symbols.element.rectangle(
                center_x - width_left,
                center_y - height_half,
                center_x + width_right,
                center_y + height_half,
                kicad.config.symbols.ELEMENT_THICKNESS,
                kicad.symbols.type.fill.background,
                unit
            )
        )

        if len(pins[kicad.symbols.type.direction.up]) > 1:
            up_x = (len(pins[kicad.symbols.type.direction.up]) - 1) * kicad.config.symbols.PIN_GRID // 2
            up_x = up_x // kicad.config.symbols.PIN_GRID * kicad.config.symbols.PIN_GRID
        else:
            up_x = 0

        if len(pins[kicad.symbols.type.direction.down]) > 1:
            down_x = (len(pins[kicad.symbols.type.direction.down]) - 1) * kicad.config.symbols.PIN_GRID // 2
            down_x = down_x // kicad.config.symbols.PIN_GRID * kicad.config.symbols.PIN_GRID
        else:
            down_x = 0

        self.elements.extend(create_pins(center_x - width_left, center_y + height_half - kicad.config.symbols.PIN_GRID, 0, -kicad.config.symbols.PIN_GRID, pins[kicad.symbols.type.direction.left], kicad.symbols.type.direction.left))
        self.elements.extend(create_pins(center_x + width_right, center_y + height_half - kicad.config.symbols.PIN_GRID, 0, -kicad.config.symbols.PIN_GRID, pins[kicad.symbols.type.direction.right], kicad.symbols.type.direction.right))
        self.elements.extend(create_pins(center_x - up_x, center_y + height_half, kicad.config.symbols.PIN_GRID, 0, pins[kicad.symbols.type.direction.up], kicad.symbols.type.direction.up))
        self.elements.extend(create_pins(center_x - down_x, center_y - height_half, kicad.config.symbols.PIN_GRID, 0, pins[kicad.symbols.type.direction.down], kicad.symbols.type.direction.down))

        # Add decoration
        for direction in kicad.symbols.type.direction.left, kicad.symbols.type.direction.right:
            y = center_y + height_half - kicad.config.symbols.PIN_GRID
            for item in pins[direction]:
                if 'decoration' in item and len(item['decoration']):
                    if item['decoration'] in kicad.symbols.decorator.registry.keys():
                        sign = -1 if direction == kicad.symbols.type.direction.left else 1
                        decorator = kicad.symbols.decorator.registry[item['decoration']](center_x + sign * width_half, y, direction, unit)
                        self.elements.extend(decorator.elements)
                    else:
                        print("Warning: Unknown decorator '{}'".format(item['decoration']))
                y -= kicad.config.symbols.PIN_GRID

        # Add line between empty pin slots on left and right side
        y = center_y + height_half - kicad.config.symbols.PIN_GRID
        for left, right in zip(pins[kicad.symbols.type.direction.left], pins[kicad.symbols.type.direction.right]):
            if len(left['name']) == 0 and len(right['name']) == 0:
                line = kicad.symbols.element.polygon(
                    kicad.config.symbols.DECORATION_THICKNESS,
                    kicad.symbols.type.fill.none,
                    unit
                )
                line.add(kicad.symbols.element.point(center_x - width_left, y))
                line.add(kicad.symbols.element.point(center_x + width_right, y))
                self.elements.append(line)
            y -= kicad.config.symbols.PIN_GRID

        # Section name right top corner
        if len(map['section']):
            self.elements.append(
                kicad.symbols.element.text(
                    center_x + width_right - kicad.config.symbols.PIN_GRID // 2,
                    center_y + height_half - kicad.config.symbols.PIN_GRID // 2,
                    map['section'],
                    kicad.config.symbols.FIELD_TEXT_SIZE,
                    0.0,
                    kicad.symbols.type.italic.off,
                    kicad.symbols.type.bold.off,
                    kicad.symbols.type.hjustify.right,
                    kicad.symbols.type.vjustify.top,
                    unit
                )
            )

    def __str__(self):
        '''Render symbol into string with some automatics'''

        # Count device pins
        direction_pins = {}
        for direction in kicad.symbols.type.direction:
            direction_pins[direction] = 0

        # Collect number of units and their pins used in symbol
        unit_pins = {}
        unit_count = 1
        bounds = kicad.symbols.element.boundary(0, 0, 0, 0)
        pinname = kicad.symbols.type.visible.no
        for element in self.elements:
            unit_count = max(unit_count, element.unit)
            bounds = kicad.symbols.element.boundary.add(bounds, element.bounds)
            if isinstance(element, kicad.symbols.element.pin):
                if element.number != '~':
                    pinname = kicad.symbols.type.visible.yes

                if element.unit in unit_pins:
                    unit_pins[element.unit] += 1
                else:
                    unit_pins[element.unit] = 1
                direction_pins[element.direction] += 1

        # Override pinname visibility on table based symbols
        if self.tables:
            self.pinname = pinname

        # Table generated symbols have their pin names inside
        if self.tables:
            self.offset = kicad.config.symbols.PIN_OFFSET

        # Set pin name offset to zero, if pin names not visible
        if self.pinname == kicad.symbols.type.visible.no:
            self.offset = 0

        # Pin numbers are visible, if symbol has more than one unit or was table generated
        if (self.templates and unit_count > 1) or self.tables:
            self.pinnumber = kicad.symbols.type.visible.yes

        # Check, if every unit has same number of pins. Then units should be swappable!
        units = kicad.symbols.type.units.locked
        if len(unit_pins) and 0 not in unit_pins and min(unit_pins.values()) == max(unit_pins.values()):
            units = kicad.symbols.type.units.swappable

        # If reference matches POWER_SYMBOL_REFERENCE, than we have a power symbol
        flag = kicad.symbols.type.flag.power if self.reference in kicad.config.symbols.POWER_SYMBOL_REFERENCE else kicad.symbols.type.flag.normal

        result = '#\n# {:s}\n#\n'.format(self.name)
        result += 'DEF {:s} {:s} 0 {:d} {:s} {:s} {:d} {:s} {:s}\n'.format(self.name, self.reference, self.offset, self.pinnumber, self.pinname, unit_count, units, flag)
        if len(self.alias):
            result += 'ALIAS {:s}\n'.format(' '.join(self.alias))

        y = bounds.y1
        for field in self.fields:
            # Always overwrite field 'name' and 'reference' with own parameters
            if field.type == kicad.symbols.type.field.name:
                field.value = self.name
            elif field.type == kicad.symbols.type.field.reference:
                field.value = self.reference
                if self.reference[0] == '#':
                    field.visibility = kicad.symbols.type.visibility.invisible
            elif field.type == kicad.symbols.type.field.footprint:
                field.value = self.footprint
            elif field.type == kicad.symbols.type.field.document:
                field.value = self.document

            # Reposition visible fields
            if field.visibility == kicad.symbols.type.visibility.visible:
                y -= kicad.config.symbols.PIN_GRID
            field.x = 0
            field.y = y

            if len(field.value):
                result += str(field) + '\n'
        result += 'DRAW\n'
        for element in self.elements:
            result += str(element) + '\n'
        result += 'ENDDRAW\nENDDEF\n'
        return result

class symbols(object):
    '''List of symbols'''

    def __init__(self):
        self.symbols = []

    def add(self, symbol):
        self.symbols.append(symbol)

    def __str__(self):
        result = kicad.config.symbols.LIBRARY_START
        for symbol in self.symbols:
            result += str(symbol)
        result += kicad.config.symbols.LIBRARY_END
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
        result = kicad.config.symbols.DESCRIPTION_START
        for descriptions in self.descriptions:
            result += str(descriptions)
        result += kicad.config.symbols.DESCRIPTION_END
        return result
