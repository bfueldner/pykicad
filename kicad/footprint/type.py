from enum import Enum

import kicad.footprint.helper

class footprint(Enum):
    '''Footprint technology type'''

    thd = None
    smd = 'smd'
    virtual = 'virtual'

#    connector = 'TBD'
#    through_hole = 'thru_hole'
#    non_plated = 'TBD'

    def __str__(self):
        return self.value

class technology(Enum):
    '''Pad technology'''

    thru_hole = 'thru_hole'
    smd = 'smd'
    connect = 'connect'
    np_thru_hole = 'np_thru_hole'

    def __str__(self):
        return self.value

class shape(Enum):
    '''Pad shape'''

    circle = 'circle'
    oval = 'oval'
    rectangle = 'rect'
    trapezoid = 'trapezoid'
    round_rectangle = 'roundrec'

    def __str__(self):
        return self.value

class text(Enum):
    '''Text type'''

    reference = 'reference'
    value = 'value'
    user = 'user'

    def __str__(self):
        return self.value

class style(Enum):
    '''Text style'''

    normal = None
    italic = 'italic'

    def __str__(self):
        return self.value

class name(object):
    '''Name object'''

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return kicad.footprint.helper.quote_str(self.value)

class value(object):
    '''Value object'''

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return kicad.footprint.helper.float_to_str(self.value)

class point2d(object):
    '''Coordinate in 2d space'''

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '{} {}'.format(kicad.footprint.helper.float_to_str(self.x), kicad.footprint.helper.float_to_str(self.y))

class point3d(object):
    '''Coordinate in 3d space'''

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return '{} {} {}'.format(kicad.footprint.helper.float_to_str(self.x), kicad.footprint.helper.float_to_str(self.y), kicad.footprint.helper.float_to_str(self.z))

class area(object):
    '''Area in 2d space'''

    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def __str__(self):
        return '{} {} {} {}'.format(kicad.footprint.helper.float_to_str(self.x1), kicad.footprint.helper.float_to_str(self.y1), kicad.footprint.helper.float_to_str(self.x2), kicad.footprint.helper.float_to_str(self.y2))

class key_data(object):
    '''footprint (key value) representation'''

    def __init__(self, key, data):
        self.key = key
        self.data = data

    def __str__(self):
        if isinstance(self.data, list):
            res = ''
            for item in self.data:
                res += ' '+str(item)
            return '({}{})'.format(self.key, res)
        else:
            return '({} {})'.format(self.key, str(self.data))
