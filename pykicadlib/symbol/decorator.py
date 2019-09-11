import math

import pykicadlib
import pykicadlib.config


registry = {}

class register_decorator(type):
    '''Metaclass to register decorators'''

    def __init__(self, name, bases, namespace):
        super().__init__(name, bases, namespace)

        if name != 'base':
            registry[name] = self


class base(object, metaclass = register_decorator):
    '''Base class for decorators'''

    def __init__(self, direction):
        self.sign = 1 if direction == pykicadlib.symbol.type.direction.left else -1
        self.elements = []

        if direction == pykicadlib.symbol.type.direction.up or direction == pykicadlib.symbol.type.direction.down:
            return

    @property
    def height(self):
        return pykicadlib.config.symbol.PIN_GRID

    @property
    def width(self):
        return pykicadlib.config.symbol.PIN_OFFSET + pykicadlib.config.symbol.PIN_GRID * 1.5


class connector_male(base):
    '''Male connector symbol'''

    def __init__(self, x, y, direction, unit = 0):
        super().__init__(direction)

        line = pykicadlib.symbol.element.polygon(0, pykicadlib.symbol.type.fill.none, unit)
        line.add(pykicadlib.symbol.element.point(x, y))
        x += self.sign * pykicadlib.config.symbol.PIN_OFFSET
        line.add(pykicadlib.symbol.element.point(x, y))
        self.elements.append(line)
        self.elements.append(
             pykicadlib.symbol.element.rectangle(
                x,
                y - int(pykicadlib.config.symbol.PIN_GRID * 0.2),
                x + int(self.sign * pykicadlib.config.symbol.PIN_GRID),
                y + int(pykicadlib.config.symbol.PIN_GRID * 0.2),
                pykicadlib.config.symbol.DECORATION_THICKNESS,
                pykicadlib.symbol.type.fill.foreground,
                unit
             )
        )


class connector_female(base):
    '''Female connector symbol'''

    def __init__(self, x, y, direction, unit = 0):
        super().__init__(direction)

        line = pykicadlib.symbol.element.polygon(0, pykicadlib.symbol.type.fill.none, unit)
        line.add(pykicadlib.symbol.element.point(x, y))
        x += self.sign * (pykicadlib.config.symbol.PIN_OFFSET + int(pykicadlib.config.symbol.PIN_GRID * 0.6))
        line.add(pykicadlib.symbol.element.point(x, y))
        self.elements.append(line)

        x += self.sign * int(pykicadlib.config.symbol.PIN_GRID * 0.4)
        self.elements.append(
             pykicadlib.symbol.element.arc(
                x,
                y,
                x,
                y - int(pykicadlib.config.symbol.PIN_GRID * 0.4),
                x,
                y + int(pykicadlib.config.symbol.PIN_GRID * 0.4),
                -90 - self.sign / 10,
                90 + self.sign / 10,
                int(pykicadlib.config.symbol.PIN_GRID * 0.4),
                pykicadlib.config.symbol.DECORATION_THICKNESS,
                pykicadlib.symbol.type.fill.none,
                unit
             )
        )


class connector_screw(base):
    '''Screw connector symbol'''

    def __init__(self, x, y, direction, unit = 0):
        super().__init__(direction)

        line = pykicadlib.symbol.element.polygon(0, pykicadlib.symbol.type.fill.none, unit)
        line.add(pykicadlib.symbol.element.point(x, y))
        x += self.sign * (pykicadlib.config.symbol.PIN_OFFSET + int(pykicadlib.config.symbol.PIN_GRID * 0.2))
        line.add(pykicadlib.symbol.element.point(x, y))
        self.elements.append(line)

        x += self.sign * int(pykicadlib.config.symbol.PIN_GRID * 0.4)
        self.elements.append(
             pykicadlib.symbol.element.circle(
                x,
                y,
                int(pykicadlib.config.symbol.PIN_GRID * 0.4),
                pykicadlib.config.symbol.DECORATION_THICKNESS,
                pykicadlib.symbol.type.fill.none,
                unit
             )
        )

        offset = int(math.sin(math.pi / 4) * pykicadlib.config.symbol.PIN_GRID * 0.4)
        line = pykicadlib.symbol.element.polygon(pykicadlib.config.symbol.DECORATION_THICKNESS, pykicadlib.symbol.type.fill.none, unit)
        line.add(pykicadlib.symbol.element.point(x - offset, y - offset))
        line.add(pykicadlib.symbol.element.point(x + offset, y + offset))
        self.elements.append(line)


