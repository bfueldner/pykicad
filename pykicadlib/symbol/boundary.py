"""KiCAD symbol boundary.

.. py::module:: pykicadlib.symbol.boundary
   :synopsis: KiCAD symbol boundary
   :noindex:

.. moduleauthor:: Benjamin Füldner <benjamin@fueldner.net>
"""


class Boundary():
    """Element/symbol boundary class.

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
        """Constructor."""
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
        if not isinstance(other, Boundary):
            raise TypeError

        return Boundary(
            min(self.x1, other.x1),
            min(self.y1, other.y1),
            max(self.x2, other.x2),
            max(self.y2, other.y2),
        )

    def __eq__(self, other):
        """Compare :class:`Boundary` instances."""
        if not isinstance(other, Boundary):
            raise TypeError

        return self.x1 == other.x1 and self.y1 == other.y1 and \
            self.x2 == other.x2 and self.y2 == other.y2
