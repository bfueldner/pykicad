import re
import csv
from enum import Enum

import kicad.config
import kicad.symbols.element

class symbol(object):
    '''KiCAD symbol class'''

    def __init__(self, name, reference, footprint, document, alias = ''): #, offset = 0, fields = [], elements = []):
        self.name = name
        self.reference = reference
        self.footprint = footprint
        self.document = document
        self.alias = alias.split()
        self.offset = 0
        self.pinname = kicad.symbols.type.visible.yes
        self.fields = []
        self.elements = []

    def optimize(self):
        '''Merge duplicate graphical elements into unit = 0'''

        if len(self.elements) < 2:
            return

        # Walk over every element and delete duplicates from behind
        compare = len(self.elements) - 1
        while compare:
            base = compare - 1
            while base >= 0:
                if self.elements[base] == self.elements[compare]:
                    self.elements[base].unit = 0
                    del self.elements[compare]
                    break
                base -= 1
            compare -= 1

    def sort(self):
        '''Sort fields and elements according to their priority'''

        self.fields.sort(key = lambda field: field.type.value)
        self.elements.sort(key = lambda element: element.priority)

    def from_file(self, filename, map, unit = 0, unify = True):
        '''Read symbol from file, replace "$key" text with value from map and unify text sizes if required'''

        file = open(filename, "r")
        self.from_str(file.read(), map, unit, unify)
        file.close()

    def from_str(self, text, map, unit = 0, unify = True):
        '''Read symbol from string, replace "$key" text with value from map and unify text sizes if required'''

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
                #   self.pinnumber = kicad.symbols.type.visible.from_str(part[5])
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
            else:
                # Fields
                if parser == position.definition:
                    field = kicad.symbols.element.from_str(line, unify)
                    if field.type.name in map:
                        field.value = map[field.type.name]
                    self.fields.append(field)
                # Elements
                elif parser == position.drawing:
                    element = kicad.symbols.element.from_str(line, unify)
                    element.unit = unit
                    self.elements.append(element)

    def from_csv(self, filename, unit = 0): #, section = '', centered = True):
    #    # In table based symbols pin numbers are always visible!
    #    self.pinnumber = 'Y'

        class space(object):
            '''Space dummy class'''

            def __init__(self):
                pass

        pins = {}
        for direction in kicad.symbols.type.direction:
            pins[direction] = []

        with open(filename, 'r') as csvfile:
            table = csv.reader(csvfile, delimiter = ',', quotechar = '\"')

            first_row = True
            for row in table:
                if first_row == True:
                    header = row
                    first_row = False
                else:
                    data = dict(zip(header, row))
                    x = '''
                    for i in range(len(row)):
                        try:
                            row[i] = int(row[i])
                        except:
                            pass'''

                    print(data)

                    direction = kicad.symbols.type.direction.from_name(data['direction'])
                    if data['electric'] != 'space':
                        electric = kicad.symbols.type.electric.from_name(data['electric'])
                        shape = kicad.symbols.type.shape.from_name(data['shape'])

                        pins[direction].append(
                            kicad.symbols.element.pin(
                                0,
                                0,
                                data['name'],
                                data['number'],
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
                    else:
                        pins[direction].append(space())
                        print('space')

        for direction in kicad.symbols.type.direction:
            print(direction.name, len(pins[direction]))

        self.offset = kicad.config.symbols.PIN_OFFSET

        width = max(len(pins[kicad.symbols.type.direction.up]), len(pins[kicad.symbols.type.direction.down]))
        height = max(len(pins[kicad.symbols.type.direction.left]), len(pins[kicad.symbols.type.direction.right]))
        print(width, height)

        # Two grid spaces above first pin and below last pin
        width = (width + 1) * kicad.config.symbols.PIN_GRID
        height = (height + 1) * kicad.config.symbols.PIN_GRID
        print(width, height)

        # Detect space for device name and pin names (not really exact!)
        device_width = len(self.name) * kicad.config.symbols.FIELD_TEXT_SIZE
        for left, right in zip(pins[kicad.symbols.type.direction.left], pins[kicad.symbols.type.direction.right]):
            left_width = len(left.name) if isinstance(left, kicad.symbols.element.pin) else 0
            right_width = len(right.name) if isinstance(right, kicad.symbols.element.pin) else 0
            left_width *= kicad.config.symbols.PIN_NAME_SIZE
            right_width *= kicad.config.symbols.PIN_NAME_SIZE
            device_width = max(device_width, 3 * kicad.config.symbols.PIN_OFFSET + left_width + right_width)
        device_width = (((device_width + (kicad.config.symbols.PIN_GRID - 1)) // (kicad.config.symbols.PIN_GRID)) * kicad.config.symbols.PIN_GRID)

        self.elements.append(
            kicad.symbols.element.rectangle(
                -device_width // 2,
                -height // 2,
                device_width // 2,
                height // 2,
                kicad.config.symbols.ELEMENT_THICKNESS,
                kicad.symbols.type.fill.background,
                unit
            )
        )

        x = device_width // 2
        y = height // 2
        y -= 1 * kicad.config.symbols.PIN_GRID
        for left, right in zip(pins[kicad.symbols.type.direction.left], pins[kicad.symbols.type.direction.right]):
            space = True
            if isinstance(left, kicad.symbols.element.pin):
                left.x = -x - kicad.config.symbols.PIN_LENGTH
                left.y = y
                print(left.name, left.x, left.y)
                self.elements.append(left)
                space = False

            # TODO: Pin name line for dupplicate names

            if isinstance(right, kicad.symbols.element.pin):
                right.x = x + kicad.config.symbols.PIN_LENGTH
                right.y = y
                print(right.name, right.x, right.y)
                self.elements.append(right)
                space = False

            # TODO: Pin name line for dupplicate names

            # TODO: Pin decoration

            if space:
                line = kicad.symbols.element.polygon(
                    kicad.config.symbols.SPACE_THICKNESS,
                    kicad.symbols.type.fill.none,
                    unit
                )
                line.add(kicad.symbols.element.point(-x, y))
                line.add(kicad.symbols.element.point(x, y))
                self.elements.append(line)
            y -= kicad.config.symbols.PIN_GRID

        # TODO: Section name right top corner
        # TODO: Reference Top left
        # TODO: Name Bottom left

    def __str__(self):
        '''Render symbol into string with some automatics'''

        # Collect number of units and their pins used in symbol
        unit_pins = {}
        unit_count = 1
    #   pinname = kicad.symbols.type.visible.no
        for element in self.elements:
            unit_count = max(unit_count, element.unit)
            if isinstance(element, kicad.symbols.element.pin):
            #   if element.number != '~':
            #    pinname = kicad.symbols.type.visible.yes

                if element.unit in unit_pins:
                    unit_pins[element.unit] += 1
                else:
                    unit_pins[element.unit] = 1

        # Set pin name offset to zero, if pin names not visible
        if self.pinname == kicad.symbols.type.visible.no:
            self.offset = 0

        # Pin numbers are visible, if symbol has more than one unit
        pinnumber = kicad.symbols.type.visible.yes if unit_count > 1 else kicad.symbols.type.visible.no

        # Check, if every unit has same number of pins. Then units should be swappable!
        units = kicad.symbols.type.units.locked
        if len(unit_pins) and 0 not in unit_pins and min(unit_pins.values()) == max(unit_pins.values()):
            units = kicad.symbols.type.units.swappable

        # If reference matches POWER_SYMBOL_REFERENCE, than we have a power symbol
        flag = kicad.symbols.type.flag.power if self.reference in kicad.config.symbols.POWER_SYMBOL_REFERENCE else kicad.symbols.type.flag.normal

        result = '#\n# {:s}\n#\n'.format(self.name)
        result += 'DEF {:s} {:s} 0 {:d} {:s} {:s} {:d} {:s} {:s}\n'.format(self.name, self.reference, self.offset, pinnumber, self.pinname, unit_count, units, flag)
        if len(self.alias):
            result += 'ALIAS {:s}\n'.format(' '.join(self.alias))

        for field in self.fields:
            # Always overwrite field 'name' and 'reference' with own parameters
            if field.type == kicad.symbols.type.field.name:
                field.value = self.name
            elif field.type == kicad.symbols.type.field.reference:
                field.value = self.reference
            elif field.type == kicad.symbols.type.field.footprint:
                field.value = self.footprint
            elif field.type == kicad.symbols.type.field.document:
                field.value = self.document

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
