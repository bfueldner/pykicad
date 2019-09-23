"""KiCAD symbol decorator.

.. py::module:: pykicadlib.symbol.decorator
   :synopsis: KiCAD symbol decorator

.. moduleauthor:: Benjamin Füldner <benjamin@fueldner.net>
"""

import math
import pykicadlib
import pykicadlib.config

REGISTRY = {}   #: Decorator registry


class RegisterDecorator(type):
    """Metaclass to register decorators.

    :param str name:
        Class name
    :param list bases:
        List of bases
    :param str namespace:
        Namespace
    """

    def __init__(cls, name, bases, namespace):
        """Constructor."""
        super().__init__(name, bases, namespace)

        if name != 'Base':
            REGISTRY[name] = cls


class Base(metaclass=RegisterDecorator):
    """Base class for decorators.

    :param Direction direction:
        Direction of decorator
    """

    def __init__(self, direction):
        """Constructor."""
        self.sign = 1 if direction == pykicadlib.symbol.types.Direction.left else -1
        self.elements = []

        if direction in (pykicadlib.symbol.types.Direction.up,
                         pykicadlib.symbol.types.Direction.down):
            return

    @property
    def height(self):
        """Height.

        :type:
            int
        """
        return pykicadlib.config.Symbol.PIN_GRID

    @property
    def width(self):
        """Width.

        :type:
            int
        """
        return pykicadlib.config.Symbol.PIN_OFFSET + pykicadlib.config.Symbol.PIN_GRID * 1.5


class ConnectorMale(Base):
    """Male connector symbol.

    :param int x:
        X coordinate
    :param int y:
        Y coordinate
    :param Direction direction:
        Connector direction
    :param int unit:
        Unit
    """

    def __init__(self, x, y, direction, unit=0):
        """Constructor."""
        super().__init__(direction)

        line = pykicadlib.symbol.elements.Polygon(0, pykicadlib.symbol.types.Fill.none, unit)
        line.add(pykicadlib.symbol.elements.Point(x, y))
        x += self.sign * pykicadlib.config.Symbol.PIN_OFFSET
        line.add(pykicadlib.symbol.elements.Point(x, y))
        self.elements.append(line)
        self.elements.append(
            pykicadlib.symbol.elements.Rectangle(
                x,
                y - int(pykicadlib.config.Symbol.PIN_GRID * 0.2),
                x + int(self.sign * pykicadlib.config.Symbol.PIN_GRID),
                y + int(pykicadlib.config.Symbol.PIN_GRID * 0.2),
                pykicadlib.config.Symbol.DECORATION_THICKNESS,
                pykicadlib.symbol.types.Fill.foreground,
                unit
            )
        )


class ConnectorFemale(Base):
    """Female connector symbol.

    :param int x:
        X coordinate
    :param int y:
        Y coordinate
    :param Direction direction:
        Connector direction
    :param int unit:
        Unit
    """

    def __init__(self, x, y, direction, unit=0):
        """Constructor."""
        super().__init__(direction)

        line = pykicadlib.symbol.elements.Polygon(0, pykicadlib.symbol.types.Fill.none, unit)
        line.add(pykicadlib.symbol.elements.Point(x, y))
        x += self.sign * \
            (pykicadlib.config.Symbol.PIN_OFFSET + int(pykicadlib.config.Symbol.PIN_GRID * 0.6))
        line.add(pykicadlib.symbol.elements.Point(x, y))
        self.elements.append(line)

        x += self.sign * int(pykicadlib.config.Symbol.PIN_GRID * 0.4)
        self.elements.append(
            pykicadlib.symbol.elements.Arc(
                x,
                y,
                x,
                y - int(pykicadlib.config.Symbol.PIN_GRID * 0.4),
                x,
                y + int(pykicadlib.config.Symbol.PIN_GRID * 0.4),
                -90 - self.sign / 10,
                90 + self.sign / 10,
                int(pykicadlib.config.Symbol.PIN_GRID * 0.4),
                pykicadlib.config.Symbol.DECORATION_THICKNESS,
                pykicadlib.symbol.types.Fill.none,
                unit
            )
        )


