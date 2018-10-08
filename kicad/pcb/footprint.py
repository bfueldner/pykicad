import time

import kicad.pcb.element

class base(object):
    '''Footprint class'''

    def __init__(self, technology, name, model, description = None, tags = None):
        self.technology = technology
        self.name = name
        self.model = model
        self.description = description
        self.tags = tags
        self.element = []

    #    if add_ref_value:
    #        self.elements.append(text(cfg.FOOTPRINT_REFERENCE_LAYER, "reference", "REF**", 0, 0, 0, cfg.FOOTPRINT_REFERENCE_FONT_SIZE, cfg.FOOTPRINT_REFERENCE_FONT_THICKNESS))
    #        self.elements.append(text(cfg.FOOTPRINT_VALUE_LAYER, "value", "VAL**", 0, cfg.FOOTPRINT_VALUE_FONT_SIZE + 2 * cfg.FOOTPRINT_VALUE_FONT_THICKNESS, 0, cfg.FOOTPRINT_VALUE_FONT_SIZE, cfg.FOOTPRINT_VALUE_FONT_THICKNESS))

    def add(self, element):
        '''Add element to generator list'''
        self.element.append(element)

    def remove(self, index):
        '''Remove element from generator list'''
        self.element.remove(index)

    def __str__(self):
        model = [
            str(kicad.pcb.type.key_data('xyz', kicad.pcb.type.point3d(0.0, 0.0, 0.0) )),
            str(kicad.pcb.type.key_data('xyz', kicad.pcb.type.point3d(1.0, 1.0, 1.0) )),
            str(kicad.pcb.type.key_data('xyz', kicad.pcb.type.point3d(0.0, 0.0, 0.0) )),
        ]

        parts = [
            str(kicad.pcb.type.key_data('layer', kicad.pcb.layer.copper_top)),
            str(kicad.pcb.type.key_data('tedit', '{:8X}'.format(int(time.time())))),
            str(kicad.pcb.type.key_data('descr', kicad.pcb.type.text(self.description))),
            str(kicad.pcb.type.key_data('tags', self.tags))
        ]

        if self.technology.value is not None:
            parts += [ str(kicad.pcb.type.key_data('attr', self.technology)) ]

        return '\n'.join(parts)

        x = '''
        result = '(module {} (tedit {:8X})\n'.format(self.name, int(time.time()))
        if self.technology == kicad.pcb.type.technology.smd:
            result += '  (attr smd)\n'

        if len(self.description):
            result += '  (descr "'+self.description+'")\n'

        if len(self.tags):
            result += '  (tags "'+self.tags+'")\n'

        for element in self.elements:
            result += element.render()

        if len(self.model):
            result += '  (model '+self.model+'\n    (at (xyz 0 0 0))\n    (scale (xyz 1 1 1))\n    (rotate (xyz 0 0 0))\n  )\n'

        result += ')\n'
        '''
        return result
