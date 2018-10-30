import re
import itertools
from enum import Enum

import kicad.config
import kicad.symbols.element

class base(object):

    def __init__(self, name, reference, offset = 0, pinnumber = kicad.symbols.type.visible.yes, pinname = kicad.symbols.type.visible.yes, units = kicad.symbols.type.units.swappable, flag = kicad.symbols.type.flag.normal, fields = [], elements = []):
        self.name = name
        self.reference = reference
        self.offset = offset
        self.pinnumber = pinnumber
        self.pinname = pinname
        self.units = units
        self.flag = flag
        self.fields = fields
        self.elements = elements

        self.unit_count = 0

    def add(self, item):
        pass

    def sort(self):
        '''Sort elements according to their priority'''

        self.elements.sort(key = lambda element: element.priority)

    def optimize(self):
        '''Remove empty fields and detect duplicate graphical elements from symbol and merge them to unit = 0'''

        x = '''
        list = []
        for key, field in self.fields.iteritems():
            if not len(field.value):
                list.append(key)
        self.fields = { key: self.fields[key] for key in self.fields if key not in list }'''

        start = 0
        # Loop over all elements in a double loop
        while start < len(self.elements) - 1:
            base = self.elements[start]
            start += 1

            # Already processed? Continue!
            if base.unit < 0:
                continue

            list = []
            count = 0
            for element in itertools.islice(self.elements, start, None):
                # Already processed? Continue!
                if element.unit < 0:
                    continue

                if base == element:
                    # Same element already symbol wide defined
                    if base.unit == 0:
                        element.unit = -1
                    elif element.unit == 0:
                        base.unit = -1
                    # Same element, but none of it is in unit == 0
                    else:
                        base.unit = 0
                        element.unit = -1
                    #    list.append(module)
                    #    count += 1

            if self.units > 1 and count == self.units - 1:
                base.unit = 0
                for module in list:
                    module.unit = -1

        self.modules = [item for item in self.elements if item.unit != -1]


    def __str__(self):
        result = '#\n# {:s}\n#\n'.format(self.name)
        result += 'DEF {:s} {:s} 0 {:d} {:s} {:s} {:d} {:s} {:s}\n'.format(self.name, self.reference, self.offset, self.pinnumber, self.pinname, self.unit_count, self.units, self.flag)
        for field in self.fields:
            if len(field.value):
                result += str(field) + '\n'
        result += 'DRAW\n'
        for element in self.elements:
            result += str(element) + '\n'
        result += 'ENDDRAW\nENDDEF\n'
        return result

