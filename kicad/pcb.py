import re

import kicad.type

class layer(object):
    '''4.5 Layer'''

    def __init__(self, layer_position, layer_type):
        pass


    def render(self):
        return ""

class layers(object):
    '''4.5 Layers'''
    pass

#helper:
#point(name x y)
#layer(layer name.name)
#dimension(name value)
#
#set of valid layers: index name.name signal/user
