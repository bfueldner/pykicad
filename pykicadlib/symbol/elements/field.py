"""KiCAD symbol field element.

.. py::module:: pykicadlib.symbol.elements.field
   :synopsis: KiCAD symbol field elements

.. moduleauthor:: Benjamin Füldner <benjamin@fueldner.net>
"""

from pykicadlib.config import Symbol


# Section 2.3.2 in fileformat.pdf
# pylint: disable=too-many-instance-attributes, too-few-public-methods
class Field():
    """Component field.

    :param types.Field type_:
        Type of :class:`Field`
    :param str value:
        Value of :class:`Field` text
    :param int x:
        X coordinate
    :param int y:
        Y coordinate
    :param int size:
        Text size
    :param Orientation orientation:
        Text orientation
    :param Visibility visibility:
        Text visibility
    :param HJustify hjustify:
        Horizontal text justify
    :param VJustify vjustify:
        Vertical text justify
    :param Style style:
        Text style

    .. automethod:: __str__
    """
    from pykicadlib.symbol.types import Orientation, Visibility, HJustify, VJustify, Style
    from pykicadlib.symbol.types import Field as Type

    fmt = 'F{:d} "{:s}" {:d} {:d} {:d} {:s} {:s} {:s} {:s}{:s} "{:s}"'

    def __init__(
            self,
            type_,
            x, y,
            value):
        """Constructor."""
        self.type = type_                                   #: Type of :class:`Field`
        self.x = x                                          #: X coordinate
        self.y = y                                          #: Y coordinate
        self.value = value                                  #: Value of :class:`Field` text
        self.size = Symbol.FIELD_TEXT_SIZE                  #: Text size
        self.orientation = Field.Orientation.horizontal     #: Text orientation
        self.visibility = Field.Visibility.visible          #: Text visibility
        self.hjustify = Field.HJustify.left                 #: Horizontal text justify
        self.vjustify = Field.VJustify.center               #: Vertical text justify
        self.style = Field.Style.none                       #: Text style

    def __str__(self):
        """Return :class:`Field` in KiCAD format."""
        return Field.fmt.format(
            self.type.value,
            self.value,
            self.x,
            self.y,
            self.size,
            self.orientation,
            self.visibility,
            self.hjustify,
            self.vjustify,
            self.style,
            self.type
        )