class ConnectorScrew(Base):
    """Screw connector symbol.

    :param int x:
        X coordinate
    :param int y:
        Y coordinate
    :param Direction direction:
        Connector direction
    :param int unit:
        Unit
    """

    def __init__(self, x, y, direction, unit=0):
        """Constructor."""
        super().__init__(direction)

        line = pykicadlib.symbol.elements.Polygon(0, pykicadlib.symbol.types.Fill.none, unit)
        line.add(pykicadlib.symbol.elements.Point(x, y))
        x += self.sign * \
            (pykicadlib.config.Symbol.PIN_OFFSET + int(pykicadlib.config.Symbol.PIN_GRID * 0.2))
        line.add(pykicadlib.symbol.elements.Point(x, y))
        self.elements.append(line)

        x += self.sign * int(pykicadlib.config.Symbol.PIN_GRID * 0.4)
        self.elements.append(
            pykicadlib.symbol.elements.Circle(
                x,
                y,
                int(pykicadlib.config.Symbol.PIN_GRID * 0.4),
                pykicadlib.config.Symbol.DECORATION_THICKNESS,
                pykicadlib.symbol.types.Fill.none,
                unit
            )
        )

        offset = int(math.sin(math.pi / 4) * pykicadlib.config.Symbol.PIN_GRID * 0.4)
        line = pykicadlib.symbol.elements.Polygon(
            pykicadlib.config.Symbol.DECORATION_THICKNESS,
            pykicadlib.symbol.types.Fill.none,
            unit
        )
        line.add(pykicadlib.symbol.elements.Point(x - offset, y - offset))
        line.add(pykicadlib.symbol.elements.Point(x + offset, y + offset))
        self.elements.append(line)


class SwitchWiper(Base):
    """Switch wiper.

    :param int x:
        X coordinate
    :param int y:
        Y coordinate
    :param Direction direction:
        Connector direction
    :param int unit:
        Unit
    """

    def __init__(self, x, y, direction, unit=0):
        """Constructor."""
        super().__init__(direction)

        line = pykicadlib.symbol.elements.Polygon(
            pykicadlib.config.Symbol.DECORATION_THICKNESS,
            pykicadlib.symbol.types.Fill.none,
            unit
        )
        line.add(pykicadlib.symbol.elements.Point(x, y))
        x += self.sign * (pykicadlib.config.Symbol.PIN_OFFSET + pykicadlib.config.Symbol.PIN_GRID)
        line.add(pykicadlib.symbol.elements.Point(x, y))
        x += int(self.sign * pykicadlib.config.Symbol.PIN_GRID * 1.2)
        y += int(pykicadlib.config.Symbol.PIN_GRID * 0.6)
        line.add(pykicadlib.symbol.elements.Point(x, y))
        self.elements.append(line)


class SwitchNo(Base):
    """Switch 'normaly open'.

    :param int x:
        X coordinate
    :param int y:
        Y coordinate
    :param Direction direction:
        Connector direction
    :param int unit:
        Unit
    """

    def __init__(self, x, y, direction, unit=0):
        """Constructor."""
        super().__init__(direction)

        line = pykicadlib.symbol.elements.Polygon(
            pykicadlib.config.Symbol.DECORATION_THICKNESS,
            pykicadlib.symbol.types.Fill.none,
            unit
        )
        line.add(pykicadlib.symbol.elements.Point(x, y))
        x += self.sign * (pykicadlib.config.Symbol.PIN_OFFSET + pykicadlib.config.Symbol.PIN_GRID)
        line.add(pykicadlib.symbol.elements.Point(x, y))
        self.elements.append(line)


