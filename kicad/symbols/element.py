import re
import shlex
import datetime

import kicad.symbols.type

def pinValue(value):
    '''Convert pin number into value (especially for BGA numbering scheme)'''

    res = re.match(r"[0-9A-Z]+", value)
    if res:
        sum = 0
        for c in res.group(0):
            sum = sum * 128 + ord(c)
        return sum
    else:
        raise ValueError('Value does not match!')

class alias(object):
    '''2.3.1 Aliases'''
    pass

class field(object):
    '''2.3.2 Component field'''

    fmt = 'F{:d} "{:s}" {:d} {:d} {:d} {:s} {:s} {:s} {:s}{:s} "{:s}"'

    def __init__(self, type, value, x, y, size, orientation, visibility, hjustify, vjustify, style):
        self.type = type
        self.value = value
        self.x = x
        self.y = y
        self.size = size
        self.orientation = orientation
        self.visibility = visibility
        self.hjustify = hjustify
        self.vjustify = vjustify
        self.style = style

    def __str__(self):
        return field.fmt.format(
            self.type.value,
            self.value,
            self.x,
            self.y,
            self.size,
            self.orientation,
            self.visibility,
            self.hjustify,
            self.vjustify,
            self.style,
            self.type
        )

class point(object):
    '''Point helper'''

    fmt = "{:d} {:d}"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        '''Compare only same instances'''

        if not isinstance(other, point):
            return False

        return self.x == other.x and self.y == other.y

    def __str__(self):
        return point.fmt.format(
            self.x,
            self.y,
        )

class element(object):
    '''Component element'''

    def __init__(self, unit, representation, order):
        self.unit = unit
        self.representation = representation
        self.order = order

    @property
    def priority(self):
        return self.unit * 1048576 + self.order * 65536

class polygon(element):
    '''2.3.3.1 Polygon'''

    fmt = "P {:d} {:d} {:d} {:d} {:s}{:s}"
    order = 2

    def __init__(self, thickness, fill, unit = 0, representation = kicad.symbols.type.representation.normal):
        super().__init__(unit, representation, polygon.order)

        self.thickness = thickness
        self.fill = fill
        self.points = []

    def add(self, point):
        '''Add point to polygon'''

        self.points.append(point)

    def remove(self, index):
        '''Remove element from polygon'''

        del self.points[index]
    #    self.points.remove(index)

    def __eq__(self, other):
        '''Compare only same instances'''

        if not isinstance(other, polygon):
            return False

        if len(self.points) != len(other.points):
            return False

        for point1, point2 in zip(self.points, other.points):
            if point1 != point2:
                return False
        return True

    @property
    def priority(self):
        return self.unit * 1048576 + self.order * 65536 + len(self.points)

    def __str__(self):
        points = ''
        for point in self.points:
            points += str(point) + ' '

        return polygon.fmt.format(
            len(self.points),
            self.unit,
            self.representation.value,
            self.thickness,
            points,
            self.fill
        )

class rectangle(element):
    '''2.3.3.2 Rectangle'''

    fmt = 'S {:d} {:d} {:d} {:d} {:d} {:d} {:d} {:s}'
    order = 1

    def __init__(self, x1, y1, x2, y2, thickness, fill, unit = 0, representation = kicad.symbols.type.representation.normal):
        super().__init__(unit, representation, rectangle.order)

        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.thickness = thickness
        self.fill = fill

    def __eq__(self, other):
        '''Compare only same instances'''

        if not isinstance(other, rectangle):
            return False

        return self.x1 == other.x1 and self.y1 == other.y1 and self.x2 == other.x2 and self.y2 == other.y2

    def __str__(self):
        return rectangle.fmt.format(
            self.x1,
            self.y1,
            self.x2,
            self.y2,
            self.unit,
            self.representation.value,
            self.thickness,
            self.fill
        )

class circle(element):
    '''2.3.3.3 Circle'''

    fmt = 'C {:d} {:d} {:d} {:d} {:d} {:d} {:s}'
    order = 3

    def __init__(self, x, y, radius, thickness, fill, unit = 0, representation = kicad.symbols.type.representation.normal):
        super().__init__(unit, representation, circle.order)

        self.x = x
        self.y = y
        self.radius = radius
        self.thickness = thickness
        self.fill = fill

    def __eq__(self, other):
        '''Compare only same instances'''

        if not isinstance(other, circle):
            return False

        return self.x == other.x and self.y == other.y and self.radius == other.radius

    def __str__(self):
        return circle.fmt.format(
            self.x,
            self.y,
            self.radius,
            self.unit,
            self.representation.value,
            self.thickness,
            self.fill
        )

