#import decimal

import kicad.pcb.layer

#helper:
#point(name x y)
#layer(layer name.name)
#dimension(name value)
#
#set of valid layers: index name.name signal/user

def quote(text):
    '''Quote string'''

    if all(ord(char) > 127 for char in text):
        raise ValueError('Only ASCII 7bit allowed!')
    return "\"{}\"".format(text.replace('"', '""'))

#ctx = decimal.Context()
#ctx.prec = 20

def float_str(f):
    '''
    Convert the given float to a string, without resorting to scientific notation
    @ref https://stackoverflow.com/questions/38847690/convert-float-to-string-without-scientific-notation-and-false-precision
    '''
#    return format(ctx.create_decimal(repr(f)), 'f')
    return repr(f)

class key_value(object):
    '''PCB (key value) representation'''

    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return '({} {})'.format(self.key, str(self.value))


class dimension(object):
    '''Represent a name with one value'''

    def __init__(self, value):
        if not isinstance(value, float):
            raise TypeError("value must be instance of float")

        self.value = value

    def __str__(self):
        return float_str(self.value)

class point2d(object):
    '''Represent a coordinate in 2d space'''

    def __init__(self, x, y):
        if not isinstance(x, float) or not isinstance(y, float):
            raise TypeError("x and y must be instance of float")

        self.x = x
        self.y = y

    def __str__(self):
        return float_str(self.x)+' '+float_str(self.y)

class point3d(object):
    '''Represent a coordinate in 3d space'''

    def __init__(self, x, y, z):
        if not isinstance(x, float) or not isinstance(y, float) or not isinstance(z, float):
            raise TypeError("x, y and z must be instance of float")

        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return float_str(self.x)+' '+float_str(self.y)+' '+float_str(self.z)

class area(object):
    '''Represent a area in 2d space'''

    def __init__(self, x1, y1, x2, y2):
        if not isinstance(x1, float) or not isinstance(y1, float) or not isinstance(x2, float) or not isinstance(y2, float):
            raise TypeError("x1, y1, x2 and y2 must be instance of float")

        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def __str__(self):
        return float_str(self.x1)+' '+float_str(self.y1)+' '+float_str(self.x2)+' '+float_str(self.y2)
