import re

import kicad.type

def quote_text(text):
    if all(ord(char) > 127 for char in text):
        raise ValueError('Only ASCII 7bit allowed!')
    return "\"{}\"".format(text.replace('"', '""'))

class layer(object):
    '''4.5 Layer'''

    def __init__(self, layer_position, layer_type):
        pass


    def render(self):
        return ""

class layers(object):
    '''4.5 Layers'''
    pass

#copper_front = [copper_layer.front, layer.copper]
#
#helper:
#point(name x y)
#layer(layer name.name)
#dimension(name value)
#
#set of valid layers: index name.name signal/user
