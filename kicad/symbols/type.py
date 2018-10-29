from enum import Enum

class field(Enum):
    '''Schematic field type'''

    reference = 0
    name = 1
    footprint = 2
    document = 3
    manufacturer = 4
    value = 5
    tolerance = 6
    temperature = 7
    model = 8
    voltage = 9
    power = 10

    def __str__(self):
        return self.name.title()

    @staticmethod
    def from_str(value):
        int_value = int(value)
        for item in field:
            if item.value == int_value:
                return item
        raise NotImplementedError("'{}' is no element of 'field'".format(value))

class orientation(Enum):
    '''Field orientation'''

    horizontal = 'H'
    vertical = 'V'

    def __str__(self):
        return self.value

    @staticmethod
    def from_str(value):
        for item in orientation:
            if item.value == value:
                return item
        raise NotImplementedError("'{}' is no element of 'orientation'".format(value))

class visibility(Enum):
    '''Field visibility'''

    visible = 'V'
    invisible = 'I'

    def __str__(self):
        return self.value

    @staticmethod
    def from_str(value):
        for item in visibility:
            if item.value == value:
                return item
        raise NotImplementedError("'{}' is no element of 'visibility'".format(value))

class hjustify(Enum):
    '''Field horizontal justify'''

    left = 'L'
    center = 'C'
    right = 'R'

    def __str__(self):
        return self.value

    @staticmethod
    def from_str(value):
        for item in hjustify:
            if item.value == value:
                return item
        raise NotImplementedError("'{}' is no element of 'hjustify'".format(value))

class vjustify(Enum):
    '''Field vertical justify'''

    top = 'T'
    center = 'C'
    bottom = 'B'

    def __str__(self):
        return self.value

    @staticmethod
    def from_str(value):
        for item in vjustify:
            if item.value == value:
                return item
        raise NotImplementedError("'{}' is no element of 'vjustify'".format(value))

class style(Enum):
    '''Field style'''

    none = 'NN'
    italic = 'IN'
    bold = 'NB'
    italic_bold = 'IB'

    def __str__(self):
        return self.value

    @staticmethod
    def from_str(value):
        for item in style:
            if item.value == value:
                return item
        raise NotImplementedError("'{}' is no element of 'style'".format(value))

class fill(Enum):
    '''Element fill'''

    none = 'N'
    foreground = 'F'
    background = 'f'

    def __str__(self):
        return self.value

    @staticmethod
    def from_str(value):
        for item in fill:
            if item.value == value:
                return item
        raise NotImplementedError("'{}' is no element of 'fill'".format(value))

class representation(Enum):
    '''Symbol representation'''

    both = 0
    normal = 1
    morgan = 2

    def __str__(self):
        return str(self.value)

    @staticmethod
    def from_str(value):
        int_value = int(value)
        for item in representation:
            if item.value == int_value:
                return item
        raise NotImplementedError("'{}' is no element of 'representation'".format(value))

class italic(Enum):
    '''Text element italic'''

    off = 'Normal'
    on = 'Italic'

    def __str__(self):
        return self.value

    @staticmethod
    def from_str(value):
        for item in italic:
            if item.value == value:
                return item
        raise NotImplementedError("'{}' is no element of 'italic'".format(value))

class bold(Enum):
    '''Text element bold'''

    off = 0
    on = 1

    def __str__(self):
        return str(self.value)

    @staticmethod
    def from_str(value):
        int_value = int(value)
        for item in bold:
            if item.value == int_value:
                return item
        raise NotImplementedError("'{}' is no element of 'bold'".format(value))

class direction(Enum):
    '''2.3.4 Pin direction (flipped in opposition to KiCAD documentation)'''

    up = 'D'
    down = 'U'
    right = 'L'
    left = 'R'

    def __str__(self):
        return self.value

    @staticmethod
    def from_str(value):
        for item in direction:
            if item.value == value:
                return item
        raise NotImplementedError("'{}' is no element of 'direction'".format(value))

class electric(Enum):
    '''2.3.4 Electric pin type'''

    input = 'I'
    output = 'O'
    bidirectional = 'B'
    tristate = 'T'
    passive = 'P'
    unspecified = 'U'
    power_input = 'W'
    power_output = 'w'
    open_collector = 'C'
    open_emitter = 'E'
    not_connected = 'N'

    def __str__(self):
        return self.value

    @staticmethod
    def from_str(value):
        for item in electric:
            if item.value == value:
                return item
        raise NotImplementedError("'{}' is no element of 'electric'".format(value))

# Add 'N' before characters, to create an invisible pin
class shape(Enum):
    '''2.3.4 Pin shape'''

    line = ''
    invisible = 'N'
    inverted = 'I'
    clock = 'C'
    inverted_clock = 'CI'
    input_low = 'L'
    clock_low = 'CL'
    output_low = 'V'
    falling_edge_clock = 'F'
    non_logic = 'X'

    def __str__(self):
        return self.value

    @staticmethod
    def from_str(value):
        for item in shape:
            if item.value == value:
                return item
        raise NotImplementedError("'{}' is no element of 'shape'".format(value))
