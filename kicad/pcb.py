import re

import kicad.type

class line(object):
    '''PCB line'''

    def __init__(self, layer, x1, y1, x2, y2, width):
        self.start = kicad.pcb.helper.key_value('start', kicad.pcb.helper.point2d(x1, y1))
        self.end = kicad.pcb.helper.key_value('end', kicad.pcb.helper.point2d(x2, y2))
        self.layer = kicad.pcb.helper.key_value('layer', layer)
        self.width = kicad.pcb.helper.key_value('width', width)

    def __str__(self):
        list = ['fp_line', str(self.start), str(self.end), str(self.layer), str(self.width)]
        return '(' + ' '.join(list) +')'



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
