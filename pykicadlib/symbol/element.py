import re
import shlex
import datetime

import pykicadlib


def pin_value(value):
    '''Convert pin number into value (especially for BGA numbering scheme)'''

    res = re.match(r"[~0-9A-Z]+", value)
    if res:
        sum = 0
        for c in res.group(0):
            sum = sum * 128 + ord(c)
        return sum
    else:
        raise ValueError("'{}' is no valid pin value".format(value))


class alias(object):
    '''2.3.1 Aliases'''
    pass


class field(object):
    '''2.3.2 Component field'''

    fmt = 'F{:d} "{:s}" {:d} {:d} {:d} {:s} {:s} {:s} {:s}{:s} "{:s}"'

    def __init__(self, type, value, x, y, size, orientation, visibility, hjustify, vjustify, style):
        self.type = type
        self.value = str(value)
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


class boundary(object):

    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    @staticmethod
    def add(lhs, rhs):
        if isinstance(lhs, boundary) and isinstance(rhs, boundary):
            return boundary(
                min(lhs.x1, rhs.x1),
                min(lhs.y1, rhs.y1),
                max(lhs.x2, rhs.x2),
                max(lhs.y2, rhs.y2),
            )
        else:
            return boundary(0, 0, 0, 0)


class element(object):
    '''Component element'''

    def __init__(self, unit, representation, order):
        self.unit = unit
        self.representation = representation
        self.order = order
        self.id = None
        self.count = 0

    @property
    def priority(self):
        return self.unit * 1048576 + self.order * 65536

    @property
    def bounds(self):
        return boundary(0, 0, 0, 0)


