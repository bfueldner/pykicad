import kicad.pcb.type

class arc(object):
    '''Arc between x1/y1 and x2/y2 with given angle'''

    def __init__(self, layer, x1, y1, x2, y2, angle, width):
        self.start = kicad.pcb.type.key_data('start', kicad.pcb.type.point2d(x1, y1))
        self.end = kicad.pcb.type.key_data('end', kicad.pcb.type.point2d(x2, y2))
        self.angle = kicad.pcb.type.key_data('angle', angle)
        self.layer = kicad.pcb.type.key_data('layer', layer)
        self.width = kicad.pcb.type.key_data('width', width)

    def __str__(self):
        list = [str(self.start), str(self.end), str(self.angle), str(self.layer), str(self.width)]
        return '(fp_arc ' + ' '.join(list) +')'

class circle(object):
    '''Circle with center x1/y1 and radius through point x2/y2'''

    def __init__(self, layer, x1, y1, x2, y2, width):
        self.center = kicad.pcb.type.key_data('center', kicad.pcb.type.point2d(x1, y1))
        self.end = kicad.pcb.type.key_data('end', kicad.pcb.type.point2d(x2, y2))
        self.layer = kicad.pcb.type.key_data('layer', layer)
        self.width = kicad.pcb.type.key_data('width', width)

    def __str__(self):
        list = [str(self.center), str(self.end), str(self.layer), str(self.width)]
        return '(fp_circle ' + ' '.join(list) +')'

class line(object):
    '''Line from x1/y1 to x2/y2'''

    def __init__(self, layer, x1, y1, x2, y2, width):
        self.start = kicad.pcb.type.key_data('start', kicad.pcb.type.point2d(x1, y1))
        self.end = kicad.pcb.type.key_data('end', kicad.pcb.type.point2d(x2, y2))
        self.layer = kicad.pcb.type.key_data('layer', layer)
        self.width = kicad.pcb.type.key_data('width', kicad.pcb.type.value(width))

    def __str__(self):
        list = [str(self.start), str(self.end), str(self.layer), str(self.width)]
        return '(fp_line ' + ' '.join(list) +')'
