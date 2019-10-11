"""KiCAD symbol element point.

.. py::module:: pykicadlib.symbol.elements.point
   :synopsis: KiCAD symbol element point
   :noindex:

.. moduleauthor:: Benjamin Füldner <benjamin@fueldner.net>
"""


class Point():
    """Point helper.

    :param int x:
        X coordinate
    :param int y:
        Y coordinate

    .. automethod:: __eq__
    .. automethod:: __str__
    """

    fmt = "{:d} {:d}"

    def __init__(self, x, y):
        """Constructor."""
        self.x = x  #: X coordinate
        self.y = y  #: Y coordinate

    def __eq__(self, other):
        """Compare :class:`Point` instances.

        :returns:
            ``True``, if ``other`` == :class:`Point` and all attributes match. Otherwise ``False``.
        """
        if not isinstance(other, Point):
            raise TypeError

        return self.x == other.x and self.y == other.y

    def __str__(self):
        """Return :class:`Point` in KiCAD format."""
        return Point.fmt.format(
            self.x,
            self.y,
        )
