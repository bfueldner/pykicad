import time

import pykicadlib
import pykicadlib.config

registry = {}


class register_generator(type):
    '''Metaclass to register generators'''

    def __init__(self, name, bases, namespace):
        super().__init__(name, bases, namespace)

        if name != 'base':
        #   print("Register '{}' footprint generator".format(name))
            registry[name] = self


class base(object, metaclass = register_generator):
    '''Base class for footprint generators'''

    def __init__(self, technology, name, model, description = None, tags = None):
        self.technology = technology
        self.name = name
        self.model = model
        self.description = description if description is not None and len(description) else None
        self.tags = tags if tags is not None and  len(tags) else None
        self.elements = []

    #    if add_ref_value:
    #        self.elements.append(text(cfg.FOOTPRINT_REFERENCE_LAYER, "reference", "REF**", 0, 0, 0, cfg.FOOTPRINT_REFERENCE_FONT_SIZE, cfg.FOOTPRINT_REFERENCE_FONT_THICKNESS))
    #        self.elements.append(text(cfg.FOOTPRINT_VALUE_LAYER, "value", "VAL**", 0, cfg.FOOTPRINT_VALUE_FONT_SIZE + 2 * cfg.FOOTPRINT_VALUE_FONT_THICKNESS, 0, cfg.FOOTPRINT_VALUE_FONT_SIZE, cfg.FOOTPRINT_VALUE_FONT_THICKNESS))

    def add(self, element):
        '''Add element to generator list'''

        self.elements.append(element)

    def remove(self, index):
        '''Remove element from generator list'''

        self.elements.remove(index)

    def __str__(self):
        parts = [
            str(pykicadlib.footprint.type.key_data('tedit', '{:8X}'.format(int(time.time()))))
        ]

        if self.description is not None:
            parts += [
                str(pykicadlib.footprint.type.key_data('descr', pykicadlib.footprint.type.name(self.description)))
            ]

        if self.tags is not None:
            parts += [
                str(pykicadlib.footprint.type.key_data('tags', pykicadlib.footprint.type.name(self.tags)))
            ]

        if self.technology.value is not None:
            parts += [
                str(pykicadlib.footprint.type.key_data('attr', self.technology))
            ]

        for element in self.elements:
            parts.append(str(element))

        if self.model is not None:
            model = [
                str(pykicadlib.footprint.type.key_data('at', pykicadlib.footprint.type.key_data('xyz', pykicadlib.footprint.type.point3d(0.0, 0.0, 0.0) ) )),
                str(pykicadlib.footprint.type.key_data('scale', pykicadlib.footprint.type.key_data('xyz', pykicadlib.footprint.type.point3d(1.0, 1.0, 1.0) ) )),
                str(pykicadlib.footprint.type.key_data('rotate', pykicadlib.footprint.type.key_data('xyz', pykicadlib.footprint.type.point3d(0.0, 0.0, 0.0) ) ))
            ]

            model = '\n    '.join(model)
            parts += [
                str(pykicadlib.footprint.type.key_data('model', [pykicadlib.footprint.type.name(self.model), '\n    '+model+'\n']))
            ]

        return str(pykicadlib.footprint.type.key_data('module', [pykicadlib.footprint.type.name(self.name), pykicadlib.footprint.type.key_data('layer', pykicadlib.footprint.layer.copper_top), '\n  '.join(parts) ]))

        x = '''
        result = '(module {} (tedit {:8X})\n'.format(self.name, int(time.time()))
        if self.technology == pykicadlib.footprint.type.technology.smd:
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
