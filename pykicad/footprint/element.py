import pykicad


class text(object):
    '''Text at x/y'''

    def __init__(self, layer, text, value, x, y, size, thickness, angle = 0.0, style = pykicad.footprint.type.style.normal, visible = True):
        self.text = text
        if text == pykicad.footprint.type.text.reference:
            if value is not None:
                raise ValueError('Value has to be None when text is reference')
            self.value = 'REF**'
        elif text == pykicad.footprint.type.text.value:
            if value is not None:
                raise ValueError('Value has to be None when text is value')
            self.value = 'VAL**'
        else:
            self.value = pykicad.footprint.type.name(value)
        self.at = pykicad.footprint.type.key_data('at', pykicad.footprint.type.point3d(x, y, angle))
        self.layer = pykicad.footprint.type.key_data('layer', layer)
        self.visible = visible
        self.size = pykicad.footprint.type.key_data('size', pykicad.footprint.type.point2d(size, size))
        self.thickness = pykicad.footprint.type.key_data('thickness', pykicad.footprint.type.value(thickness))
        self.style = style

    def __str__(self):
        fontlist = [self.size, self.thickness]
        if self.style != pykicad.footprint.type.style.normal:
            fontlist += [self.style]
        font = pykicad.footprint.type.key_data('font', fontlist)
        effects = pykicad.footprint.type.key_data('effects', font)

        list = [str(self.text), str(self.value), str(self.at), str(self.layer)]
        if self.visible == False:
            list += ['hide']
        list += [str(effects)]
        return '(fp_text ' + ' '.join(list) +')'


class arc(object):
    '''Arc between x1/y1 and x2/y2 with given angle'''

    def __init__(self, layer, x1, y1, x2, y2, angle, width):
        self.start = pykicad.footprint.type.key_data('start', pykicad.footprint.type.point2d(x1, y1))
        self.end = pykicad.footprint.type.key_data('end', pykicad.footprint.type.point2d(x2, y2))
        self.angle = pykicad.footprint.type.key_data('angle', angle)
        self.layer = pykicad.footprint.type.key_data('layer', layer)
        self.width = pykicad.footprint.type.key_data('width', width)

    def __str__(self):
        list = [str(self.start), str(self.end), str(self.angle), str(self.layer), str(self.width)]
        return '(fp_arc ' + ' '.join(list) +')'


class circle(object):
    '''Circle with center x1/y1 and radius through point x2/y2'''

    def __init__(self, layer, x1, y1, x2, y2, width):
        self.center = pykicad.footprint.type.key_data('center', pykicad.footprint.type.point2d(x1, y1))
        self.end = pykicad.footprint.type.key_data('end', pykicad.footprint.type.point2d(x2, y2))
        self.layer = pykicad.footprint.type.key_data('layer', layer)
        self.width = pykicad.footprint.type.key_data('width', width)

    def __str__(self):
        list = [str(self.center), str(self.end), str(self.layer), str(self.width)]
        return '(fp_circle ' + ' '.join(list) +')'


class line(object):
    '''Line from x1/y1 to x2/y2'''

    def __init__(self, layer, x1, y1, x2, y2, width):
        self.start = pykicad.footprint.type.key_data('start', pykicad.footprint.type.point2d(x1, y1))
        self.end = pykicad.footprint.type.key_data('end', pykicad.footprint.type.point2d(x2, y2))
        self.layer = pykicad.footprint.type.key_data('layer', layer)
        self.width = pykicad.footprint.type.key_data('width', pykicad.footprint.type.value(width))

    def __str__(self):
        list = [str(self.start), str(self.end), str(self.layer), str(self.width)]
        return '(fp_line ' + ' '.join(list) +')'


class pad(object):
    '''Pad at x/y with size width/height in given type/shap on layers'''

    def __init__(self, layers, name, technology, shape, x, y, width, height, drill = None, angle = 0.0):
        self.name = pykicad.footprint.type.name(name if technology != pykicad.footprint.type.technology.np_thru_hole else '')
        self.technology = technology
        self.shape = shape
        self.at = pykicad.footprint.type.key_data('at', pykicad.footprint.type.point3d(x, y, angle))
        if shape == pykicad.footprint.type.shape.circle:
            if width != height:
                raise ValueError('width and height must be equal if shape is a circle')
            self.size = pykicad.footprint.type.key_data('size', pykicad.footprint.type.point2d(width, height))
        else:
            self.size = pykicad.footprint.type.key_data('size', pykicad.footprint.type.point2d(width, height))

        if technology == pykicad.footprint.type.technology.thru_hole or technology == pykicad.footprint.type.technology.np_thru_hole:
            if drill is None:
                raise ValueError('Thru hole pads need a drill diameter')
            self.drill = pykicad.footprint.type.key_data('drill', pykicad.footprint.type.value(drill))
        else:
            self.drill = None
        self.layers = pykicad.footprint.type.key_data('layers', layers)
        self.roundrect_rratio = pykicad.footprint.type.key_data('roundrect_rratio', pykicad.footprint.type.value(0.25))

    def __str__(self):
        list = [str(self.name), str(self.technology), str(self.shape), str(self.at), str(self.size)]
        if self.drill is not None:
            list += [str(self.drill)]
        list += [str(self.layers)]
        if self.shape == pykicad.footprint.type.shape.round_rectangle:
            list += [str(self.round_rectangle)]
        return '(pad ' + ' '.join(list) +')'


class multi_element(object):
    '''Multiple elements'''

    def __init__(self):
        self.elements = []

    def add(self, element):
        '''Add element to object'''

        self.elements.append(element)

    def remove(self, index):
        '''Remove element from object'''

        self.elements.remove(index)

    def __str__(self):
        result = ''
        for element in self.elements:
            result += str(element)+'\n  '
        return result