#    @staticmethod
    def from_file(self, filename, map, unit = 0, unify = True):
        file = open(filename, "r")
        from_str(file.read(), map, unit, unify)
        file.close()

    def from_str(self, text, map, unit = 0, unify = True):
        class position(Enum):
            unknown = 0
            definition = 1
            drawing = 2

        # Remove comment lines
        text = re.sub('^#.*$\s*', '', text, flags = re.MULTILINE)

        # Replace $KEYWORD with mapped value
        text = re.sub("\$(\w+)", lambda match: map[match.group(1).lower()] if match.group(1).lower() in map else match.group(0), text)

        replace_map = '''
        for key, value in map.items():
            if type(value) is str:
                rep_map[key.upper()] = value.replace(' ', '~')
            else:
                rep_map[key.upper()] = value
'''

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

                self.name = part[1]
                self.reference = part[2]
                self.offset = int(part[4])
                self.pinnumber = kicad.symbols.type.visible.from_str(part[5])
                self.pinname = kicad.symbols.type.visible.from_str(part[6])
            #   self.unit_count
                self.units = kicad.symbols.type.units.from_str(part[8])
                self.flag = kicad.symbols.type.flag.from_str(part[9])

                parser = position.definition
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
                #    self.unit_count = max(self.unit_count, element.unit)
                    self.elements.append(element)
                else:
                    print(key)

        x = '''
        inDef = False
        inDraw = False
        for row in csv.reader(text, delimiter = " ", skipinitialspace = True):
            if row[0] == 'EESchema-LIBRARY':
                if row[2] != '2.3':
                    print "Symbol version %s is not supported yet!"%(row[2])
                    sys.exit(2)
            elif row[0] == 'DEF':
                inDef = True
            elif row[0] == 'DRAW':
                inDraw = True
                continue
            elif row[0] == 'ENDDEF':
                inDef = False
            elif row[0] == 'ENDDRAW':
                inDraw = False

            for i in range(len(row)):
               try:
                   row[i] = int(row[i])
               except:
                   pass

            if inDef and not inDraw:
                if header:
                    if row[0] == 'DEF':
                        row.pop(0)
                        self.offset = row[3]
                        # Take pin number visibility from symbol. Names are checked automatically.
                        self.pinnumber = row[4]
                        self.count = 0 # = highest unit if != 0
                        self.locked = False # False, if no component part in unit = 0
                        self.flag = row[8]
                    else:
                        m = re.match(r"F(\d+)", row[0])
                        if m:
                            row.pop(0)
                            data = dict(zip(['value', 'x', 'y', 'size', 'orientation', 'visibility', 'hjustify', 'vjustify'], row))
                            data['style'] = data['vjustify'][1:]
                            data['vjustify'] = data['vjustify'][0]
                            data['id'] = int(m.group(1))

                            self.fields[int(m.group(1))] = Field(**data)

            elif inDef and inDraw:
                symbol_type = row[0]
                row.pop(0)
                # Polygon
                if symbol_type == 'P':
                    data = dict(zip(['unit', 'representation', 'width', 'fill'], row[1:4]+row[-1:]))
                    if unit != -1:
                        data['unit'] = unit
                    data['representation'] = representation

                    points = row[4:-1]

                    poly = Polygon(**data)
                    for i in range(0, len(points), 2):
                        poly.add(Point(points[i], points[i + 1]))
                    self.addModule(poly)

                # Rectangle
                elif symbol_type == 'S':
                    data = dict(zip(['x1', 'y1', 'x2', 'y2', 'unit', 'representation', 'width', 'fill'], row))
                    if unit != -1:
                        data['unit'] = unit
                    data['representation'] = representation

                    self.addModule(Rectangle(**data))

                # Circle
                elif symbol_type == 'C':
                    data = dict(zip(['x', 'y', 'radius', 'unit', 'representation', 'width', 'fill'], row))
                    if unit != -1:
                        data['unit'] = unit
                    data['representation'] = representation

                    self.addModule(Circle(**data))

                # Arc
                elif symbol_type == 'A':
                    data = dict(zip(['x', 'y', 'radius', 'startAngle', 'endAngle', 'unit', 'representation', 'width', 'fill', 'startX', 'startY', 'endX', 'endY'], row))
                    if unit != -1:
                        data['unit'] = unit
                    data['representation'] = representation

                    self.addModule(Arc(**data))

                # Text
                elif symbol_type == 'T':
                    row.pop(4) # Pop unused argument
                    data = dict(zip(['orientation', 'x', 'y', 'size', 'unit', 'representation', 'text', 'italic', 'bold', 'hjustify', 'vjustify'], row))
                    if unit != -1:
                        data['unit'] = unit
                    data['representation'] = representation

                    self.addModule(Text(**data))

                # Pin
                elif symbol_type == 'X':
                    data = dict(zip(['name', 'number', 'x', 'y', 'length', 'orientation', 'numberSize', 'nameSize', 'unit', 'representation', 'type', 'shape'], row))
                    if unit != -1:
                        data['unit'] = unit
                    data['representation'] = representation

                    self.addModule(Pin_(**data))

        # If more than one unit is loaded, we make pin numbers visible!
        if unit:
            self.pinnumber = 'Y'
'''
