import kicad.pcb.helper

class arc(object):
    '''PCB arc'''

    def __init__(self, layer, x, y, x2, y2, width):
        self.center = kicad.pcb.helper.key_value('center', kicad.pcb.helper.point2d(x1, y1))
        self.end = kicad.pcb.helper.key_value('end', kicad.pcb.helper.point2d(x2, y2))
        self.layer = kicad.pcb.helper.key_value('layer', layer)
        self.width = kicad.pcb.helper.key_value('width', width)

    def __str__(self):
        list = [str(self.start), str(self.end), str(self.layer), str(self.width)]
        return '(fp_arc' + ' '.join(list) +')'

class line(object):
    '''PCB line'''

    def __init__(self, layer, x1, y1, x2, y2, width):
        self.start = kicad.pcb.helper.key_value('start', kicad.pcb.helper.point2d(x1, y1))
        self.end = kicad.pcb.helper.key_value('end', kicad.pcb.helper.point2d(x2, y2))
        self.layer = kicad.pcb.helper.key_value('layer', layer)
        self.width = kicad.pcb.helper.key_value('width', width)
        print('__init__', width)

    def __str__(self):
        list = [str(self.start), str(self.end), str(self.layer), str(self.width)]
        return '(fp_line ' + ' '.join(list) +')'
