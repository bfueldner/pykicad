# pylint: disable=too-many-instance-attributes, too-few-public-methods
"""
.. py::module:: pykicadlib.symbol.elements
   :synopsis: KiCAD symbol elements

.. moduleauthor:: Benjamin Füldner <benjamin@fueldner.net>
"""

import re
import shlex

import pykicadlib


def pin_value(value):
    """Convert pin number into value (especially for BGA numbering scheme)"""

    res = re.match(r'[~0-9A-Z]+', value)
    if res:
        _sum = 0
        for _chr in res.group(0):
            _sum = _sum * 128 + ord(_chr)
        return _sum
    raise ValueError("'{}' is no valid pin value".format(value))


# Section 2.3.1 in fileformat.pdf
class Alias():
    """Aliases"""


# Section 2.3.2 in fileformat.pdf
class Field():
    """Component field

    :param types.Field type:
        Type of :class:`Field`
    :param str value:
        Value of :class:`Field` text
    :param int x:
        X coordinate
    :param int y:
        Y coordinate
    :param int size:
        Text size
    :param Orientation orientation:
        Text orientation
    :param Visibility visibility:
        Text visibility
    :param HJustify hjustify:
        Horizontal text justify
    :param VJustify vjustify:
        Vertical text justify
    :param Style style:
        Text style

    .. automethod:: __str__
    """

    fmt = 'F{:d} "{:s}" {:d} {:d} {:d} {:s} {:s} {:s} {:s}{:s} "{:s}"'

    # pylint: disable=too-many-arguments, redefined-builtin
    def __init__(
            self,
            type,
            value,
            x, y,
            size,
            orientation,
            visibility,
            hjustify,
            vjustify,
            style):
        self.type = type                #: Type of :class:`Field`
        self.value = value              #: Value of :class:`Field` text
        self.x = x                      #: X coordinate
        self.y = y                      #: Y coordinate
        self.size = size                #: Text size
        self.orientation = orientation  #: Text orientation
        self.visibility = visibility    #: Text visibility
        self.hjustify = hjustify        #: Horizontal text justify
        self.vjustify = vjustify        #: Vertical text justify
        self.style = style              #: Text style

    def __str__(self):
        """Return :class:`Field` in KiCAD format"""

        return Field.fmt.format(
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


class Point():
    """Point helper

    :param int x:
        X coordinate
    :param int y:
        Y coordinate

    :attributes:
        * x (int) - X cord

    .. automethod:: __eq__
    .. automethod:: __str__
    """

    fmt = "{:d} {:d}"

    def __init__(self, x, y):
        self.x = x  #: X coordinate
        self.y = y  #: Y coordinate

    def __eq__(self, other):
        """Compare :class:`Point` instances

        :returns:
            ``True``, if ``other`` == :class:`Point` and all attributes match. Otherwise ``False``.
        """

        if not isinstance(other, Point):
            return False

        return self.x == other.x and self.y == other.y

    def __str__(self):
        """Return :class:`Point` in KiCAD format"""

        return Point.fmt.format(
            self.x,
            self.y,
        )


class Boundary():
    """Element/symbol boundary class

    :param int x1:
        X1 coordinate
    :param int y1:
        Y1 coordinate
    :param int x2:
        X2 coordinate
    :param int y2:
        Y2 coordinate

    .. automethod:: __add__
    """

    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1    #: X1 coordinate
        self.y1 = y1    #: Y1 coordinate
        self.x2 = x2    #: X2 coordinate
        self.y2 = y2    #: Y2 coordinate

    def __add__(self, other):
        """Merge boundary from ``other`` object with own boundary.

        :param Boundary other:
            Object to merge with
        :returns:
            Boundary of both merged objects
        :rtype:
            Boundary
        """

        if isinstance(other, Boundary):
            return Boundary(
                min(self.x1, other.x1),
                min(self.y1, other.y1),
                max(self.x2, other.x2),
                max(self.y2, other.y2),
            )
        return Boundary(self.x1, self.y1, self.x2, self.y2)


class Element():
    """Element base class

    :param int unit:
        Unit number
    :param Representation representation:
        Element representation
    :param int order:
        Order number
    """

    def __init__(self, unit, representation, order):
        self.unit = unit
        self.representation = representation
        self.order = order
        self.id = None
        """Element id"""

        self.count = 0

    @property
    def priority(self):
        """Element priority depending on order and unit.

        :type:
            int
        """

        return self.unit * 0x100000 + self.order * 0x10000

    @property
    def bounds(self):
        """Element boundary.

        :type:
            Boundary
        """

        return Boundary(0, 0, 0, 0)


# Section 2.3.3.1 in fileformat.pdf
class Polygon(Element):
    """Polygon

    :param int thickness:
        Thickness of outline
    :param Fill fill:
        Fill type
    :param int unit:
        Unit index
    :param Representation representation:
        Representation type

    .. automethod:: __eq__
    .. automethod:: __str__
    """

    fmt = "P {:d} {:d} {:d} {:d} {:s}{:s}"
    order = 2

    def __init__(
            self,
            thickness,
            fill,
            unit=0,
            representation=pykicadlib.symbol.types.Representation.normal):
        super().__init__(unit, representation, Polygon.order)

        self.thickness = thickness  #: Thickness of outline
        self.fill = fill            #: Fill type
        self.points = []            #: Outline points

    @property
    def priority(self):
        return super() + len(self.points)

    @property
    def bounds(self):
        result = Boundary(0, 0, 0, 0)
        for point in self.points:
            result.x1 = min(point.x, result.x1)
            result.y1 = min(point.y, result.y1)
            result.x2 = max(point.x, result.x2)
            result.y2 = max(point.y, result.y2)
        return result

    def add(self, point):
        """Add point to polygon

        :param Point point:
            Point to add
        """

        self.points.append(point)

    def remove(self, index):
        """Remove element from polygon

        :param int index:
            Index of point to remove
        """

        del self.points[index]

    def __eq__(self, other):
        """Compare :class:`Polygon` instances"""

        if not isinstance(other, Polygon):
            return False

        if len(self.points) != len(other.points):
            return False

        for point1, point2 in zip(self.points, other.points):
            if point1 != point2:
                return False
        return True

    def __str__(self):
        """Return :class:`Polygon` in KiCAD format"""

        points = ''
        for point in self.points:
            points += str(point) + ' '

        return Polygon.fmt.format(
            len(self.points),
            self.unit,
            self.representation.value,
            self.thickness,
            points,
            self.fill
        )


# Section 2.3.3.2 in fileformat.pdf
class Rectangle(Element):
    """Rectangle from ``x1``/``y1`` to ``x2``/``y2``.

    :param int x1:
        X1 coordinate
    :param int y1:
        Y1 coordinate
    :param int x2:
        X2 coordinate
    :param int y2:
        Y2 coordinate
    :param int thickness:
        Thickness of outline
    :param Fill fill:
        Fill type
    :param int unit:
        Unit index
    :param Representation representation:
        Representation type

    .. automethod:: __eq__
    .. automethod:: __str__
    """

    fmt = 'S {:d} {:d} {:d} {:d} {:d} {:s} {:d} {:s}'
    order = 1

    # pylint: disable=too-many-arguments
    def __init__(
            self,
            x1,
            y1,
            x2,
            y2,
            thickness,
            fill,
            unit=0,
            representation=pykicadlib.symbol.types.Representation.normal):
        super().__init__(unit, representation, Rectangle.order)

        # Swap x coordinates of second values are less than first
        # values to make optimization possible
        if x1 > x2:
            self.x1 = x2            #: X1 coordinate
            self.x2 = x1            #: X2 coordinate
        else:
            self.x1 = x1
            self.x2 = x2

        # Swap y coordinates of second values are less than first
        # values to make optimization possible
        if y1 > y2:
            self.y1 = y2            #: Y1 coordinate
            self.y2 = y1            #: Y2 coordinate
        else:
            self.y1 = y1
            self.y2 = y2

        self.thickness = thickness  #: Thickness of outline
        self.fill = fill            #: Fill type

    @property
    def bounds(self):
        return Boundary(self.x1, self.y1, self.x2, self.y2)

    def __eq__(self, other):
        """Compare :class:`Rectangle` instances"""

        if not isinstance(other, Rectangle):
            return False

        return self.x1 == other.x1 and self.y1 == other.y1 and \
            self.x2 == other.x2 and self.y2 == other.y2

    def __str__(self):
        """Return :class:`Rectangle` in KiCAD format"""

        return Rectangle.fmt.format(
            self.x1,
            self.y1,
            self.x2,
            self.y2,
            self.unit,
            self.representation,
            self.thickness,
            self.fill
        )


# Section 2.3.3.3 in fileformat.pdf
class Circle(Element):
    """Circle with center at ``x``/``y`` and ``radius``.

    :param int x:
        X coordinate
    :param int y:
        Y coordinate
    :param int radius:
        Circle radius
    :param int thickness:
        Thickness of outline
    :param Fill fill:
        Fill type
    :param int unit:
        Unit index
    :param Representation representation:
        Representation type

    .. automethod:: __eq__
    .. automethod:: __str__
    """

    fmt = 'C {:d} {:d} {:d} {:d} {:d} {:d} {:s}'
    order = 3

    # pylint: disable=too-many-arguments
    def __init__(
            self,
            x,
            y,
            radius,
            thickness,
            fill,
            unit=0,
            representation=pykicadlib.symbol.types.Representation.normal):
        super().__init__(unit, representation, Circle.order)

        self.x = x                  #: X coordinate
        self.y = y                  #: Y coordinate
        self.radius = radius        #: Circle radius
        self.thickness = thickness  #: Thickness of outline
        self.fill = fill            #: Fill type

    @property
    def bounds(self):
        return Boundary(
            self.x - self.radius, self.y - self.radius, self.x + self.radius, self.y + self.radius)

    def __eq__(self, other):
        """Compare :class:`Circle` instances"""

        if not isinstance(other, Circle):
            return False

        return self.x == other.x and self.y == other.y and self.radius == other.radius

    def __str__(self):
        """Return :class:`Circle` in KiCAD format"""

        return Circle.fmt.format(
            self.x,
            self.y,
            self.radius,
            self.unit,
            self.representation.value,
            self.thickness,
            self.fill
        )


# Section 2.3.3.4 in fileformat.pdf
class Arc(Element):
    """Arc with center at ``x``/``y`` and ``radius``.

    :param int x:
        X coordinate
    :param int y:
        Y coordinate
    :param int start_x:
        Start X coordinate
    :param int start_y:
        Start Y coordinate
    :param int end_x:
        End X coordinate
    :param int end_y:
        End Y coordinate
    :param int start_angle:
        Start angle (?..?)
    :param int end_angle:
        End angle (?..?)
    :param int radius:
        Arc radius
    :param int thickness:
        Thickness of outline
    :param Fill fill:
        Fill type
    :param int unit:
        Unit index
    :param Representation representation:
        Representation type

    .. automethod:: __eq__
    .. automethod:: __str__
    """

    fmt = 'A {:d} {:d} {:d} {:.0f} {:.0f} {:d} {:d} {:d} {:s} {:d} {:d} {:d} {:d}'
    order = 4

    # pylint: disable=too-many-arguments
    def __init__(
            self,
            x, y,
            start_x, start_y,
            end_x, end_y,
            start_angle, end_angle,
            radius,
            thickness,
            fill,
            unit=0,
            representation=pykicadlib.symbol.types.Representation.normal):
        super().__init__(unit, representation, Arc.order)

        # Swap x coordinates of second values are less than first
        # values to make optimization possible
        # if start_x > end_x:
        #    self.start_x = end_x
        #    self.end_x = start_x
        # else:
        #    self.start_x = start_x
        #    self.end_x = end_x

        # Swap y coordinates of second values are less than first
        # values to make optimization possible
        # if start_y > end_y:
        #    self.start_y = end_y
        #    self.end_y = start_y
        # else:
        #    self.start_y = start_y
        #    self.end_y = end_y

        self.x = x                      #: X coordinate
        self.y = y                      #: Y coordinate
        self.start_x = start_x          #: Start X coordinate
        self.start_y = start_y          #: Start Y coordinate
        self.end_x = end_x              #: End X coordinate
        self.end_y = end_y              #: End Y coordinate
        self.start_angle = start_angle  #: Start angle
        self.end_angle = end_angle      #: End angle
        self.radius = radius            #: Arc radius
        self.thickness = thickness      #: Thickness of outline
        self.fill = fill                #: Fill type

    @property
    def bounds(self):
        # Not exact!
        return Boundary(
            self.x - self.radius,
            self.y - self.radius,
            self.x + self.radius,
            self.y + self.radius)

    def __eq__(self, other):
        """Compare :class:`Arc` instances"""

        if not isinstance(other, Arc):
            return False

        return self.x == other.x and self.y == other.y and \
            self.start_x == other.start_x and self.start_y == other.start_y and \
            self.end_x == other.end_x and self.end_y == other.end_y and \
            self.start_angle == other.start_angle and self.end_angle == other.end_angle and \
            self.radius == other.radius

    def __str__(self):
        """Return :class:`Arc` in KiCAD format"""

        return Arc.fmt.format(
            self.x,
            self.y,
            self.radius,
            self.start_angle * 10,
            self.end_angle * 10,
            self.unit,
            self.representation.value,
            self.thickness,
            self.fill,
            self.start_x,
            self.start_y,
            self.end_x,
            self.end_y
        )


# Section 2.3.3.5 in fileformat.pdf
class Text(Element):
    """Text at ``x``/``y`` with ``value``, ``size``, ``angle`` and multiple style options.
    New format since 2.4?

    :param int x:
        X coordinate
    :param int y:
        Y coordinate
    :param str value:
        Text value
    :param int size:
        Text size
    :param int angle:
        Text angle
    :param Italic italic:
        Text italic style
    :param Bold bold:
        Text bold style
    :param HJustify hjustify:
        Horizontal text justify
    :param VJustify vjustify:
        Vertical text justify
    :param int unit:
        Unit index
    :param Representation representation:
        Representation type

    .. automethod:: __eq__
    .. automethod:: __str__
    """

    fmt = 'T {:.0f} {:d} {:d} {:d} 0 {:d} {:d} "{:s}" {:s} {:d} {:s} {:s}'
    order = 0

    # pylint: disable=too-many-arguments
    def __init__(
            self,
            x,
            y,
            value,
            size,
            angle,
            italic=pykicadlib.symbol.types.Italic.off,
            bold=pykicadlib.symbol.types.Bold.off,
            hjustify=pykicadlib.symbol.types.HJustify.center,
            vjustify=pykicadlib.symbol.types.VJustify.center,
            unit=0,
            representation=pykicadlib.symbol.types.Representation.normal):
        super().__init__(unit, representation, Text.order)

        self.x = x                  #: X coordinate
        self.y = y                  #: Y coordinate
        self.value = value          #: Text value
        self.size = size            #: Text size
        self.angle = angle          #: Text angle
        self.italic = italic        #: Text italic style
        self.bold = bold            #: Text bold style
        self.hjustify = hjustify    #: Horizontal text justify
        self.vjustify = vjustify    #: Vertical text justify

    @property
    def bounds(self):
        # NOTE: Ignore for the moment!
        return Boundary(self.x, self.y, self.x, self.y)

    def __eq__(self, other):
        """Compare :class:`Text` instances"""

        if not isinstance(other, Text):
            return False

        return self.x == other.x and self.y == other.y and self.value == other.value

    def __str__(self):
        """Return :class:`Text` in KiCAD format"""

        return Text.fmt.format(
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


# Section 2.3.4 in fileformat.pdf
class Pin(Element):
    """Pin at ``x``/``y`` with ``name``/``number``.

    :param int x:
        X coordinate
    :param int y:
        Y coordinate
    :param str name:
        Pin name
    :param str number:
        Pin number
    :param int length:
        Pin length
    :param Direction direction:
        Pin direction
    :param int name_size:
        Pin name size
    :param int number_size:
        Pin number size
    :param Electric electric:
        Electric type
    :param Shape shape:
        Shape type
    :param bool visible:
        Visibility
    :param int unit:
        Unit index
    :param Representation representation:
        Representation type

    .. automethod:: __eq__
    .. automethod:: __str__
    """

    fmt = 'X {:s} {:s} {:d} {:d} {:d} {:s} {:d} {:d} {:d} {:d} {:s} {:s}{:s}'
    order = 10

    # pylint: disable=too-many-arguments
    def __init__(
            self,
            x,
            y,
            name,
            number,
            length,
            direction,
            name_size,
            number_size,
            electric=pykicadlib.symbol.types.Electric.input,
            shape=pykicadlib.symbol.types.Shape.line,
            visible=True,
            unit=0,
            representation=pykicadlib.symbol.types.Representation.normal):
        super().__init__(unit, representation, Pin.order)

        self.x = x                      #: X coordinate
        self.y = y                      #: Y coordinate
        self.name = name                #: Pin name
        self.number = number            #: Pin number
        self.length = length            #: Pin length
        self.direction = direction      #: Pin direction
        self.name_size = name_size      #: Pin name size
        self.number_size = number_size  #: Pin number size
        self.electric = electric        #: Electric type
        self.shape = shape              #: Shape type
        self.visible = visible          #: Visibility

    @property
    def priority(self):
        return self.unit * 1048576 + self.order * 65536 + pin_value(self.number)

    @property
    def bounds(self):
        result = Boundary(self.x, self.y, self.x, self.y)
        if self.direction == pykicadlib.symbol.types.Direction.left:
            result.x1 -= self.length
        elif self.direction == pykicadlib.symbol.types.Direction.right:
            result.x2 += self.length
        elif self.direction == pykicadlib.symbol.types.Direction.up:
            result.y1 -= self.length
        elif self.direction == pykicadlib.symbol.types.Direction.down:
            result.y2 += self.length
        return result

    def __eq__(self, other):
        """Compare :class:`Pin` instances"""

        if not isinstance(other, Pin):
            return False

    #   return self.x == other.x and self.y == other.y and \
    #       self.length == other.length and self.name == other.name and self.number == other.number
        return False

    def __str__(self):
        """Return :class:`Pin` in KiCAD format"""

        return Pin.fmt.format(
            self.name,
            self.number,
            self.x,
            self.y,
            self.length,
            self.direction,
            self.name_size,
            self.number_size,
            self.unit,
            self.representation.value,
            self.electric,
            'N' if not self.visible else '',
            self.shape
        ).rstrip()


# pylint: disable=too-many-return-statements,too-many-branches
def from_str(string):
    """Generate elements out of string statements. Used to load a KiCAD symbol file line by line.

    >>> element = pykicadlib.symbol.elements.from_str("S 10 10 20 20 0 1 5 N")
    >>> type(element)
    <class 'pykicadlib.symbol.elements.Rectangle'>
    >>> print(element)
    S 10 10 20 20 0 1 5 N

    :param str string:
        KiCAD symbol line to parse.
    :return:
        Element object depending on input string.
    :rtype:
        symbol.elements.Arc,
        symbol.elements.Circle,
        symbol.elements.Field,
        symbol.elements.Pin,
        symbol.elements.Polygon,
        symbol.elements.Rectangle,
        symbol.elements.Text
    :raises:
        KeyError, ValueError
    """

    string = string.strip()
    char = string[0]
    part = shlex.split(string[1:])

    if char == 'F':
        if len(part) < 9:
            raise ValueError("Not enough parts for 'Field' element")

        # NOTE: Optional name field is ignored!
        return Field(
            pykicadlib.symbol.types.Field.from_str(int(part[0])),
            str(part[1]),
            int(part[2]),
            int(part[3]),
            int(part[4]),
            pykicadlib.symbol.types.Orientation.from_str(part[5]),
            pykicadlib.symbol.types.Visibility.from_str(part[6]),
            pykicadlib.symbol.types.HJustify.from_str(part[7]),
            pykicadlib.symbol.types.VJustify.from_str(part[8][:1]),
            pykicadlib.symbol.types.Style.from_str(part[8][1:])
        )

    if char == 'P':
        if len(part) < 6:
            raise ValueError("Not enough parts for 'Polygon' element")

        count = int(part[0])
        result = Polygon(
            int(part[3]),
            pykicadlib.symbol.types.Fill.from_str(part[-1]),
            int(part[1]),
            pykicadlib.symbol.types.Representation.from_str(part[2])
        )

        for index in range(count):
            result.add(Point(int(part[index * 2 + 4]), int(part[index * 2 + 5])))
        return result

    if char == 'S':
        if len(part) != 8:
            raise ValueError("Not enough parts for 'Rectangle' element")

        return Rectangle(
            int(part[0]),
            int(part[1]),
            int(part[2]),
            int(part[3]),
            int(part[6]),
            pykicadlib.symbol.types.Fill.from_str(part[7]),
            int(part[4]),
            pykicadlib.symbol.types.Representation.from_str(part[5])
        )

    if char == 'C':
        if len(part) != 7:
            raise ValueError("Not enough parts for 'Circle' element")

        return Circle(
            int(part[0]),
            int(part[1]),
            int(part[2]),
            int(part[5]),
            pykicadlib.symbol.types.Fill.from_str(part[6]),
            int(part[3]),
            pykicadlib.symbol.types.Representation.from_str(part[4])
        )

    if char == 'A':
        if len(part) != 13:
            raise ValueError("Not enough parts for 'Arc' element")

        return Arc(
            int(part[0]),                                                   # x
            int(part[1]),                                                   # y
            int(part[9]),                                                   # start_x
            int(part[10]),                                                  # start_y
            int(part[11]),                                                  # end_x
            int(part[12]),                                                  # end_y
            int(part[3]) / 10,                                              # start_angle
            int(part[4]) / 10,                                              # end_angle
            int(part[2]),                                                   # radius
            int(part[7]),                                                   # thickness
            pykicadlib.symbol.types.Fill.from_str(part[8]),                 # fill
            int(part[5]),                                                   # unit
            pykicadlib.symbol.types.Representation.from_str(part[6])        # representation
        )

    if char == 'T':
        # Old format
        if len(part) == 8:
            return Text(
                int(part[1]),                                               # x
                int(part[2]),                                               # y
                part[7].replace('~', ' '),                                  # value
                int(part[3]),                                               # size
                int(part[0]) * 90.0,                                        # angle
                pykicadlib.symbol.types.Italic.off,                         # italic
                pykicadlib.symbol.types.Bold.off,                           # bold
                pykicadlib.symbol.types.HJustify.center,                    # horizontal justify
                pykicadlib.symbol.types.VJustify.center,                    # vertical justify
                int(part[5]),                                               # unit
                pykicadlib.symbol.types.Representation.from_str(part[6])    # representation
            )

        # New format
        if len(part) == 12:
            return Text(
                int(part[1]),                                               # x
                int(part[2]),                                               # y
                part[7].replace("''", '"'),                                 # value
                int(part[3]),                                               # size
                int(part[0]) / 10,                                          # angle
                pykicadlib.symbol.types.Italic.from_str(part[8]),           # italic
                pykicadlib.symbol.types.Bold.from_str(part[9]),             # bold
                pykicadlib.symbol.types.HJustify.from_str(part[10]),        # horizontal justify
                pykicadlib.symbol.types.VJustify.from_str(part[11]),        # vertical justify
                int(part[5]),                                               # unit
                pykicadlib.symbol.types.Representation.from_str(part[6])    # representation
            )

        raise ValueError("Not enough parts for 'Text' element")

    if char == 'X':
        if len(part) == 12:
            visible = True
            if part[11][0] == 'N':
                visible = False
                part[11] = part[11][1:]
            shape = pykicadlib.symbol.types.Shape.from_str(part[11])
        elif len(part) == 11:
            visible = True
            shape = pykicadlib.symbol.types.Shape.line
        else:
            raise ValueError("Not enough parts for 'Pin' element")

        return Pin(
            int(part[2]),                                                   # x
            int(part[3]),                                                   # y
            part[0],                                                        # name
            part[1],                                                        # number
            int(part[4]),                                                   # length
            pykicadlib.symbol.types.Direction.from_str(part[5]),            # direction
            int(part[6]),                                                   # name_size
            int(part[7]),                                                   # number_size
            pykicadlib.symbol.types.Electric.from_str(part[10]),            # electric
            shape,
            visible,
            int(part[8]),                                                   # unit
            pykicadlib.symbol.types.Representation.from_str(part[9]),       # representation
        )

    raise KeyError