class rectangle(multi_element):
    '''Rectangle from x1/y1 to x2/y2'''

    def __init__(self, layer, x1, y1, x2, y2, width):
        super().__init__()
        super().add(line(layer, x1, y1, x2, y1, width))
        super().add(line(layer, x2, y1, x2, y2, width))
        super().add(line(layer, x2, y2, x1, y2, width))
        super().add(line(layer, x1, y2, x1, y1, width))


class centered_rectangle(rectangle):
    '''Centered rectangle at x/y with width/height'''

    def __init__(self, layer, x, y, width, height, line_width):
        x -= width / 2
        y -= height / 2

        super().__init__(layer, x, y, x + width, y + height, line_width)


class rounded_rectangle(multi_element):
    '''Rectangle with rounded edges from x1/y1 to x2/y2'''

    def __init__(self, layer, x1, y1, x2, y2, line_width, radius):
        super().__init__()
        super().add(line(layer, x1, y1 + radius, x1, y2 - radius, line_width))    # |
        super().add(arc(layer, x1 + radius, y2 - radius, x1 + radius, y2, 90.0, line_width))    # \
        super().add(line(layer, x1 + radius, y2, x2 - radius, y2, line_width))    # -
        super().add(arc(layer, x2 - radius, y2 - radius, x2, y2 - radius, 90.0, line_width))    # /
        super().add(line(layer, x2, y2 - radius, x2, y1 + radius, line_width))    # |
        super().add(arc(layer, x2 - radius, y1 + radius, x2 - radius, y1, 90.0, line_width))    # \
        super().add(line(layer, x2 - radius, y1, x1 + radius, y1, line_width))    # -
        super().add(arc(layer, x1 + radius, y1 + radius, x1, y1 + radius, 90.0, line_width))    # /


class beveled_rectangle(multi_element):
    '''Rectangle with beveled edges from x1/y1 to x2/y2'''

    def __init__(self, layer, x1, y1, x2, y2, line_width, bevel):
        super().__init__()
        super().add(line(layer, x1 + bevel, y1, x2 - bevel, y1, line_width))    # -
        super().add(line(layer, x2 - bevel, y1, x2, y1 + bevel, line_width))    # \
        super().add(line(layer, x2, y1 + bevel, x2, y2 - bevel, line_width))    # |
        super().add(line(layer, x2, y2 - bevel, x2 - bevel, y2, line_width))    # /
        super().add(line(layer, x2 - bevel, y2, x1 + bevel, y2, line_width))    # -
        super().add(line(layer, x1 + bevel, y2, x1, y2 - bevel, line_width))    # \
        super().add(line(layer, x1, y2 - bevel, x1, y1 + bevel, line_width))    # |
        super().add(line(layer, x1, y1 + bevel, x1 + bevel, y1, line_width))    # /


class centered_beveled_rectangle(beveled_rectangle):
    '''Centered rectangle with beveled edges at x/y with width/height'''

    def __init__(self, layer, x, y, width, height, line_width, bevel):
        x -= width / 2
        y -= height / 2

        super().__init__(layer, x, y, x + width, y + height, line_width, bevel)


class beveled_outline(multi_element):
    '''Outline with beveled corners every grid point from x1/y1 to x2/y2'''

    def __init__(self, layer, x1, y1, x2, y2, line_width, bevel, grid):
        super().__init__()

        x_rep = int((x2 - x1) / grid)
        y_rep = int((y2 - y1) / grid)
        for i in range(x_rep):
            if i != 0:
                super().add(line(layer, i * grid + x1, y1 + bevel, i * grid + x1 + bevel, y1, line_width))
            super().add(line(layer, i * grid + x1 + bevel, y1, i * grid + x1 + grid - bevel, y1, line_width))
            super().add(line(layer, i * grid + x1 + grid - bevel, y1, i * grid + x1 + grid, y1 + bevel, line_width))

        for i in range(y_rep):
            if i != 0:
                super().add(line(layer, x2 - bevel, i * grid + y1, x2, i * grid + y1 + bevel, line_width))
            super().add(line(layer, x2, i * grid + y1 + bevel, x2, i * grid + y1 + grid - bevel, line_width))
            super().add(line(layer, x2, i * grid + y1 + grid - bevel, x2 - bevel, i * grid + y1 + grid, line_width))

        for i in reversed(range(x_rep)):
            if i != (x_rep - 1):
                super().add(line(layer, i * grid + x1 + grid, y2 - bevel, i * grid + x1 + grid - bevel, y2, line_width))
            super().add(line(layer, i * grid + x1 + grid - bevel, y2, i * grid + x1 + bevel, y2, line_width))
            super().add(line(layer, i * grid + x1 + bevel, y2, i * grid + x1, y2 - bevel, line_width))

        for i in reversed(range(y_rep)):
            if i != (y_rep - 1):
                super().add(line(layer, x1 + bevel, i * grid + y1 + grid, x1, i * grid + y1 + grid - bevel, line_width))
            super().add(line(layer, x1, i * grid + y1 + grid - bevel, x1, i * grid + y1 + bevel, line_width))
            super().add(line(layer, x1, i * grid + y1 + bevel, x1 + bevel, i * grid + y1, line_width))


class centered_beveled_outline(beveled_outline):
    '''Centered outline with beveled corners every grid point at x/y with width/height'''

    def __init__(self, layer, x, y, width, height, line_width, bevel, grid):
        x -= width / 2
        y -= height / 2

        super().__init__(layer, x, y, x + width, y + height, line_width, bevel, grid)
