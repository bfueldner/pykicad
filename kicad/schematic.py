import datetime

import kicad.type

class field(object):
    '''Component field'''

    fmt = 'F{} "{}" {} {} {} {} {} {} {}{} "{}"'

    def __init__(self, type, text, x, y, dimension, orientation, visibility, hjustify, vjustify, style):
        if not isinstance(type, kicad.type.field):
            raise TypeError("type must be instance of kicad.type.field")

        if not isinstance(text, str):
            raise TypeError("text must be instance of str")

        if not isinstance(x, int) or not isinstance(y, int) or not isinstance(dimension, int):
            raise TypeError("x, y and dimension must be instance of int")

        if not isinstance(orientation, kicad.type.orientation):
            raise TypeError("orientation must be instance of kicad.type.orientation")

        if not isinstance(visibility, kicad.type.visibility):
            raise TypeError("visibility must be instance of kicad.type.visibility")

        if not isinstance(hjustify, kicad.type.hjustify):
            raise TypeError("hjustify must be instance of kicad.type.hjustify")

        if not isinstance(vjustify, kicad.type.vjustify):
            raise TypeError("vjustify must be instance of kicad.type.vjustify")

        if not isinstance(style, kicad.type.style):
            raise TypeError("style must be instance of kicad.type.style")

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

    def render(self):
        return self.fmt.format(
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

    def __init__(self):
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

    def render(self):
        print("EESchema-LIBRARY Version {}.{} {}".format(self.version_major, self.version_minor, datetime.datetime.today().strftime('%d/%m/%Y-%H:%M:%S')))
        print("description of the components")
        print("# End Library")
        pass

def from_str(string):
    string = string.strip()
    char = string[0]
    part = string[1:].split()
    if char == 'F':
        return field(
            kicad.type.field.from_str(int(part[0])),
            str(part[1]),
            int(part[2]),
            int(part[3]),
            int(part[4]),
            kicad.type.orientation.from_str(part[5]),
            kicad.type.visibility.from_str(part[6]),
            kicad.type.hjustify.from_str(part[7]),
            kicad.type.vjustify.from_str(part[8][:1]),
            kicad.type.style.from_str(part[8][1:])
        )
    else:
        raise KeyError
    return None
