import datetime

import kicad.schematic.type

class alias(object):
    '''2.3.1 Aliases'''
    pass

class field(object):
    '''2.3.2 Component field'''

    fmt = 'F{} "{}" {} {} {} {} {} {} {}{} "{}"'

    def __init__(self, type, text, x, y, dimension, orientation, visibility, hjustify, vjustify, style):
        if not isinstance(type, kicad.schematic.type.field):
            raise TypeError("type must be instance of kicad.schematic.type.field")

        if not isinstance(text, str):
            raise TypeError("text must be instance of str")

        if not isinstance(x, int) or not isinstance(y, int) or not isinstance(dimension, int):
            raise TypeError("x, y and dimension must be instance of int")

        if not isinstance(orientation, kicad.schematic.type.orientation):
            raise TypeError("orientation must be instance of kicad.schematic.type.orientation")

        if not isinstance(visibility, kicad.schematic.type.visibility):
            raise TypeError("visibility must be instance of kicad.schematic.type.visibility")

        if not isinstance(hjustify, kicad.schematic.type.hjustify):
            raise TypeError("hjustify must be instance of kicad.schematic.type.hjustify")

        if not isinstance(vjustify, kicad.schematic.type.vjustify):
            raise TypeError("vjustify must be instance of kicad.schematic.type.vjustify")

        if not isinstance(style, kicad.schematic.type.style):
            raise TypeError("style must be instance of kicad.schematic.type.style")

        self.type = type
        self.text = text
        self.x = x
        self.y = y
        self.dimension = dimension
        self.orientation = orientation
        self.visibility = visibility
        self.hjustify = hjustify
        self.vjustify = vjustify
        self.style = style

    def __str__(self):
        return field.fmt.format(
            self.type.value,
            self.text,
            self.x,
            self.y,
            self.dimension,
            self.orientation,
            self.visibility,
            self.hjustify,
            self.vjustify,
            self.style,
            self.type)

class element(object):
    '''Component element'''

    def __init__(self, unit, representation, order):
        if not isinstance(unit, int) or not isinstance(order, int):
            raise TypeError("unit and order must be instance of int")

        if not isinstance(representation, kicad.schematic.type.representation):
            raise TypeError("representation must be instance of kicad.schematic.type.representation")

        self.unit = unit
        self.representation = representation
        self.order = order

    @property
    def priority(self):
        return self.unit * 65536 + self.order * 256

class polygon(element):
    '''2.3.3.1 Polygon'''
    pass

class rectangle(element):
    '''2.3.3.2 Rectangle'''

    fmt = 'S {} {} {} {} {} {} {} {}'
    order = 1

    def __init__(self, x1, y1, x2, y2, width, fill, unit = 0, representation = kicad.schematic.type.representation.normal):
        element.__init__(self, unit, representation, rectangle.order)
        if not isinstance(x1, int) or not isinstance(y1, int) or not isinstance(x2, int) or not isinstance(y2, int) or not isinstance(width, int):
            raise TypeError("x1, y1, x2, y2 and width must be instance of int")

        if not isinstance(fill, kicad.schematic.type.fill):
            raise TypeError("fill must be instance of kicad.schematic.type.fill")

        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.width = width
        self.fill = fill

    def equal(self, rhs):
        '''Compare only same instances'''
        if not isinstance(rhs, rectangle):
            return False

        return self.x1 == rhs.x1 and self.y1 == rhs.y1 and self.x2 == rhs.x2 and self.y2 == rhs.y2

    def __str__(self):
        return rectangle.fmt.format(
            self.x1,
            self.y1,
            self.x2,
            self.y2,
            self.unit,
            self.representation,
            self.width,
            self.fill
        )

class circle(element):
    '''2.3.3.3 Circle'''
    pass

class arc(element):
    '''2.3.3.4 Arc'''
    pass

class text(element):
    '''2.3.3.5 Text'''
    pass

class fields(object):
    '''Component fields'''

    def __init__(self):
        self.fields = {}



class elements(object):
    '''Component elements'''

    def __init__(self):
        pass


class component(object):
    '''Schematic component'''

    def __init__(self):
        self.name = ''
        self.reference = ''
        self.text_offset = ''
        self.draw_pinnumber = True
        self.draw_pinname = True
        self.unit_count = 0
        self.units_locked = False
        self.option_flag = ''

        self.fields = fields()
        self.alias = []
        self.elements = []

    @property
    def fields(self):
        return self.fields

    def load(self, file):
        pass

    def save(self, file):
        pass

class schematic(object):
    '''Schematic class'''

    version_major = 2
    version_minor = 0

    def __init__(self):
        pass

    def __str__(self):
        print("EESchema-LIBRARY Version {}.{} {}".format(self.version_major, self.version_minor, datetime.datetime.today().strftime('%d/%m/%Y-%H:%M:%S')))
        print("description of the components")
        print("# End Library")
        pass

def from_str(string):
    '''Generate elements out of string lines. Used to load a symbol file'''
    
    string = string.strip()
    char = string[0]
    part = string[1:].split()
    if char == 'F':
        # NOTE: Optional name field is ignored!
        return field(
            kicad.schematic.type.field.from_str(int(part[0])),
            str(part[1]),
            int(part[2]),
            int(part[3]),
            int(part[4]),
            kicad.schematic.type.orientation.from_str(part[5]),
            kicad.schematic.type.visibility.from_str(part[6]),
            kicad.schematic.type.hjustify.from_str(part[7]),
            kicad.schematic.type.vjustify.from_str(part[8][:1]),
            kicad.schematic.type.style.from_str(part[8][1:])
        )
    else:
        raise KeyError
    return None
