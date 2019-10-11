"""KiCAD symbol circle element.

.. py::module:: pykicadlib.symbol.elements.circle
   :synopsis: KiCAD symbol circle elements

.. moduleauthor:: Benjamin Füldner <benjamin@fueldner.net>
"""

from pykicadlib.config import Symbol
from pykicadlib.symbol.element import Element


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

    def __init__(self, x, y, radius):
        """Constructor."""
        super().__init__(order=Circle.order)

        self.x = x                                  #: X coordinate
        self.y = y                                  #: Y coordinate
        self.radius = radius                        #: Circle radius
        self.thickness = Symbol.ELEMENT_THICKNESS   #: Thickness of outline
        self.fill = Circle.Fill.none                #: Fill type

    @property
    def bounds(self):
        """Element boundary.

        :type:
            Boundary
        """
        return Element.Boundary(
            self.x - self.radius, self.y - self.radius, self.x + self.radius, self.y + self.radius)

    def __eq__(self, other):
        """Compare :class:`Circle` instances."""
        if not isinstance(other, Circle):
            raise TypeError

        return self.x == other.x and self.y == other.y and self.radius == other.radius

    def __str__(self):
        """Return :class:`Circle` in KiCAD format."""
        return Circle.fmt.format(
            self.x,
            self.y,
            self.radius,
            self.unit,
            self.representation.value,
            self.thickness,
            self.fill
        )
