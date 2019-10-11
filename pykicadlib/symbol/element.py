"""KiCAD symbol element.

.. py::module:: pykicadlib.symbol.element
   :synopsis: KiCAD symbol element
   :noindex:

.. moduleauthor:: Benjamin Füldner <benjamin@fueldner.net>
"""


class Element():
    """Element base class.

    :param int unit:
        Unit number
    :param Representation representation:
        Element representation
    :param int order:
        Order number
    """

    from pykicadlib.symbol.boundary import Boundary
    from pykicadlib.symbol.types import Fill, Representation

    def __init__(self, unit=0, representation=Representation.normal, order=0):
        """Constructor."""
        self.unit = unit                        #: Unit
        self.representation = representation    #: Representation
        self.order = order                      #: Sort order

        self.id = None                          #: ID
        self.count = 0                          #: Count

    @property
    def priority(self):
        """Element priority.

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
        return Element.Boundary(0, 0, 0, 0)
