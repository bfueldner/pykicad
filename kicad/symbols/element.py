import datetime

import kicad.symbols.type

class alias(object):
    '''2.3.1 Aliases'''
    pass

class field(object):
    '''2.3.2 Component field'''

    fmt = 'F{} "{}" {} {} {} {} {} {} {}{} "{}"'

    def __init__(self, type, text, x, y, dimension, orientation, visibility, hjustify, vjustify, style):
        self.type = type
        self.text = text
        self.x = x
        self.y = y
        self.dimension = dimension
        self.orientation = orientation
        self.visibility = visibility
        self.hjustify = hjustify
        self.vjustify = vjustify
        self.style = style

    def __str__(self):
        return field.fmt.format(
            self.type.value,
            self.text,
            self.x,
            self.y,
            self.dimension,
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
        return self.unit * 65536 + self.order * 256

class polygon(element):
    '''2.3.3.1 Polygon'''

    fmt = "P {:d} {:d} {:s} {:d} {:s}{:s}"
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
        return self.unit * 65536 + self.order * 256 + len(self.points)

    def __str__(self):
        points = ''
        for point in self.points:
            points += str(point) + ' '

        return polygon.fmt.format(
            len(self.points),
            self.unit,
            self.representation,
            self.thickness,
            points,
            self.fill
        )

class rectangle(element):
    '''2.3.3.2 Rectangle'''

    fmt = 'S {:d} {:d} {:d} {:d} {:d} {:s} {:d} {:s}'
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
            self.representation,
            self.thickness,
            self.fill
        )

class circle(element):
    '''2.3.3.3 Circle'''

    fmt = 'C {:d} {:d} {:d} {:d} {:s} {:d} {:s}'
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
            self.representation,
            self.thickness,
            self.fill
        )

class arc(element):
    '''2.3.3.4 Arc'''

    fmt = 'A {:d} {:d} {:d} {:.0f} {:.0f} {:d} {:s} {:d} {:s} {:d} {:d} {:d} {:d}'
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
            self.representation,
            self.thickness,
            self.fill,
            self.startX,
            self.startY,
            self.endX,
            self.endY
        )

class text(element):
    '''2.3.3.5 Text'''
    pass

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

def from_str(string):
    '''Generate elements out of string lines. Used to load a symbol file'''

    string = string.strip()
    char = string[0]
    part = string[1:].split()
    if char == 'F':
        # NOTE: Optional name field is ignored!
        return field(
            kicad.symbols.type.field.from_str(int(part[0])),
            str(part[1]),
            int(part[2]),
            int(part[3]),
            int(part[4]),
            kicad.symbols.type.orientation.from_str(part[5]),
            kicad.symbols.type.visibility.from_str(part[6]),
            kicad.symbols.type.hjustify.from_str(part[7]),
            kicad.symbols.type.vjustify.from_str(part[8][:1]),
            kicad.symbols.type.style.from_str(part[8][1:])
        )
    else:
        raise KeyError
    return None