class switch_wiper(base):
    '''Switch wiper'''

    def __init__(self, x, y, direction, unit = 0):
        super().__init__(direction)

        line = pykicadlib.symbol.element.polygon(pykicadlib.config.symbol.DECORATION_THICKNESS, pykicadlib.symbol.type.fill.none, unit)
        line.add(pykicadlib.symbol.element.point(x, y))
        x += self.sign * (pykicadlib.config.symbol.PIN_OFFSET + pykicadlib.config.symbol.PIN_GRID)
        line.add(pykicadlib.symbol.element.point(x, y))
        x += int(self.sign * pykicadlib.config.symbol.PIN_GRID * 1.2)
        y += int(pykicadlib.config.symbol.PIN_GRID * 0.6)
        line.add(pykicadlib.symbol.element.point(x, y))
        self.elements.append(line)


class switch_no(base):
    '''Switch "normaly open"'''

    def __init__(self, x, y, direction, unit = 0):
        super().__init__(direction)

        line = pykicadlib.symbol.element.polygon(pykicadlib.config.symbol.DECORATION_THICKNESS, pykicadlib.symbol.type.fill.none, unit)
        line.add(pykicadlib.symbol.element.point(x, y))
        x += self.sign * (pykicadlib.config.symbol.PIN_OFFSET + pykicadlib.config.symbol.PIN_GRID)
        line.add(pykicadlib.symbol.element.point(x, y))
        self.elements.append(line)


class switch_nc_up(base):
    '''Switch "normaly closed" up'''

    def __init__(self, x, y, direction, unit = 0):
        super().__init__(direction)

        line = pykicadlib.symbol.element.polygon(pykicadlib.config.symbol.DECORATION_THICKNESS, pykicadlib.symbol.type.fill.none, unit)
        line.add(pykicadlib.symbol.element.point(x, y))
        x += self.sign * (pykicadlib.config.symbol.PIN_OFFSET + pykicadlib.config.symbol.PIN_GRID)
        line.add(pykicadlib.symbol.element.point(x, y))
        y += int(pykicadlib.config.symbol.PIN_GRID * 0.5)
        line.add(pykicadlib.symbol.element.point(x, y))
        self.elements.append(line)


class switch_nc_down(base):
    '''Switch "normaly closed" down'''

    def __init__(self, x, y, direction, unit = 0):
        super().__init__(direction)

        line = pykicadlib.symbol.element.polygon(pykicadlib.config.symbol.DECORATION_THICKNESS, pykicadlib.symbol.type.fill.none, unit)
        line.add(pykicadlib.symbol.element.point(x, y))
        x += self.sign * (pykicadlib.config.symbol.PIN_OFFSET + pykicadlib.config.symbol.PIN_GRID)
        line.add(pykicadlib.symbol.element.point(x, y))
        y -= int(pykicadlib.config.symbol.PIN_GRID * 0.5)
        line.add(pykicadlib.symbol.element.point(x, y))
        self.elements.append(line)


class dip_switch_off(base):
    '''DIP switch pictogram without wiper'''

    def __init__(self, x, y, direction, unit = 0):
        super().__init__(direction)

        x += self.sign * (pykicadlib.config.symbol.PIN_OFFSET + int(pykicadlib.config.symbol.PIN_GRID * 0.5))
        self.elements.append(
             pykicadlib.symbol.element.rectangle(
                x,
                y - int(pykicadlib.config.symbol.PIN_GRID * 0.4),
                x + self.sign * pykicadlib.config.symbol.PIN_GRID * 2,
                y + int(pykicadlib.config.symbol.PIN_GRID * 0.4),
                pykicadlib.config.symbol.DECORATION_THICKNESS,
                pykicadlib.symbol.type.fill.none,
                unit
             )
        )


class dip_switch_on(dip_switch_off):
    '''DIP switch pictogram with wiper'''

    def __init__(self, x, y, direction, unit = 0):
        super().__init__(x, y, direction, unit)

        x += self.sign * (pykicadlib.config.symbol.PIN_OFFSET + int(pykicadlib.config.symbol.PIN_GRID * 0.5))
        self.elements.append(
             pykicadlib.symbol.element.rectangle(
                x,
                y - int(pykicadlib.config.symbol.PIN_GRID * 0.4),
                x + self.sign * int(pykicadlib.config.symbol.PIN_GRID * 0.5),
                y + int(pykicadlib.config.symbol.PIN_GRID * 0.4),
                pykicadlib.config.symbol.DECORATION_THICKNESS,
                pykicadlib.symbol.type.fill.foreground,
                unit
             )
        )
