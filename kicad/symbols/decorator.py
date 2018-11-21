import math

import kicad.config
import kicad.symbols.element

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
        self.sign = 1 if direction == kicad.symbols.type.direction.left else -1
        self.elements = []

        if direction == kicad.symbols.type.direction.up or direction == kicad.symbols.type.direction.down:
            return

    @property
    def height(self):
        return kicad.config.symbols.PIN_GRID

    @property
    def width(self):
        return kicad.config.symbols.PIN_OFFSET + kicad.config.symbols.PIN_GRID * 1.5

class connector_male(base):
    '''Male connector symbol'''

    def __init__(self, x, y, direction, unit = 0):
        super().__init__(direction)

        line = kicad.symbols.element.polygon(0, kicad.symbols.type.fill.none, unit)
        line.add(kicad.symbols.element.point(x, y))
        x += self.sign * kicad.config.symbols.PIN_OFFSET
        line.add(kicad.symbols.element.point(x, y))
        self.elements.append(line)
        self.elements.append(
             kicad.symbols.element.rectangle(
                x,
                y - int(kicad.config.symbols.PIN_GRID * 0.2),
                x + int(self.sign * kicad.config.symbols.PIN_GRID),
                y + int(kicad.config.symbols.PIN_GRID * 0.2),
                kicad.config.symbols.DECORATION_THICKNESS,
                kicad.symbols.type.fill.foreground,
                unit
             )
        )

class connector_female(base):
    '''Female connector symbol'''

    def __init__(self, x, y, direction, unit = 0):
        super().__init__(direction)

        line = kicad.symbols.element.polygon(0, kicad.symbols.type.fill.none, unit)
        line.add(kicad.symbols.element.point(x, y))
        x += self.sign * (kicad.config.symbols.PIN_OFFSET + int(kicad.config.symbols.PIN_GRID * 0.6))
        line.add(kicad.symbols.element.point(x, y))
        self.elements.append(line)

        x += self.sign * int(kicad.config.symbols.PIN_GRID * 0.4)
        self.elements.append(
             kicad.symbols.element.arc(
                x,
                y,
                x,
                y - int(kicad.config.symbols.PIN_GRID * 0.4),
                x,
                y + int(kicad.config.symbols.PIN_GRID * 0.4),
                -90 - self.sign / 10,
                90 + self.sign / 10,
                int(kicad.config.symbols.PIN_GRID * 0.4),
                kicad.config.symbols.DECORATION_THICKNESS,
                kicad.symbols.type.fill.none,
                unit
             )
        )

class connector_screw(base):
    '''Screw connector symbol'''

    def __init__(self, x, y, direction, unit = 0):
        super().__init__(direction)

        line = kicad.symbols.element.polygon(0, kicad.symbols.type.fill.none, unit)
        line.add(kicad.symbols.element.point(x, y))
        x += self.sign * (kicad.config.symbols.PIN_OFFSET + int(kicad.config.symbols.PIN_GRID * 0.2))
        line.add(kicad.symbols.element.point(x, y))
        self.elements.append(line)

        x += self.sign * int(kicad.config.symbols.PIN_GRID * 0.4)
        self.elements.append(
             kicad.symbols.element.circle(
                x,
                y,
                int(kicad.config.symbols.PIN_GRID * 0.4),
                kicad.config.symbols.DECORATION_THICKNESS,
                kicad.symbols.type.fill.none,
                unit
             )
        )

        offset = int(math.sin(math.pi / 4) * kicad.config.symbols.PIN_GRID * 0.4)
        line = kicad.symbols.element.polygon(kicad.config.symbols.DECORATION_THICKNESS, kicad.symbols.type.fill.none, unit)
        line.add(kicad.symbols.element.point(x - offset, y - offset))
        line.add(kicad.symbols.element.point(x + offset, y + offset))
        self.elements.append(line)

