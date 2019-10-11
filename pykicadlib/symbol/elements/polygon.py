"""KiCAD symbol polygon element.

.. py::module:: pykicadlib.symbol.elements.polygon
   :synopsis: KiCAD symbol polygon elements

.. moduleauthor:: Benjamin Füldner <benjamin@fueldner.net>
"""

from pykicadlib.config import Symbol
from pykicadlib.symbol.element import Element


# Section 2.3.3.1 in fileformat.pdf
class Polygon(Element):
    """Polygon.

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

    from pykicadlib.symbol.elements.point import Point

    fmt = "P {:d} {:d} {:d} {:d} {:s}{:s}"
    order = 2

    def __init__(self):
        """Constructor."""
        super().__init__(order=Polygon.order)

        self.thickness = Symbol.ELEMENT_THICKNESS   #: Thickness of outline
        self.fill = Polygon.Fill.none               #: Fill type
        self.points = []                            #: Outline points

    @property
    def priority(self):
        """Element priority.

        :type:
            int
        """
        return super().priority + len(self.points)

    @property
    def bounds(self):
        """Element boundary.

        :type:
            Boundary
        """
        result = Element.Boundary(0, 0, 0, 0)
        for point in self.points:
            result.x1 = min(point.x, result.x1)
            result.y1 = min(point.y, result.y1)
            result.x2 = max(point.x, result.x2)
            result.y2 = max(point.y, result.y2)
        return result

    def add(self, point):
        """Add point to polygon.

        :param Point point:
            Point to add
        """
        self.points.append(point)

    def remove(self, index):
        """Remove element from polygon.

        :param int index:
            Index of point to remove
        """
        del self.points[index]

    def __eq__(self, other):
        """Compare :class:`Polygon` instances."""
        if not isinstance(other, Polygon):
            raise TypeError

        if len(self.points) != len(other.points):
            return False

        for point1, point2 in zip(self.points, other.points):
            if point1 != point2:
                return False
        return True

    def __str__(self):
        """Return :class:`Polygon` in KiCAD format."""
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
