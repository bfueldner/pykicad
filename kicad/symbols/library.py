import re
from enum import Enum

import kicad.config
import kicad.symbols.element

class symbol(object):
    '''KiCAD symbol class'''

    def __init__(self, name, reference, footprint, document, alias = '', offset = 0, pinname = kicad.symbols.type.visible.yes, fields = [], elements = []):
        self.name = name
        self.reference = reference
        self.footprint = footprint
        self.document = document
        self.alias = alias.split()
        self.offset = offset
        self.pinname = pinname
        self.fields = fields
        self.elements = elements

    def optimize(self):
        '''Merge duplicate graphical elements into unit = 0'''

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

    def __str__(self):
        '''Render symbol into string with some automatics'''

        # Set pin name offset to zero, if pin names not visible
        if self.pinname == kicad.symbols.type.visible.no:
            self.offset = 0

        # Detect number of units and their pins used in symbol
        unit_pins = {}
        unit_count = 1
        for element in self.elements:
            unit_count = max(unit_count, element.unit)
            if isinstance(element, kicad.symbols.element.pin):
                if element.unit in unit_pins:
                    unit_pins[element.unit] += 1
                else:
                    unit_pins[element.unit] = 1

        # Pin numbers are visible, if symbol has more than one unit
        pinnumber = kicad.symbols.type.visible.yes if unit_count > 1 else kicad.symbols.type.visible.no

        # Check, if every unit has same number of pins. Then units should be swappable!
        units = kicad.symbols.type.units.swappable if 0 not in unit_pins and min(unit_pins.values()) == max(unit_pins.values()) else kicad.symbols.type.units.locked

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

    def from_file(self, filename, map, unit = 0, unify = True):
        '''Read symbol from file, replace "$key" text with value from map and unify text sizes if required'''

        file = open(filename, "r")
        from_str(file.read(), map, unit, unify)
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
                    self.fields.append(field)
                # Elements
                elif parser == position.drawing:
                    element = kicad.symbols.element.from_str(line, unify)
                    element.unit = unit
                    self.elements.append(element)

class description(object):
    '''KiCAD symbol description class'''

    def __init__(self, name, description, keywords, document):
        self.name = name
        self.description = description.replace('\n\r', '')
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