class polygon(element):
    '''2.3.3.1 Polygon'''

    fmt = "P {:d} {:d} {:d} {:d} {:s}{:s}"
    order = 2

    def __init__(self, thickness, fill, unit = 0, representation = pykicadlib.symbol.type.representation.normal):
        super().__init__(unit, representation, polygon.order)

        self.thickness = thickness
        self.fill = fill
        self.points = []

    @property
    def priority(self):
        return self.unit * 1048576 + self.order * 65536 + len(self.points)

    @property
    def bounds(self):
        result = boundary(0, 0, 0, 0)
        for point in self.points:
            result.x1 = min(point.x, result.x1)
            result.y1 = min(point.y, result.y1)
            result.x2 = max(point.x, result.x2)
            result.y2 = max(point.y, result.y2)
        return result

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

    def __init__(self, x1, y1, x2, y2, thickness, fill, unit = 0, representation = pykicadlib.symbol.type.representation.normal):
        super().__init__(unit, representation, rectangle.order)

        # Swap x coordinates of second values are less than first values to make optimization possible
        if x1 > x2:
            self.x1 = x2
            self.x2 = x1
        else:
            self.x1 = x1
            self.x2 = x2

        # Swap y coordinates of second values are less than first values to make optimization possible
        if y1 > y2:
            self.y1 = y2
            self.y2 = y1
        else:
            self.y1 = y1
            self.y2 = y2

        self.thickness = thickness
        self.fill = fill

    @property
    def bounds(self):
        return boundary(self.x1, self.y1, self.x2, self.y2)

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

    def __init__(self, x, y, radius, thickness, fill, unit = 0, representation = pykicadlib.symbol.type.representation.normal):
        super().__init__(unit, representation, circle.order)

        self.x = x
        self.y = y
        self.radius = radius
        self.thickness = thickness
        self.fill = fill

    @property
    def bounds(self):
        return boundary(self.x - self.radius, self.y - self.radius, self.x + self.radius, self.y + self.radius)

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

    def __init__(self, x, y, startX, startY, endX, endY, startAngle, endAngle, radius, thickness, fill, unit = 0, representation = pykicadlib.symbol.type.representation.normal):
        super().__init__(unit, representation, arc.order)

        # Swap x coordinates of second values are less than first values to make optimization possible
        if startX > endX:
            self.startX = endX
            self.endX = startX
        else:
            self.startX = startX
            self.endX = endX

        # Swap y coordinates of second values are less than first values to make optimization possible
        if startY > endY:
            self.startY = endY
            self.endY = startY
        else:
            self.startY = startY
            self.endY = endY

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

    @property
    def bounds(self):
        # FIXME: Not exact!
        return boundary(self.x - self.radius, self.y - self.radius, self.x + self.radius, self.y + self.radius)

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

    def __init__(self, x, y, value, size, angle, italic = pykicadlib.symbol.type.italic.off, bold = pykicadlib.symbol.type.bold.off, hjustify = pykicadlib.symbol.type.hjustify.center, vjustify = pykicadlib.symbol.type.vjustify.center, unit = 0, representation = pykicadlib.symbol.type.representation.normal):
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

    @property
    def bounds(self):
        # NOTE: Ignore for the moment!
        return boundary(self.x, self.y, self.x, self.y)

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

    def __init__(self, x, y, name, number, length, direction, nameSize, numberSize, electric = pykicadlib.symbol.type.electric.input, shape = pykicadlib.symbol.type.shape.line, visible = True, unit = 0, representation = pykicadlib.symbol.type.representation.normal):
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

    @property
    def priority(self):
        return self.unit * 1048576 + self.order * 65536 + pin_value(self.number)

    @property
    def bounds(self):
        result = boundary(self.x, self.y, self.x, self.y)
        if self.direction == pykicadlib.symbol.type.direction.left:
            result.x1 -= self.length
        elif self.direction == pykicadlib.symbol.type.direction.right:
            result.x2 += self.length
        elif self.direction == pykicadlib.symbol.type.direction.up:
            result.y1 -= self.length
        elif self.direction == pykicadlib.symbol.type.direction.down:
            result.y2 += self.length
        return result

    def __eq__(self, other):
        '''Compare only same instances'''

        if not isinstance(other, pin):
            return False

    #   return self.x == other.x and self.y == other.y and self.length == other.length and self.name == other.name and self.number == other.number
        return False

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
            pykicadlib.symbol.type.field.from_str(int(part[0])),
            str(part[1]),
            int(part[2]),
            int(part[3]),
            pykicadlib.config.symbol.FIELD_TEXT_SIZE if unify else int(part[4]),
            pykicadlib.symbol.type.orientation.from_str(part[5]),
            pykicadlib.symbol.type.visibility.from_str(part[6]),
            pykicadlib.symbol.type.hjustify.from_str(part[7]),
            pykicadlib.symbol.type.vjustify.from_str(part[8][:1]),
            pykicadlib.symbol.type.style.from_str(part[8][1:])
        )
    elif char == 'P':
        if len(part) < 6:
            raise ValueError("Not enough parts for 'polygon' element")

        count = int(part[0])
        result = polygon(
            int(part[3]),
            pykicadlib.symbol.type.fill.from_str(part[-1]),
            int(part[1]),
            pykicadlib.symbol.type.representation.from_str(part[2])
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
            pykicadlib.symbol.type.fill.from_str(part[7]),
            int(part[4]),
            pykicadlib.symbol.type.representation.from_str(part[5])
        )
    elif char == 'C':
        if len(part) != 7:
            raise ValueError("Not enough parts for 'circle' element")

        return circle(
            int(part[0]),
            int(part[1]),
            int(part[2]),
            int(part[5]),
            pykicadlib.symbol.type.fill.from_str(part[6]),
            int(part[3]),
            pykicadlib.symbol.type.representation.from_str(part[4])
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
            pykicadlib.symbol.type.fill.from_str(part[8]), # fill
            int(part[5]), # unit
            pykicadlib.symbol.type.representation.from_str(part[6]) # representation
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
                pykicadlib.symbol.type.italic.off,
                pykicadlib.symbol.type.bold.off,
                pykicadlib.symbol.type.hjustify.center,
                pykicadlib.symbol.type.vjustify.center,
                int(part[5]), # unit
                pykicadlib.symbol.type.representation.from_str(part[6]) # representation
            )
        # New format
        elif len(part) == 12:
            return text(
                int(part[1]), # x
                int(part[2]), # y
                part[7].replace("''", '"'), # value
                int(part[3]), # size
                int(part[0]) / 10, # angle
                pykicadlib.symbol.type.italic.from_str(part[8]), # italic
                pykicadlib.symbol.type.bold.from_str(part[9]), # bold
                pykicadlib.symbol.type.hjustify.from_str(part[10]), # horizontal justify
                pykicadlib.symbol.type.vjustify.from_str(part[11]), # vertical justify
                int(part[5]), # unit
                pykicadlib.symbol.type.representation.from_str(part[6]) # representation
            )
        else:
            raise ValueError("Not enough parts for 'text' element")
    elif char == 'X':
        if len(part) == 12:
            visible = True
            if part[11][0] == 'N':
                visible = False
                part[11] = part[11][1:]
            shape = pykicadlib.symbol.type.shape.line.from_str(part[11])
        elif len(part) == 11:
            visible = True
            shape = pykicadlib.symbol.type.shape.line
        else:
            raise ValueError("Not enough parts for 'pin' element")

        return pin(
            int(part[2]), # x
            int(part[3]), # y
            part[0], # name
            part[1], # number
            int(part[4]), # length
            pykicadlib.symbol.type.direction.from_str(part[5]), # direction
            pykicadlib.config.symbol.PIN_NAME_SIZE if unify else int(part[6]), # nameSize
            pykicadlib.config.symbol.PIN_NUMBER_SIZE if unify else int(part[7]), # numberSize
            pykicadlib.symbol.type.electric.from_str(part[10]), # electric
            shape,
            visible,
            int(part[8]), # unit
            pykicadlib.symbol.type.representation.from_str(part[9]), # representation
        )
    else:
        raise KeyError