class switch_wiper(base):
    '''Switch wiper'''

    def __init__(self, x, y, direction, unit = 0):
        super().__init__(direction)

        line = kicad.symbols.element.polygon(kicad.config.symbols.DECORATION_THICKNESS, kicad.symbols.type.fill.none, unit)
        line.add(kicad.symbols.element.point(x, y))
        x += self.sign * (kicad.config.symbols.PIN_OFFSET + kicad.config.symbols.PIN_GRID)
        line.add(kicad.symbols.element.point(x, y))
        x += int(self.sign * kicad.config.symbols.PIN_GRID * 1.2)
        y += int(kicad.config.symbols.PIN_GRID * 0.6)
        line.add(kicad.symbols.element.point(x, y))
        self.elements.append(line)

class switch_no(base):
    '''Switch "normaly open"'''

    def __init__(self, x, y, direction, unit = 0):
        super().__init__(direction)

        line = kicad.symbols.element.polygon(kicad.config.symbols.DECORATION_THICKNESS, kicad.symbols.type.fill.none, unit)
        line.add(kicad.symbols.element.point(x, y))
        x += self.sign * (kicad.config.symbols.PIN_OFFSET + kicad.config.symbols.PIN_GRID)
        line.add(kicad.symbols.element.point(x, y))
        self.elements.append(line)

class switch_nc_up(base):
    '''Switch "normaly closed" up'''

    def __init__(self, x, y, direction, unit = 0):
        super().__init__(direction)

        line = kicad.symbols.element.polygon(kicad.config.symbols.DECORATION_THICKNESS, kicad.symbols.type.fill.none, unit)
        line.add(kicad.symbols.element.point(x, y))
        x += self.sign * (kicad.config.symbols.PIN_OFFSET + kicad.config.symbols.PIN_GRID)
        line.add(kicad.symbols.element.point(x, y))
        y += int(kicad.config.symbols.PIN_GRID * 0.5)
        line.add(kicad.symbols.element.point(x, y))
        self.elements.append(line)

class switch_nc_down(base):
    '''Switch "normaly closed" down'''

    def __init__(self, x, y, direction, unit = 0):
        super().__init__(direction)

        line = kicad.symbols.element.polygon(kicad.config.symbols.DECORATION_THICKNESS, kicad.symbols.type.fill.none, unit)
        line.add(kicad.symbols.element.point(x, y))
        x += self.sign * (kicad.config.symbols.PIN_OFFSET + kicad.config.symbols.PIN_GRID)
        line.add(kicad.symbols.element.point(x, y))
        y -= int(kicad.config.symbols.PIN_GRID * 0.5)
        line.add(kicad.symbols.element.point(x, y))
        self.elements.append(line)

class dip_switch_off(base):
    '''DIP switch pictogram without wiper'''

    def __init__(self, x, y, direction, unit = 0):
        super().__init__(direction)

        x += self.sign * (kicad.config.symbols.PIN_OFFSET + int(kicad.config.symbols.PIN_GRID * 0.5))
        self.elements.append(
             kicad.symbols.element.rectangle(
                x,
                y - int(kicad.config.symbols.PIN_GRID * 0.4),
                x + self.sign * kicad.config.symbols.PIN_GRID * 2,
                y + int(kicad.config.symbols.PIN_GRID * 0.4),
                kicad.config.symbols.DECORATION_THICKNESS,
                kicad.symbols.type.fill.none,
                unit
             )
        )

class dip_switch_on(dip_switch_off):
    '''DIP switch pictogram with wiper'''

    def __init__(self, x, y, direction, unit = 0):
        super().__init__(x, y, direction, unit)

        x += self.sign * (kicad.config.symbols.PIN_OFFSET + int(kicad.config.symbols.PIN_GRID * 0.5))
        self.elements.append(
             kicad.symbols.element.rectangle(
                x,
                y - int(kicad.config.symbols.PIN_GRID * 0.4),
                x + self.sign * int(kicad.config.symbols.PIN_GRID * 0.5),
                y + int(kicad.config.symbols.PIN_GRID * 0.4),
                kicad.config.symbols.DECORATION_THICKNESS,
                kicad.symbols.type.fill.foreground,
                unit
             )
        )
