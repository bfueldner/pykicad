"""
.. py::module:: pykicadlib.symbol.types
   :synopsis: KiCAD symbol types
   :noindex:

.. moduleauthor:: Benjamin Füldner <benjamin@fueldner.net>
"""

from enum import Enum


class SymbolEnum(Enum):
    """Symbol enumeration base class

    .. automethod:: __str__
    .. automethod:: from_str
    .. autodoc-skip-member::
    """

    def __str__(self):
        """Return KiCAD value of :class:`SymbolEnum`"""

        return self.value

    @classmethod
    def from_str(cls, value):
        """Convert string to enum element.

        :param str value:
            String with value to convert.
        :returns:
            Enum class object.
        :raises:
            NotImplementedError
        """

        for item in cls:
            if item.value == value:
                return item
        raise NotImplementedError("'{}' is no element of '{}'".format(value, cls.__name__))


class Visible(SymbolEnum):
    """Symbol pin name/number visible"""

    no = 'N'            #: Not visible
    yes = 'Y'           #: Visible


class Units(SymbolEnum):
    """Symbol units swappable or locked"""

    locked = 'L'        #: Locked
    swappable = 'F'     #: Swappable


class Flag(SymbolEnum):
    """Flag normal or power symbol"""

    normal = 'N'        #: Normal symbol
    power = 'P'         #: Power symbol


class Field(Enum):
    """Symbol field type"""

    reference = 0       #: Reference field
    name = 1            #: Name field
    footprint = 2       #: Footprint field
    document = 3        #: Document field
    manufacturer = 4    #: Manufacturer field
    value = 5           #: Value field
    tolerance = 6       #: Tolerance field
    temperature = 7     #: Temperature range field
    model = 8           #: Model field
    voltage = 9         #: Voltage field
    power = 10          #: Power field

    def __str__(self):
        """Return KiCAD value of :class:`Field`"""

        return str(self.name).title()

    @classmethod
    def from_str(cls, value):
        """Convert string to enum element.

        :param str value:
            String with value to convert.
        :returns:
            Enum class object.
        :raises:
            NotImplementedError
        """

        int_value = int(value)
        for item in cls:
            if item.value == int_value:
                return item
        raise NotImplementedError("'{}' is no element of '{}'".format(value, cls.__name__))


class Orientation(SymbolEnum):
    """Field orientation"""

    horizontal = 'H'    #: Horizontal orientation
    vertical = 'V'      #: Vertical orientation


class Visibility(SymbolEnum):
    """Field visibility"""

    visible = 'V'       #: Visible
    invisible = 'I'     #: Invisible


class HJustify(SymbolEnum):
    """Field horizontal justify"""

    left = 'L'          #: Left
    center = 'C'        #: Center
    right = 'R'         #: Right


class VJustify(SymbolEnum):
    """Field vertical justify"""

    top = 'T'           #: Top
    center = 'C'        #: Center
    bottom = 'B'        #: Bottom


class Style(SymbolEnum):
    """Field style"""

    none = 'NN'         #: None
    italic = 'IN'       #: Italic
    bold = 'NB'         #: Bold
    italic_bold = 'IB'  #: Italic and Bold


class Fill(SymbolEnum):
    """Element fill"""

    none = 'N'          #: None
    foreground = 'F'    #: Foreground
    background = 'f'    #: Background


class Representation(Enum):
    """Symbol representation"""

    both = 0            #: Both
    normal = 1          #: Normal
    morgan = 2          #: Morgan

    def __str__(self):
        """Return KiCAD value of :class:`Representation`"""

        return str(self.value)

    @classmethod
    def from_str(cls, value):
        """Convert string to enum element.

        :param str value:
            String with value to convert.
        :returns:
            Enum class object.
        :raises:
            NotImplementedError
        """

        int_value = int(value)
        for item in cls:
            if item.value == int_value:
                return item
        raise NotImplementedError("'{}' is no element of '{}'".format(value, cls.__name__))


class Italic(SymbolEnum):
    """Text element italic"""

    off = 'Normal'      #: Normal
    on = 'Italic'       #: Italic


class Bold(Enum):
    """Text element bold"""

    off = 0             #: Normal
    on = 1              #: Bold

    def __str__(self):
        """Return KiCAD value of :class:`Bold`"""
        return str(self.value)

    @classmethod
    def from_str(cls, value):
        """Convert string to enum element.

        :param str value:
            String with value to convert.
        :returns:
            Enum class object.
        :raises:
            NotImplementedError
        """

        int_value = int(value)
        for item in cls:
            if item.value == int_value:
                return item
        raise NotImplementedError("'{}' is no element of '{}'".format(value, cls.__name__))


class Direction(SymbolEnum):
    """2.3.4 Pin direction (flipped in opposition to KiCAD documentation)"""

    up = 'D'            #: Up
    down = 'U'          #: Down
    right = 'L'         #: Right
    left = 'R'          #: Left

    @classmethod
    def from_name(cls, name):
        """Convert name to enum element.

        :param str name:
            String with name to convert.
        :returns:
            Enum class object.
        :raises:
            NotImplementedError
        """

        for item in cls:
            if item.name == name:
                return item
        raise NotImplementedError("'{}' is no name of '{}'".format(name, cls.__name__))


class Electric(SymbolEnum):
    '''2.3.4 Electric pin type'''

    input = 'I'             #: Input
    output = 'O'            #: Output
    bidirectional = 'B'     #: Bidirectional
    tristate = 'T'          #: Tristate
    passive = 'P'           #: Passive
    unspecified = 'U'       #: Unspecified
    power_input = 'W'       #: Power input
    power_output = 'w'      #: Power output
    open_collector = 'C'    #: Open collector
    open_emitter = 'E'      #: Open emitter
    not_connected = 'N'     #: Not connected

    @classmethod
    def from_name(cls, name):
        """Convert name to enum element.

        :param str name:
            String with name to convert.
        :returns:
            Enum class object.
        :raises:
            NotImplementedError
        """

        for item in cls:
            if item.name == name:
                return item
        raise NotImplementedError("'{}' is no name of '{}'".format(name, cls.__name__))


# Add 'N' before characters, to create an invisible pin
class Shape(SymbolEnum):
    '''2.3.4 Pin shape'''

    line = ''                   #: Line
    invisible = 'N'             #: Invisible
    inverted = 'I'              #: Inverted
    clock = 'C'                 #: Clock
    inverted_clock = 'CI'       #: Inverted clock
    input_low = 'L'             #: Input low
    clock_low = 'CL'            #: Clock low
    output_low = 'V'            #: Output low
    falling_edge_clock = 'F'    #: Falling-edge clock
    non_logic = 'X'             #: Non logic

    @classmethod
    def from_name(cls, name):
        """Convert name to enum element.

        :param str name:
            String with name to convert.
        :returns:
            Enum class object.
        :raises:
            NotImplementedError
        """

        for item in cls:
            if item.name == name:
                return item
        raise NotImplementedError("'{}' is no name of '{}'".format(name, cls.__name__))
