"""KiCAD symbol rectangle element.

.. py::module:: pykicadlib.symbol.elements.rectangle
   :synopsis: KiCAD symbol rectangle elements

.. moduleauthor:: Benjamin Füldner <benjamin@fueldner.net>
"""

from pykicadlib.config import Symbol
from pykicadlib.symbol.element import Element


# Section 2.3.3.2 in fileformat.pdf
# pylint: disable=too-many-instance-attributes
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

    def __init__(self, x1, y1, x2, y2):
        """Constructor."""
        super().__init__(order=Rectangle.order)

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

        self.thickness = Symbol.ELEMENT_THICKNESS   #: Thickness of outline
        self.fill = Rectangle.Fill.none             #: Fill type

    @property
    def bounds(self):
        """Element boundary.

        :type:
            Boundary
        """
        return Element.Boundary(self.x1, self.y1, self.x2, self.y2)

    def __eq__(self, other):
        """Compare :class:`Rectangle` instances."""
        if not isinstance(other, Rectangle):
            raise TypeError

        return self.x1 == other.x1 and self.y1 == other.y1 and \
            self.x2 == other.x2 and self.y2 == other.y2

    def __str__(self):
        """Return :class:`Rectangle` in KiCAD format."""
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
