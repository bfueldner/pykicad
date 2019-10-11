"""KiCAD symbol pin element.

.. py::module:: pykicadlib.symbol.elements.pin
   :synopsis: KiCAD symbol pin elements

.. moduleauthor:: Benjamin Füldner <benjamin@fueldner.net>
"""

from re import match
from pykicadlib.config import Symbol
from pykicadlib.symbol.element import Element


def _pin_value(value):
    """Convert pin number into value (especially for BGA numbering scheme)."""
    res = match(r'[~0-9A-Z]+', value)
    if res:
        sum_ = 0
        for chr_ in res.group(0):
            sum_ = sum_ * 128 + ord(chr_)
        return sum_
    raise ValueError("'{}' is no valid pin value".format(value))


# Section 2.3.4 in fileformat.pdf
# pylint: disable=too-many-instance-attributes
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

    from pykicadlib.symbol.types import Direction, Electric, Shape

    fmt = 'X {:s} {:s} {:d} {:d} {:d} {:s} {:d} {:d} {:d} {:d} {:s} {:s}{:s}'
    order = 10

    def __init__(self, x, y, name, number):
        """Constructor."""
        super().__init__(order=Pin.order)

        self.x = x                                  #: X coordinate
        self.y = y                                  #: Y coordinate
        self.name = name                            #: Pin name
        self.number = number                        #: Pin number
        self.length = Symbol.PIN_LENGTH             #: Pin length
        self.direction = Pin.Direction.down         #: Pin direction
        self.name_size = Symbol.PIN_NAME_SIZE       #: Pin name size
        self.number_size = Symbol.PIN_NUMBER_SIZE   #: Pin number size
        self.electric = Pin.Electric.input          #: Electric type
        self.shape = Pin.Shape.line                 #: Shape type
        self.visible = True                         #: Visibility

    @property
    def priority(self):
        """Element priority.

        :type:
            int
        """
        return super().priority + _pin_value(self.number)

    @property
    def bounds(self):
        """Element boundary.

        :type:
            Boundary
        """
        result = Element.Boundary(self.x, self.y, self.x, self.y)
        if self.direction == Pin.Direction.left:
            result.x1 -= self.length
        elif self.direction == Pin.Direction.right:
            result.x2 += self.length
        elif self.direction == Pin.Direction.up:
            result.y1 -= self.length
        elif self.direction == Pin.Direction.down:
            result.y2 += self.length
        return result

    def __eq__(self, other):
        """Compare :class:`Pin` instances."""
        if not isinstance(other, Pin):
            raise TypeError

    #   return self.x == other.x and self.y == other.y and \
    #       self.length == other.length and self.name == other.name and self.number == other.number
        return False

    def __str__(self):
        """Return :class:`Pin` in KiCAD format."""
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