class SwitchNcUp(Base):
    """Switch 'normaly closed' up.

    :param int x:
        X coordinate
    :param int y:
        Y coordinate
    :param Direction direction:
        Connector direction
    :param int unit:
        Unit
    """

    def __init__(self, x, y, direction, unit=0):
        """Constructor."""
        super().__init__(direction)

        line = pykicadlib.symbol.elements.Polygon(
            pykicadlib.config.Symbol.DECORATION_THICKNESS,
            pykicadlib.symbol.types.Fill.none,
            unit
        )
        line.add(pykicadlib.symbol.elements.Point(x, y))
        x += self.sign * (pykicadlib.config.Symbol.PIN_OFFSET + pykicadlib.config.Symbol.PIN_GRID)
        line.add(pykicadlib.symbol.elements.Point(x, y))
        y += int(pykicadlib.config.Symbol.PIN_GRID * 0.5)
        line.add(pykicadlib.symbol.elements.Point(x, y))
        self.elements.append(line)


class SwitchNcDown(Base):
    """Switch 'normaly closed' down.

    :param int x:
        X coordinate
    :param int y:
        Y coordinate
    :param Direction direction:
        Connector direction
    :param int unit:
        Unit
    """

    def __init__(self, x, y, direction, unit=0):
        """Constructor."""
        super().__init__(direction)

        line = pykicadlib.symbol.elements.Polygon(
            pykicadlib.config.Symbol.DECORATION_THICKNESS,
            pykicadlib.symbol.types.Fill.none,
            unit
        )
        line.add(pykicadlib.symbol.elements.Point(x, y))
        x += self.sign * (pykicadlib.config.Symbol.PIN_OFFSET + pykicadlib.config.Symbol.PIN_GRID)
        line.add(pykicadlib.symbol.elements.Point(x, y))
        y -= int(pykicadlib.config.Symbol.PIN_GRID * 0.5)
        line.add(pykicadlib.symbol.elements.Point(x, y))
        self.elements.append(line)


class DipSwitchOff(Base):
    """DIP switch pictogram without wiper.

    :param int x:
        X coordinate
    :param int y:
        Y coordinate
    :param Direction direction:
        Connector direction
    :param int unit:
        Unit
    """

    def __init__(self, x, y, direction, unit=0):
        """Constructor."""
        super().__init__(direction)

        x += self.sign * \
            (pykicadlib.config.Symbol.PIN_OFFSET + int(pykicadlib.config.Symbol.PIN_GRID * 0.5))
        self.elements.append(
            pykicadlib.symbol.elements.Rectangle(
                x,
                y - int(pykicadlib.config.Symbol.PIN_GRID * 0.4),
                x + self.sign * pykicadlib.config.Symbol.PIN_GRID * 2,
                y + int(pykicadlib.config.Symbol.PIN_GRID * 0.4),
                pykicadlib.config.Symbol.DECORATION_THICKNESS,
                pykicadlib.symbol.types.Fill.none,
                unit
            )
        )


class DipSwitchOn(DipSwitchOff):
    """DIP switch pictogram with wiper.

    :param int x:
        X coordinate
    :param int y:
        Y coordinate
    :param Direction direction:
        Connector direction
    :param int unit:
        Unit
    """

    def __init__(self, x, y, direction, unit=0):
        """Constructor."""
        super().__init__(x, y, direction, unit)

        x += self.sign * \
            (pykicadlib.config.Symbol.PIN_OFFSET + int(pykicadlib.config.Symbol.PIN_GRID * 0.5))
        self.elements.append(
            pykicadlib.symbol.elements.Rectangle(
                x,
                y - int(pykicadlib.config.Symbol.PIN_GRID * 0.4),
                x + self.sign * int(pykicadlib.config.Symbol.PIN_GRID * 0.5),
                y + int(pykicadlib.config.Symbol.PIN_GRID * 0.4),
                pykicadlib.config.Symbol.DECORATION_THICKNESS,
                pykicadlib.symbol.types.Fill.foreground,
                unit
            )
        )
