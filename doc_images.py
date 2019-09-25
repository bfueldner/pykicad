import pykicadlib


class Generator():

    def __init__(self, name):
        filename = name + pykicadlib.config.Symbol.LIBRARY_EXTENSION
        self.symbol = pykicadlib.symbol.library.Symbol(name, 'T', '', '')
        self.generate()

        self.file = open(filename, 'w')
        self.file.write(pykicadlib.config.Symbol.LIBRARY_START)
        self.file.write(str(self.symbol))
        self.file.write(pykicadlib.config.Symbol.LIBRARY_END)
        self.file.close()

    def generate(self):
        pass


class SymbolTypesFill(Generator):

    def generate(self):
        self.symbol.elements.append(pykicadlib.symbol.elements.Rectangle(0, 0, 750, 750, 1, pykicadlib.symbol.types.Fill.none))

        self.symbol.elements.append(pykicadlib.symbol.elements.Rectangle(10, 410, 190, 590, 0, pykicadlib.symbol.types.Fill.none))
        self.symbol.elements.append(pykicadlib.symbol.elements.Rectangle(10, 210, 190, 390, 0, pykicadlib.symbol.types.Fill.foreground))
        self.symbol.elements.append(pykicadlib.symbol.elements.Rectangle(10, 10, 190, 190, 0, pykicadlib.symbol.types.Fill.background))

        self.symbol.elements.append(pykicadlib.symbol.elements.Text(200, 500, "none", 50, 0, hjustify=pykicadlib.symbol.types.HJustify.left))
        self.symbol.elements.append(pykicadlib.symbol.elements.Text(200, 300, "foreground", 50, 0, hjustify=pykicadlib.symbol.types.HJustify.left))
        self.symbol.elements.append(pykicadlib.symbol.elements.Text(200, 100, "background", 50, 0, hjustify=pykicadlib.symbol.types.HJustify.left))


class SymbolTypesShape(Generator):

    def generate(self):
        self.symbol.elements.append(pykicadlib.symbol.elements.Rectangle(0, 0, 750, 750, 1, pykicadlib.symbol.types.Fill.none))

        y = 1000
        for shape in pykicadlib.symbol.types.Shape:
            self.symbol.elements.append(pykicadlib.symbol.elements.Pin(100, y, 'Name', 'Number', pykicadlib.config.Symbol.PIN_LENGTH, pykicadlib.symbol.types.Direction.left, pykicadlib.config.Symbol.PIN_NAME_SIZE, pykicadlib.config.Symbol.PIN_NUMBER_SIZE, shape=shape))
            self.symbol.elements.append(pykicadlib.symbol.elements.Text(250, y, shape.name, 50, 0, hjustify=pykicadlib.symbol.types.HJustify.left))
            line = pykicadlib.symbol.elements.Polygon(pykicadlib.config.Symbol.ELEMENT_THICKNESS, pykicadlib.symbol.types.Fill.none)
            line.add(pykicadlib.symbol.elements.Point(200, y - 50))
            line.add(pykicadlib.symbol.elements.Point(200, y + 50))
            self.symbol.elements.append(line)
            y -= 200

if __name__ == '__main__':
    SymbolTypesFill('symbol_types_fill')
    SymbolTypesShape('symbol_types_shape')
