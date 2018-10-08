from enum import Enum

import kicad.pcb.helper

class technology(Enum):
    '''Footprint technology type'''

    smd = 'smd'
    connector = 'TBD'
    through_hole = 'thru_hole'
    non_plated = 'TBD'

    def __str__(self):
        return self.value

class text(object):
    '''Text object'''

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return kicad.pcb.helper.quote_str(self.value)

class value(object):
    '''Value object'''

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return kicad.pcb.helper.float_to_str(self.value)

class point2d(object):
    '''Coordinate in 2d space'''

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '{} {}'.format(kicad.pcb.helper.float_to_str(self.x), kicad.pcb.helper.float_to_str(self.y))

class point3d(object):
    '''Coordinate in 3d space'''

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return '{} {} {}'.format(kicad.pcb.helper.float_to_str(self.x), kicad.pcb.helper.float_to_str(self.y), kicad.pcb.helper.float_to_str(self.z))

class area(object):
    '''Area in 2d space'''

    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def __str__(self):
        return '{} {} {} {}'.format(kicad.pcb.helper.float_to_str(self.x1), kicad.pcb.helper.float_to_str(self.y1), kicad.pcb.helper.float_to_str(self.x2), kicad.pcb.helper.float_to_str(self.y2))

class key_data(object):
    '''PCB (key value) representation'''

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