class arc(element):
    '''2.3.3.4 Arc'''

    fmt = 'A {:d} {:d} {:d} {:.0f} {:.0f} {:d} {:d} {:d} {:s} {:d} {:d} {:d} {:d}'
    order = 4

    def __init__(self, x, y, startX, startY, endX, endY, startAngle, endAngle, radius, thickness, fill, unit = 0, representation = kicad.symbols.type.representation.normal):
        super().__init__(unit, representation, arc.order)

        self.x = x
        self.y = y
        self.startX = startX
        self.startY = startY
        self.endX = endX
        self.endY = endY
        self.startAngle = startAngle
        self.endAngle = endAngle
        self.radius = radius
        self.thickness = thickness
        self.fill = fill

    def __eq__(self, other):
        '''Compare only same instances'''

        if not isinstance(other, arc):
            return False

        return self.x == other.x and self.y == other.y and self.startX == other.startX and self.startY == other.startY and self.endX == other.endX and self.endY == other.endY and self.startAngle == other.startAngle and self.endAngle == other.endAngle and self.radius == other.radius

    def __str__(self):
        return arc.fmt.format(
            self.x,
            self.y,
            self.radius,
            self.startAngle * 10,
            self.endAngle * 10,
            self.unit,
            self.representation.value,
            self.thickness,
            self.fill,
            self.startX,
            self.startY,
            self.endX,
            self.endY
        )

class text(element):
    '''2.3.3.5 Text
        New format since 2.4?

        x, y - Position
        text - Text
        size - Size in mil
        angle - Angle in centidegree (supported, but not documented!)
        unit - Unit number
        convert - Shape number
    '''

    fmt = 'T {:.0f} {:d} {:d} {:d} 0 {:d} {:d} "{:s}" {:s} {:d} {:s} {:s}'
    order = 0

    def __init__(self, x, y, value, size, angle, italic = kicad.symbols.type.italic.off, bold = kicad.symbols.type.bold.off, hjustify = kicad.symbols.type.hjustify.center, vjustify = kicad.symbols.type.vjustify.center, unit = 0, representation = kicad.symbols.type.representation.normal):
        super().__init__(unit, representation, text.order)

        self.x = x
        self.y = y
        self.value = value
        self.size = size
        self.angle = angle
        self.italic = italic
        self.bold = bold
        self.hjustify = hjustify
        self.vjustify = vjustify

    def __eq__(self, other):
        '''Compare only same instances'''

        if not isinstance(other, text):
            return False

        return self.x == other.x and self.y == other.y and self.value == other.value

    def __str__(self):
        return text.fmt.format(
            self.angle * 10,
            self.x,
            self.y,
            self.size,
            self.unit,
            self.representation.value,
            self.value.replace('"', "''"),
            self.italic,
            self.bold.value,
            self.hjustify,
            self.vjustify
        )

class pin(element):
    '''2.3.4 Pin'''

    fmt = 'X {:s} {:s} {:d} {:d} {:d} {:s} {:d} {:d} {:d} {:d} {:s} {:s}{:s}'
    order = 10

    def __init__(self, x, y, name, number, length, direction, nameSize, numberSize, electric = kicad.symbols.type.electric.input, shape = kicad.symbols.type.shape.line, visible = True, unit = 0, representation = kicad.symbols.type.representation.normal):
        super().__init__(unit, representation, pin.order)

        self.x = x
        self.y = y
        self.name = name
        self.number = number
        self.length = length
        self.direction = direction
        self.nameSize = nameSize
        self.numberSize = numberSize
        self.electric = electric
        self.shape = shape
        self.visible = visible

    def __eq__(self, other):
        '''Compare only same instances'''

        if not isinstance(other, pin):
            return False

    #   return self.x == other.x and self.y == other.y and self.length == other.length and self.name == other.name and self.number == other.number
        return False

    @property
    def priority(self):
        return self.unit * 1048576 + self.order * 65536 + pinValue(self.number)

    def __str__(self):
        return pin.fmt.format(
            self.name,
            self.number,
            self.x,
            self.y,
            self.length,
            self.direction,
            self.nameSize,
            self.numberSize,
            self.unit,
            self.representation.value,
            self.electric,
            'N' if not self.visible else '',
            self.shape
        ).rstrip()

class fields(object):
    '''Component fields'''

    def __init__(self):
        self.fields = {}



class elements(object):
    '''Component elements'''

    def __init__(self):
        pass


class component(object):
    '''symbols component'''

    def __init__(self):
        self.name = ''
        self.reference = ''
        self.text_offset = ''
        self.draw_pinnumber = True
        self.draw_pinname = True
        self.unit_count = 0
        self.units_locked = False
        self.option_flag = ''

        self.fields = fields()
        self.alias = []
        self.elements = []

    @property
    def fields(self):
        return self.fields

    def load(self, file):
        pass

    def save(self, file):
        pass

class symbols(object):
    '''symbols class'''

    version_major = 2
    version_minor = 0

    def __init__(self):
        pass

    def __str__(self):
        print("EESchema-LIBRARY Version {}.{} {}".format(self.version_major, self.version_minor, datetime.datetime.today().strftime('%d/%m/%Y-%H:%M:%S')))
        print("description of the components")
        print("# End Library")
        pass

def from_str(string, unify = True):
    '''Generate elements out of string lines. Used to load a symbol file'''

    string = string.strip()
    char = string[0]
