"""KiCAD symbol arc element.

.. py::module:: pykicadlib.symbol.elements.arc
   :synopsis: KiCAD symbol arc elements

.. moduleauthor:: Benjamin Füldner <benjamin@fueldner.net>
"""

from pykicadlib.config import Symbol
from pykicadlib.symbol.element import Element


# Section 2.3.3.4 in fileformat.pdf
# pylint: disable=too-many-instance-attributes
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
            radius,
            start_x, start_y,
            end_x, end_y,
            start_angle, end_angle):
        """Constructor."""
        super().__init__(order=Arc.order)

        self.x = x                                  #: X coordinate
        self.y = y                                  #: Y coordinate
        self.radius = radius                        #: Arc radius
        self.start_x = start_x                      #: Start X coordinate
        self.start_y = start_y                      #: Start Y coordinate
        self.end_x = end_x                          #: End X coordinate
        self.end_y = end_y                          #: End Y coordinate
        self.start_angle = start_angle              #: Start angle
        self.end_angle = end_angle                  #: End angle
        self.thickness = Symbol.ELEMENT_THICKNESS   #: Thickness of outline
        self.fill = Arc.Fill.none                   #: Fill type

    @property
    def bounds(self):
        """Element boundary.

        :type:
            Boundary
        """
        # Not exact!
        return Element.Boundary(
            self.x - self.radius,
            self.y - self.radius,
            self.x + self.radius,
            self.y + self.radius)

    def __eq__(self, other):
        """Compare :class:`Arc` instances."""
        if not isinstance(other, Arc):
            raise TypeError

        return self.x == other.x and self.y == other.y and \
            self.start_x == other.start_x and self.start_y == other.start_y and \
            self.end_x == other.end_x and self.end_y == other.end_y and \
            self.start_angle == other.start_angle and self.end_angle == other.end_angle and \
            self.radius == other.radius

    def __str__(self):
        """Return :class:`Arc` in KiCAD format."""
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
