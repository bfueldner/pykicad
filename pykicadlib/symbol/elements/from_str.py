# pylint: disable=too-many-instance-attributes, too-few-public-methods
"""KiCAD symbol elements from string.

.. py::module:: pykicadlib.symbol.elements.from_str
   :synopsis: KiCAD symbol elements from string

.. moduleauthor:: Benjamin Füldner <benjamin@fueldner.net>
"""

import shlex
from pykicadlib.config import Symbol
from pykicadlib.symbol.elements import Arc, Circle, Field, Pin, Polygon, Rectangle, Text


# pylint: disable=too-many-return-statements,too-many-branches,too-many-statements
def from_str(string, unify=True):
    """Generate elements out of string statements. Used to load a KiCAD symbol file line by line.

    >>> element = pykicadlib.symbol.elements.from_str("S 10 10 20 20 0 1 5 N")
    >>> type(element)
    <class 'pykicadlib.symbol.elements.Rectangle'>
    >>> print(element)
    S 10 10 20 20 0 1 5 N

    :param str string:
        KiCAD symbol line to parse.
    :param bool unify:
        Unify text sizes with pykicadlib.config.
    :return:
        Element object depending on input string.
    :rtype:
        symbol.elements.arc.Arc,
        symbol.elements.circle.Circle,
        symbol.elements.field.Field,
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
        result = Field(
            Field.Type.from_str(int(part[0])),
            int(part[2]),
            int(part[3]),
            str(part[1])
        )
        result.size = Symbol.FIELD_TEXT_SIZE if unify else int(part[4])
        result.orientation = Field.Orientation.from_str(part[5])
        result.visibility = Field.Visibility.from_str(part[6])
        result.hjustify = Field.HJustify.from_str(part[7])
        result.vjustify = Field.VJustify.from_str(part[8][:1])
        result.style = Field.Style.from_str(part[8][1:])
        return result

    if char == 'P':
        if len(part) < 6:
            raise ValueError("Not enough parts for 'Polygon' element")

        count = int(part[0])
        result = Polygon()
        result.unit = int(part[1])
        result.representation = Polygon.Representation.from_str(part[2])
        result.thickness = int(part[3])
        result.fill = Polygon.Fill.from_str(part[-1])

        for index in range(count):
            result.add(Polygon.Point(int(part[index * 2 + 4]), int(part[index * 2 + 5])))
        return result

    if char == 'S':
        if len(part) != 8:
            raise ValueError("Not enough parts for 'Rectangle' element")

        result = Rectangle(
            int(part[0]),
            int(part[1]),
            int(part[2]),
            int(part[3])
        )
        result.unit = int(part[4])
        result.representation = Rectangle.Representation.from_str(part[5])
        result.thickness = int(part[6])
        result.fill = Rectangle.Fill.from_str(part[7])
        return result

    if char == 'C':
        if len(part) != 7:
            raise ValueError("Not enough parts for 'Circle' element")

        result = Circle(
            int(part[0]),
            int(part[1]),
            int(part[2])
        )
        result.unit = int(part[3])
        result.representation = Circle.Representation.from_str(part[4])
        result.thickness = int(part[5])
        result.fill = Circle.Fill.from_str(part[6])
        return result

    if char == 'A':
        if len(part) != 13:
            raise ValueError("Not enough parts for 'Arc' element")

        result = Arc(
            int(part[0]),                       # x
            int(part[1]),                       # y
            int(part[2]),                       # radius
            int(part[9]),                       # start_x
            int(part[10]),                      # start_y
            int(part[11]),                      # end_x
            int(part[12]),                      # end_y
            int(part[3]) / 10,                  # start_angle
            int(part[4]) / 10                   # end_angle
        )
        result.unit = int(part[5])
        result.representation = Arc.Representation.from_str(part[6])
        result.thickness = int(part[7])
        result.fill = Arc.Fill.from_str(part[8])
        return result

    if char == 'T':
        # Old format
        if len(part) == 8:
            result = Text(
                int(part[1]),                   # x
                int(part[2]),                   # y
                part[7].replace('~', ' '),      # value
                int(part[3])                    # size
            )
            result.angle = int(part[0]) * 90.0
            result.unit = int(part[5])
            result.representation = Text.Representation.from_str(part[6])
            return result

        # New format
        if len(part) == 12:
            result = Text(
                int(part[1]),                   # x
                int(part[2]),                   # y
                part[7].replace("''", '"'),     # value
                int(part[3])                    # size
            )
            result.angle = int(part[0]) / 10
            result.unit = int(part[5])
            result.representation = Text.Representation.from_str(part[6])
            result.italic = Text.Italic.from_str(part[8])
            result.bold = Text.Bold.from_str(part[9])
            result.hjustify = Text.HJustify.from_str(part[10])
            result.vjustify = Text.VJustify.from_str(part[11])
            return result

        raise ValueError("Not enough parts for 'Text' element")

    if char == 'X':
        if len(part) == 12:
            visible = True
            if part[11][0] == 'N':
                visible = False
                part[11] = part[11][1:]
            shape = Pin.Shape.from_str(part[11])
        elif len(part) == 11:
            visible = True
            shape = Pin.Shape.line
        else:
            raise ValueError("Not enough parts for 'Pin' element")

        result = Pin(
            int(part[2]),                       # x
            int(part[3]),                       # y
            part[0],                            # name
            part[1]                             # number
        )
        result.length = int(part[4])
        result.direction = Pin.Direction.from_str(part[5])
        result.name_size = Symbol.PIN_NAME_SIZE if unify else int(part[6])
        result.number_size = Symbol.PIN_NUMBER_SIZE if unify else int(part[7])
        result.unit = int(part[8])
        result.representation = Pin.Representation.from_str(part[9])
        result.electric = Pin.Electric.from_str(part[10])
        result.visible = visible
        result.shape = shape
        return result

    raise KeyError
