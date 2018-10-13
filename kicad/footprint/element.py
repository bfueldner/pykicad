import kicad.footprint.type

class text(object):
    '''Generate text at x/y'''

    def __init__(self, layer, text, value, x, y, size, thickness, angle = 0.0, style = kicad.footprint.type.style.normal, visible = True):
        self.text = text
        if text == kicad.footprint.type.text.reference:
            if value is not None:
                raise ValueError('Value is ignored when text is reference')
            self.value = 'REF**'
        elif text == kicad.footprint.type.text.value:
            if value is not None:
                raise ValueError('Value is ignored when text is value')
            self.value = 'VAL**'
        else:
            self.value = kicad.footprint.type.name(value)
        self.at = kicad.footprint.type.key_data('at', kicad.footprint.type.point3d(x, y, angle))
        self.layer = kicad.footprint.type.key_data('layer', layer)
        self.visible = visible
        self.size = kicad.footprint.type.key_data('size', kicad.footprint.type.point2d(size, size))
        self.thickness = kicad.footprint.type.key_data('thickness', kicad.footprint.type.value(thickness))
        self.style = style

    def __str__(self):
        fontlist = [self.size, self.thickness]
        if self.style != kicad.footprint.type.style.normal:
            fontlist += [self.style]
        font = kicad.footprint.type.key_data('font', fontlist)
        effects = kicad.footprint.type.key_data('effects', font)

        list = [str(self.text), str(self.value), str(self.at), str(self.layer)]
        if self.visible == False:
            list += ['hide']
        list += [str(effects)]
        return '(fp_text ' + ' '.join(list) +')'

class arc(object):
    '''Arc between x1/y1 and x2/y2 with given angle'''

    def __init__(self, layer, x1, y1, x2, y2, angle, width):
        self.start = kicad.footprint.type.key_data('start', kicad.footprint.type.point2d(x1, y1))
        self.end = kicad.footprint.type.key_data('end', kicad.footprint.type.point2d(x2, y2))
        self.angle = kicad.footprint.type.key_data('angle', angle)
        self.layer = kicad.footprint.type.key_data('layer', layer)
        self.width = kicad.footprint.type.key_data('width', width)

    def __str__(self):
        list = [str(self.start), str(self.end), str(self.angle), str(self.layer), str(self.width)]
        return '(fp_arc ' + ' '.join(list) +')'

class circle(object):
    '''Circle with center x1/y1 and radius through point x2/y2'''

    def __init__(self, layer, x1, y1, x2, y2, width):
        self.center = kicad.footprint.type.key_data('center', kicad.footprint.type.point2d(x1, y1))
        self.end = kicad.footprint.type.key_data('end', kicad.footprint.type.point2d(x2, y2))
        self.layer = kicad.footprint.type.key_data('layer', layer)
        self.width = kicad.footprint.type.key_data('width', width)

    def __str__(self):
        list = [str(self.center), str(self.end), str(self.layer), str(self.width)]
        return '(fp_circle ' + ' '.join(list) +')'

class line(object):
    '''Line from x1/y1 to x2/y2'''

    def __init__(self, layer, x1, y1, x2, y2, width):
        self.start = kicad.footprint.type.key_data('start', kicad.footprint.type.point2d(x1, y1))
        self.end = kicad.footprint.type.key_data('end', kicad.footprint.type.point2d(x2, y2))
        self.layer = kicad.footprint.type.key_data('layer', layer)
        self.width = kicad.footprint.type.key_data('width', kicad.footprint.type.value(width))

    def __str__(self):
        list = [str(self.start), str(self.end), str(self.layer), str(self.width)]
        return '(fp_line ' + ' '.join(list) +')'

class rectangle(object):
    '''Rectangle from x1/y1 to x2/y2'''

    def __init__(self, layer, x1, y1, x2, y2, width):
        self.element = []
        self.element.append(line(layer, x1, y1, x2, y1, width))
        self.element.append(line(layer, x2, y1, x2, y2, width))
        self.element.append(line(layer, x2, y2, x1, y2, width))
        self.element.append(line(layer, x1, y2, x1, y1, width))

    def __str__(self):
        result = ''
        for element in self.elements:
            result += str(element)
        return result

class centered_rectangle(object):
    '''Centered rectangle at x/y with width/height'''

    pass

class pad(object):
    '''Pad at x/y with size width/height in given type/shap on layers'''

    def __init__(self, layers, name, technology, shape, x, y, width, height, drill = None, angle = 0.0):
        self.name = kicad.footprint.type.name(name if technology != kicad.footprint.type.technology.np_thru_hole else '')
        self.technology = technology
        self.shape = shape
        self.at = kicad.footprint.type.key_data('at', kicad.footprint.type.point3d(x, y, angle))
        if shape == kicad.footprint.type.shape.circle:
            if width != height:
                raise ValueError('width and height must be equal if shape is a circle')
            self.size = kicad.footprint.type.key_data('size', kicad.footprint.type.point2d(width, height))
        else:
            self.size = kicad.footprint.type.key_data('size', kicad.footprint.type.point2d(width, height))

        if technology == kicad.footprint.type.technology.thru_hole or technology == kicad.footprint.type.technology.np_thru_hole:
            if drill is None:
                raise ValueError('Thru hole pads need a drill diameter')
            self.drill = kicad.footprint.type.key_data('drill', kicad.footprint.type.value(drill))
        else:
            self.drill = None
        self.layers = kicad.footprint.type.key_data('layers', layers)
        self.roundrect_rratio = kicad.footprint.type.key_data('roundrect_rratio', kicad.footprint.type.value(0.25))

    def __str__(self):
        list = [str(self.name), str(self.technology), str(self.shape), str(self.at), str(self.size)]
        if self.drill is not None:
            list += [str(self.drill)]
        list += [str(self.layers)]
        if self.shape == kicad.footprint.type.shape.round_rectangle:
            list += [str(self.round_rectangle)]
        return '(pad ' + ' '.join(list) +')'
