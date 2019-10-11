"""KiCAD symbol text element.

.. py::module:: pykicadlib.symbol.elements.text
   :synopsis: KiCAD symbol text elements

.. moduleauthor:: Benjamin Füldner <benjamin@fueldner.net>
"""

from pykicadlib.symbol.element import Element


# Section 2.3.3.5 in fileformat.pdf
# pylint: disable=too-many-instance-attributes
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

    from pykicadlib.symbol.types import Bold, Italic, HJustify, VJustify

    fmt = 'T {:.0f} {:d} {:d} {:d} 0 {:d} {:d} "{:s}" {:s} {:d} {:s} {:s}'
    order = 0

    def __init__(self, x, y, value, size):
        """Constructor."""
        super().__init__(order=Text.order)

        self.x = x                              #: X coordinate
        self.y = y                              #: Y coordinate
        self.value = value                      #: Text value
        self.size = size                        #: Text size
        self.angle = 0.0                        #: Text angle
        self.italic = Text.Italic.off           #: Text italic style
        self.bold = Text.Bold.off               #: Text bold style
        self.hjustify = Text.HJustify.center    #: Horizontal text justify
        self.vjustify = Text.VJustify.center    #: Vertical text justify

    @property
    def bounds(self):
        """Element boundary.

        :type:
            Boundary
        """
        # NOTE: Ignore for the moment!
        return Element.Boundary(self.x, self.y, self.x, self.y)

    def __eq__(self, other):
        """Compare :class:`Text` instances."""
        if not isinstance(other, Text):
            raise TypeError

        return self.x == other.x and self.y == other.y and self.value == other.value

    def __str__(self):
        """Return :class:`Text` in KiCAD format."""
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
