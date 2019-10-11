"""KiCAD symbol decorator.

.. py::module:: pykicadlib.symbol.decorators.connector_screw
   :synopsis: KiCAD symbol decorator

.. moduleauthor:: Benjamin Füldner <benjamin@fueldner.net>
"""
from math import sin, pi
from pykicadlib.config import Symbol as Config
from pykicadlib.symbol.decorator import Decorator
from pykicadlib.symbol.elements import Circle, Polygon


class ConnectorScrew(Decorator):
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

        line = Polygon()
        line.thickness = 0
        line.unit = unit
        line.add(Polygon.Point(x, y))
        x += self.sign * (Config.PIN_OFFSET + int(Config.PIN_GRID * 0.2))
        line.add(Polygon.Point(x, y))
        self.elements.append(line)

        x += self.sign * int(Config.PIN_GRID * 0.4)
        circle = Circle(
            x,
            y,
            int(Config.PIN_GRID * 0.4)
        )
        circle.thickness = Config.DECORATION_THICKNESS
        circle.unit = unit
        self.elements.append(circle)

        offset = int(sin(pi / 4) * Config.PIN_GRID * 0.4)
        line = Polygon()
        line.thickness = Config.DECORATION_THICKNESS
        line.unit = unit
        line.add(Polygon.Point(x - offset, y - offset))
        line.add(Polygon.Point(x + offset, y + offset))
        self.elements.append(line)