#   part = string[1:].split()
#   part = re.findall(r'[^"\s]\S*|".+?"', string[1:])
    part = shlex.split(string[1:])

    if char == 'F':
        if len(part) < 9:
            raise ValueError("Not enough parts for 'field' element")

        # NOTE: Optional name field is ignored!
        return field(
            kicad.symbols.type.field.from_str(int(part[0])),
            str(part[1]),
            int(part[2]),
            int(part[3]),
            kicad.config.symbols.FIELD_TEXT_SIZE if unify else int(part[4]),
            kicad.symbols.type.orientation.from_str(part[5]),
            kicad.symbols.type.visibility.from_str(part[6]),
            kicad.symbols.type.hjustify.from_str(part[7]),
            kicad.symbols.type.vjustify.from_str(part[8][:1]),
            kicad.symbols.type.style.from_str(part[8][1:])
        )
    elif char == 'P':
        if len(part) < 6:
            raise ValueError("Not enough parts for 'polygon' element")

        count = int(part[0])
        result = polygon(
            int(part[3]),
            kicad.symbols.type.fill.from_str(part[-1]),
            int(part[1]),
            kicad.symbols.type.representation.from_str(part[2])
        )

        for index in range(count):
            result.add(point(int(part[index * 2 + 4]), int(part[index * 2 + 5])))
        return result
    elif char == 'S':
        if len(part) != 8:
            raise ValueError("Not enough parts for 'rectangle' element")

        return rectangle(
            int(part[0]),
            int(part[1]),
            int(part[2]),
            int(part[3]),
            int(part[6]),
            kicad.symbols.type.fill.from_str(part[7]),
            int(part[4]),
            kicad.symbols.type.representation.from_str(part[5])
        )
    elif char == 'C':
        if len(part) != 7:
            raise ValueError("Not enough parts for 'circle' element")

        return circle(
            int(part[0]),
            int(part[1]),
            int(part[2]),
            int(part[5]),
            kicad.symbols.type.fill.from_str(part[6]),
            int(part[3]),
            kicad.symbols.type.representation.from_str(part[4])
        )
    elif char == 'A':
        if len(part) != 13:
            raise ValueError("Not enough parts for 'arc' element")

        return arc(
            int(part[0]), # x
            int(part[1]), # y
            int(part[9]), # startX
            int(part[10]), # startY
            int(part[11]), # endX
            int(part[12]), # endY
            int(part[3]) / 10, # startAngle
            int(part[4]) / 10, # endAngle
            int(part[2]), # radius
            int(part[7]), # thickness
            kicad.symbols.type.fill.from_str(part[8]), # fill
            int(part[5]), # unit
            kicad.symbols.type.representation.from_str(part[6]) # representation
        )
    elif char == 'T':
        # Old format
        if len(part) == 8:
            return text(
                int(part[1]), # x
                int(part[2]), # y
                part[7].replace('~', ' '), # value
                int(part[3]), # size
                int(part[0]) * 90.0, # angle
                kicad.symbols.type.italic.off,
                kicad.symbols.type.bold.off,
                kicad.symbols.type.hjustify.center,
                kicad.symbols.type.vjustify.center,
                int(part[5]), # unit
                kicad.symbols.type.representation.from_str(part[6]) # representation
            )
        # New format
        elif len(part) == 12:
            return text(
                int(part[1]), # x
                int(part[2]), # y
                part[7].replace("''", '"'), # value
                int(part[3]), # size
                int(part[0]) / 10, # angle
                kicad.symbols.type.italic.from_str(part[8]), # italic
                kicad.symbols.type.bold.from_str(part[9]), # bold
                kicad.symbols.type.hjustify.from_str(part[10]), # horizontal justify
                kicad.symbols.type.vjustify.from_str(part[11]), # vertical justify
                int(part[5]), # unit
                kicad.symbols.type.representation.from_str(part[6]) # representation
            )
        else:
            raise ValueError("Not enough parts for 'text' element")
    elif char == 'X':
        if len(part) == 12:
            visible = True
            if part[11][0] == 'N':
                visible = False
                part[11] = part[11][1:]
            shape = kicad.symbols.type.shape.line.from_str(part[11])
        elif len(part) == 11:
            visible = True
            shape = kicad.symbols.type.shape.line
        else:
            raise ValueError("Not enough parts for 'pin' element")

        return pin(
            int(part[2]), # x
            int(part[3]), # y
            part[0], # name
            part[1], # number
            int(part[4]), # length
            kicad.symbols.type.direction.from_str(part[5]), # direction
            kicad.config.symbols.PIN_NAME_SIZE if unify else int(part[6]), # nameSize
            kicad.config.symbols.PIN_NUMBER_SIZE if unify else int(part[7]), # numberSize
            kicad.symbols.type.electric.from_str(part[10]), # electric
            shape,
            visible,
            int(part[8]), # unit
            kicad.symbols.type.representation.from_str(part[9]), # representation
        )
    else:
        raise KeyError
