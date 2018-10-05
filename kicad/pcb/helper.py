
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

class dimension(object):
    '''Represent a name with one value'''

    def __init__(self, key, value):
        if not isinstance(key, str):
            raise TypeError("key must be instance of str")

        if not isinstance(value, float):
            raise TypeError("value must be instance of float")
        self.key = key
        self.value = value

    def render(self):
        return '({} {:f})'.format(self.key, self.value)

class point(object):
    '''Represent a name with one coordinates'''

    def __init__(self, key, x, y):
        if not isinstance(key, str):
            raise TypeError("key must be instance of str")

        if not isinstance(x, float) or not isinstance(y, float):
            raise TypeError("x and y must be instance of float")
        self.key = key
        self.x = x
        self.y = y

    def render(self):
        return '({} {:f} {:f})'.format(self.key, self.x, self.y)

class area(object):
    '''Represent a name with two coordinates'''

    def __init__(self, key, x1, y1, x2, y2):
        if not isinstance(key, str):
            raise TypeError("key must be instance of str")

        if not isinstance(x1, float) or not isinstance(y1, float) or not isinstance(x2, float) or not isinstance(y2, float):
            raise TypeError("x1, y1, x2 and y2 must be instance of float")
        self.key = key
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def render(self):
        return '({} {:f} {:f} {:f} {:f})'.format(self.key, self.x1, self.y1, self.x2, self.y2)
